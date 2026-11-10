#!/usr/bin/env python3
"""Flag mechanical preservation differences in two UTF-8 text files; no network."""

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys


NUMBER = re.compile(
    r"(?<!\w)[+\-\u2212]?(?:\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?)"
    r"(?:[eE][+\-\u2212]?\d+)?(?:\s*%)?"
)
URL = re.compile(r"https?://[^\s<>\"']+", re.IGNORECASE)


def sha256_bytes(value):
    return hashlib.sha256(value).hexdigest()


def numeric_tokens(text):
    return Counter(re.sub(r"\s+", "", m.group()) for m in NUMBER.finditer(text))


def url_tokens(text):
    values = []
    for match in URL.finditer(text):
        value = match.group().rstrip(".,;:!?")
        for left, right in [("(", ")"), ("[", "]"), ("{", "}")]:
            while value.endswith(right) and value.count(right) > value.count(left):
                value = value[:-1]
        values.append(value)
    return Counter(values)


def counter_changes(before, after):
    return {
        "removed": dict(sorted((before - after).items())),
        "added": dict(sorted((after - before).items())),
    }


def validate_locks(locks, original):
    if locks is None:
        return []
    if not isinstance(locks, dict):
        raise ValueError("The locks file must contain a JSON object.")
    if set(locks) - {"literals", "quotations"}:
        raise ValueError("Supported lock fields are literals and quotations.")
    spans = []
    for key in ("literals", "quotations"):
        entries = locks.get(key, [])
        if not isinstance(entries, list):
            raise ValueError(f"{key} must be a list of nonempty strings.")
        for span in entries:
            if not isinstance(span, str) or not span.strip():
                raise ValueError(f"{key} must contain only nonempty strings.")
            if span not in original:
                raise ValueError(f"A {key} lock does not occur in the original: {span!r}")
            if span not in spans:
                spans.append(span)
    return spans


def check_preservation(original, revised, locks=None):
    spans = validate_locks(locks, original)
    changed_locks = []
    for span in spans:
        before_count = original.count(span)
        after_count = revised.count(span)
        if before_count != after_count:
            changed_locks.append({
                "text": span,
                "original_occurrences": before_count,
                "revised_occurrences": after_count,
            })
    numbers = counter_changes(numeric_tokens(original), numeric_tokens(revised))
    urls = counter_changes(url_tokens(original), url_tokens(revised))
    needs_review = bool(changed_locks or any(numbers.values()) or any(urls.values()))
    return {
        "status": "review_required" if needs_review else "no_mechanical_differences",
        "changed_locks": changed_locks,
        "numeric_changes": numbers,
        "url_changes": urls,
        "original_text_sha256": sha256_bytes(original.encode("utf-8")),
        "revised_text_sha256": sha256_bytes(revised.encode("utf-8")),
        "limits": [
            "This is a mechanical comparison, not semantic equivalence or fact verification.",
            "Names, units, attribution, uncertainty, conditions, and negation still need contextual review.",
            "Legitimate formatting or wording changes can require manual review.",
        ],
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("original", type=Path)
    parser.add_argument("revised", type=Path)
    parser.add_argument("--locks-file", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        if args.output and args.output.resolve() in {
            path.resolve() for path in (args.original, args.revised, args.locks_file) if path
        }:
            raise ValueError("Output must not overwrite an input or locks file.")
        original_bytes = args.original.read_bytes()
        revised_bytes = args.revised.read_bytes()
        original = original_bytes.decode("utf-8-sig")
        revised = revised_bytes.decode("utf-8-sig")
        locks = json.loads(args.locks_file.read_text(encoding="utf-8-sig")) if args.locks_file else None
        result = check_preservation(original, revised, locks)
        result["original_file_sha256"] = sha256_bytes(original_bytes)
        result["revised_file_sha256"] = sha256_bytes(revised_bytes)
        output = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
        if args.output:
            args.output.write_text(output, encoding="utf-8")
        else:
            print(output, end="")
        return 1 if result["status"] == "review_required" else 0
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"Input error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
