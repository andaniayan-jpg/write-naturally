# Write Naturally

A Codex skill for revising prose to fit its reader, purpose, and writer. It focuses on clear wording, useful structure, and preservation of claims, evidence, citations, and uncertainty. It does not claim to identify authorship or guarantee an AI detector result.

## Install

Copy this repository's skill files into `~/.codex/skills/write-naturally/`, keeping the `agents`, `references`, and `scripts` folders. Invoke the skill as `$write-naturally` when revising text.

## Use

- Ordinary writing gets a brief editorial pass.
- Substantial rewrites use the pattern and voice references, then compare the result with the source.
- The optional `scripts/check_preservation.py` helper checks numbers, URLs, and protected spans in UTF-8 text files.

The [research record](research/findings.md) describes the comparison used to revise this skill. Its [source catalog](research/all-analyzed-samples.csv) lists 1,200 human-labelled and 1,200 ChatGPT-labelled answer samples from HC3, with metadata and hashes rather than full answer texts. A separate [prior source list](research/prior-writing-sources.csv) contains 269 earlier research records. The research is an editorial comparison, not model training.

## Credits

The skill synthesizes the previous local `write-naturally` and `humanize-writing` skills with ideas from [blader/humanizer](https://github.com/blader/humanizer), [shir-danishyar/humanize](https://github.com/shir-danishyar/humanize), and [milock/humanizer](https://github.com/milock/humanizer). No outside skill text or code was copied.
