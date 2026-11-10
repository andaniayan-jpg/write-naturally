# Writing comparison and source record

Research completed 10 November 2026. This work updates a writing skill; it does not train or fine-tune a language model.

## What was examined

The comparison used **1,200 paired questions** from the English [HC3 corpus](https://huggingface.co/datasets/Hello-SimpleAI/HC3). For each question, the first available human answer and first ChatGPT answer were selected. The result was **1,200 human-labelled answers and 1,200 AI-labelled answers**. All selected answers contained 40 to 1,500 words. A fixed random seed selected 700 pairs from `reddit_eli5`, 400 from `wiki_csai` and 100 from `open_qa` after filtering. Exact file hashes, selection rules and counts are in [manifest.json](manifest.json).

[All 2,400 analyzed text records](all-analyzed-samples.csv) lists the dataset subset, source file, one-based JSONL line, answer index, source link, text hash, word count and measured features for each answer. The full answer texts are not redistributed. A separate [prior research source list](prior-writing-sources.csv) contains 269 earlier discovery records on writing craft, linguistics and authorship research. Those records were not counted among the 2,400 analyzed answers, and access levels vary.

These are **answer samples**, not 2,400 independent articles, books or original domains. HC3 supplies labels, but the original URLs of individual human answers are not present in the downloaded JSONL files. The source links in the CSV lead to the dataset row that holds each answer. The human label is not independent proof that no AI assistance occurred. The AI side represents the dataset's ChatGPT outputs, not every current model. The [official project](https://github.com/Hello-SimpleAI/chatgpt-comparison-detection) describes the source categories and notes that stricter source licenses may apply. The index therefore contains metadata and hashes rather than copied answers.

## Observed differences in this sample

| Measure | Human-labelled | ChatGPT-labelled | Reading |
| --- | ---: | ---: | --- |
| Median words per answer | 121 | 178 | The ChatGPT answers were longer in this selection. |
| Generic opening detected | 4 / 1,200 | 36 / 1,200 | A generic opening is a useful review cue when it delays the answer. |
| Formulaic closing detected | 12 / 1,200 | 126 / 1,200 | Repeated closing summaries deserve review, especially when they add no result. |
| Mean overlap between question terms and first 30 answer words | 0.080 | 0.122 | The AI answers more often repeated question terms early, by this simple measure. |
| First-person wording | 327 / 1,200 | 214 / 1,200 | First person is common in the human-labelled ELI5 subset; it is not an AI sign. |
| `may`, `might`, `could`, `perhaps` or `possibly` | 348 / 1,200 | 519 / 1,200 | The difference was largely in ELI5; in `wiki_csai` the counts were 118 and 120. Do not ban hedges. |

The opening and closing patterns were simple regular-expression checks. Question overlap was a Jaccard comparison of non-stopword terms, not a measure of factual quality or originality. These numbers describe the selected HC3 answers only. The Reddit human answers include tokenization artifacts, and the three subsets have different purposes and answer lengths. Small counts for numbered lists and bullets did not support a broad formatting rule.

Reading matched examples added a useful qualitative check. Some human-labelled answers supplied a concrete example or the requested name immediately. Some ChatGPT answers began with a definition or a general account before reaching the specific answer. That observation motivated a **reader-first review question** in the skill, not a ban on definitions. A definition can be exactly what the reader needs.

## How the skill changed

The updated entrypoint now has a short route for ordinary writing and a deeper route for substantial revisions. It asks the editor to identify the reader's actual need, keep the author's evidence and stance, revise repeated structure at paragraph scale, and then compare the result with the source. Its optional pattern reference contains review cues and false-positive cautions. A voice sample is used only when the user supplies one or an authorized project profile exists. The skill does not claim that a list of words or a detector score can establish authorship.

Ideas were synthesized from the existing `write-naturally` and `humanize-writing` skills and three MIT-licensed GitHub skills. [blader/humanizer](https://github.com/blader/humanizer) informed the review of staged contrasts, repetitive endings and wrong-reader framing. [shir-danishyar/humanize](https://github.com/shir-danishyar/humanize) informed the separation of drafting and rewrite modes and the caution that pattern checks cannot judge meaning. [milock/humanizer](https://github.com/milock/humanizer) informed the use of actual voice samples and an auditable final pass. No outside skill text or code was copied into the new skill.

## Limits

This is a matched comparison of one public dataset, not a universal taxonomy of human and AI writing. The sample's original prompts, source communities, tokenization and 2023 ChatGPT model all affect the measured patterns. A different genre or model may reverse a feature. The updated skill uses the findings as prompts for editing decisions and preserves facts, citations, uncertainty and the requested register. It cannot guarantee a detector result or certify that a draft was written by a human.
