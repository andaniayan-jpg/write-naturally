# Research basis, limits, and credits

The skill was informed by a paired analysis of 1,200 human-labelled and 1,200 ChatGPT-labelled answers in [HC3 English](https://huggingface.co/datasets/Hello-SimpleAI/HC3), using 700 `reddit_eli5`, 400 `wiki_csai` and 100 `open_qa` pairs. A separate source catalog of 269 writing and research pages informed the earlier version. The new comparison treated every answer as data; it did not fine-tune a model. The complete sample index, file hashes, selection rules and counts were delivered with the research report rather than loaded into this skill at runtime.

In the matched sample, the ChatGPT answers were longer at the median, 178 versus 121 words. Simple checks found a generic opening in 36 AI-labelled answers versus 4 human-labelled answers, and a formulaic closing in 126 versus 12. The AI answers repeated more question terms in their first 30 words by a basic overlap measure. These findings support checking whether a paragraph delays the answer or repeats it. They do **not** justify deleting all definitions, conclusions, or repeated terms.

First person appeared in 327 human-labelled answers and 214 AI-labelled answers, mostly because of the conversational Reddit subset. A hedge check differed in Reddit but was nearly equal in the technical `wiki_csai` subset. First person, hedges, passive voice, formal grammar, and any single punctuation mark are not reliable origin tests. The dataset's 2023 ChatGPT responses, answer genres, source tokenization, and uncertain individual human provenance limit generalization.

The instructions also synthesize ideas from the existing local `write-naturally` and `humanize-writing` skills and these MIT-licensed GitHub skills:

- [blader/humanizer](https://github.com/blader/humanizer), for paragraph-scale staging, repetitive endings, and reader mismatch.
- [shir-danishyar/humanize](https://github.com/shir-danishyar/humanize), for separating writing and rewrite modes, preservation checks, and treating mechanical lint as a prompt rather than a verdict.
- [milock/humanizer](https://github.com/milock/humanizer), for evidence-based voice calibration and a final review pass.

The updated skill paraphrases and combines these ideas. It does not reproduce their code or instruction text. An observed pattern can guide an edit only when the edit improves this particular piece while preserving its meaning and voice. No pattern set can certify human authorship or promise a detector outcome.
