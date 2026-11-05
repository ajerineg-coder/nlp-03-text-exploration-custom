
# Web Mining and Applied NLP | Project 03

**Addie Gemmell**  
Northwest Missouri State University  
November 2026

## Project Overview

For this project, I explored how word frequencies and relationships can help identify patterns in different types of text. I completed a technical modification to the original corpus exploration and then applied the same techniques to fictional financial fraud alert descriptions.

My goal was to see how vocabulary differs between fraud categories and whether text exploration could help identify common terms and patterns.

## Tools and Methods

- Python for text analysis
- Polars for organizing and comparing word frequencies
- Matplotlib for visualizing results
- Tokenization and stop word removal for text preparation
- Context windows for examining word relationships
- Bigrams for identifying frequently occurring word pairs
- Jupyter notebooks for documenting the analysis

## Phase 4: Technical Modification

For Phase 4, I compared context window sizes of 2 and 3 using the original corpus of 22 documents across four categories: dogs, cats, cars, and trucks.

The context window determines how many surrounding words are included when analyzing a target word.

### Results

| Target Word | Window Size 2 | Window Size 3 |
|---|---:|---:|
| Dog | 7 | 9 |
| Cat | 8 | 9 |
| Car | 8 | 11 |
| Truck | 7 | 9 |

Increasing the context window captured more surrounding words for each target. The largest difference was for "car," which increased from 8 to 11 context tokens.

This showed me that increasing the window size provides more context, but the additional words are not necessarily more relevant.

[View Phase 4 Notebook](https://github.com/ajerineg-coder/nlp-03-text-exploration-custom/blob/main/notebooks/phase4_context_window_comparison.ipynb)

## Phase 5: Fraud Text Exploration

For my custom application, I created a fictional dataset of 12 fraud alert descriptions across three categories:

- Check Fraud: 4 documents
- Wire Fraud: 4 documents
- Account Takeover: 4 documents

I chose this topic because I work in financial fraud and wanted to apply text exploration techniques to something relevant to my job.

My main question was: **How does vocabulary differ across common types of financial fraud alerts?**

All descriptions were fictional and did not contain customer information.

### Word Frequency Results

After tokenizing the descriptions, I removed common stop words to make the results more meaningful.

The category comparisons showed:

- Check Fraud: "check" appeared 3 times, followed by "deposited" at 2.
- Wire Fraud: "wire" appeared 4 times, while "customer," "requested," "email," and "fraudulent" appeared twice.
- Account Takeover: "online," "login," and "banking" each appeared twice.

### Co-occurrence and Bigrams

I also examined which words appeared near selected terms using a context window of 2 and calculated bigrams to identify consecutive word pairs.

These techniques provided additional context beyond individual word frequencies. For example, words associated with deposits appeared in the check fraud descriptions, while login and online banking terminology appeared in the account takeover descriptions.

### Visualization

I created three bar charts comparing the five most frequent words in each fraud category. Removing stop words helped highlight terms that were more relevant to each type of fraud.

[View Phase 5 Notebook](https://github.com/ajerineg-coder/nlp-03-text-exploration-custom/blob/main/notebooks/phase5_fraud_text_exploration.ipynb)

## Interpretation and Limitations

The analysis showed how different fraud categories can have distinct vocabulary patterns. I found it interesting that relatively simple text exploration techniques could identify differences between the categories.

However, word frequency alone cannot determine whether fraud actually occurred or explain the full meaning of an alert. The dataset was also small and fictional, so the findings cannot be used to draw conclusions about real fraud activity.

A larger dataset with more detailed text would provide a better opportunity to identify meaningful patterns.

## Project Links

- [GitHub Repository](https://github.com/ajerineg-coder/nlp-03-text-exploration-custom)
- [Original Corpus Exploration Script](https://github.com/ajerineg-coder/nlp-03-text-exploration-custom/blob/main/src/nlp/nlp_corpus_explore.py)
- [Phase 4 Notebook](https://github.com/ajerineg-coder/nlp-03-text-exploration-custom/blob/main/notebooks/phase4_context_window_comparison.ipynb)
- [Phase 5 Notebook](https://github.com/ajerineg-coder/nlp-03-text-exploration-custom/blob/main/notebooks/phase5_fraud_text_exploration.ipynb)

## Project Resources

- [Project Instructions](project-instructions.md)
- [Glossary](glossary.md)
- [Professional Python Guide](https://denisecase.github.io/pro-analytics-02/)
