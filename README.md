
# nlp-03-text-exploration-custom

[![Python 3.14](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](pyproject.toml)
[![CI](https://github.com/ajerineg-coder/nlp-03-text-exploration-custom/actions/workflows/ci-python-zensical.yml/badge.svg)](https://github.com/ajerineg-coder/nlp-03-text-exploration-custom/actions/workflows/ci-python-zensical.yml)
[![Documentation](https://img.shields.io/badge/docs-site-blue?logo=github)](https://ajerineg-coder.github.io/nlp-03-text-exploration-custom/)
[![uv managed](https://img.shields.io/badge/uv-managed-DE5FE9)](https://docs.astral.sh/uv/)
[![ty type checked](https://img.shields.io/badge/ty-type_checked-2F80ED)](https://docs.astral.sh/ty/)
[![Zensical docs](https://img.shields.io/badge/Zensical-docs-purple)](https://zensical.org/)
[![MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

> Explore vocabulary patterns in fictional financial fraud alerts using token frequencies, category comparisons, co-occurrence, and bigrams.

## Project Overview

**Author:** Addie Gemmell  
**Date:** November 2026  
**Course:** Web Mining and Applied NLP  
**Project:** 03 - Text Exploration

This project explores how natural language processing (NLP) techniques can identify vocabulary patterns across different categories of text.

For my custom application, I chose to analyze fictional financial fraud alerts and case descriptions. I wanted to see how the wording differs between fraud categories and whether commonly used words and word combinations could help identify patterns.

The project uses Python, Polars, and Matplotlib to examine token frequencies, word co-occurrence, bigrams, and category differences.

## Data

I created a small corpus of 12 fictional fraud alert descriptions organized into three categories:

- **Check Fraud:** 4 descriptions involving counterfeit checks, altered checks, stolen checks, and suspicious deposits.
- **Wire Fraud:** 4 descriptions involving fraudulent wire instructions, suspicious beneficiaries, and payment requests.
- **Account Takeover:** 4 descriptions involving unauthorized logins, password resets, and suspicious online banking activity.

Each document contains a category label and a short text description.

All descriptions are fictional and were created for this assignment. No actual customer information or confidential banking data was used.

## Approach

The project follows the exploratory text analysis process demonstrated in the original example.

The analysis includes:

- Creating a labeled corpus of text documents.
- Tokenizing and cleaning text by converting words to lowercase, removing punctuation, and filtering common stop words.
- Calculating global token frequencies.
- Comparing token frequencies across categories.
- Identifying the most frequently used words in each category.
- Examining word co-occurrence using context windows.
- Creating and counting bigrams.
- Visualizing vocabulary differences.
- Interpreting the results and identifying limitations.

These techniques help identify patterns in text before applying machine learning or more advanced NLP models.

## Phase 4: Technical Modification

For the technical modification, I compared context window sizes of 2 and 3 tokens using the original example corpus.

A context window determines how many words before and after a target word are considered when examining co-occurrence.

Increasing the window size allows more surrounding words to be included in the analysis.

The comparison showed that larger context windows generally produced more co-occurring word relationships because additional nearby words were included.

The results were visualized using a bar chart comparing the two window sizes across the original categories.

[View Phase 4 Context Window Comparison Notebook](notebooks/phase4_context_window_comparison.ipynb)

## Phase 5: Custom Fraud Text Exploration

For my custom project, I applied the same exploratory analysis techniques to the 12 fictional fraud descriptions.

The analysis compares vocabulary across check fraud, wire fraud, and account takeover.

### Global and Category Token Frequencies

Token frequencies show which words appear most often throughout the corpus and within individual fraud categories.

The results showed differences in the vocabulary associated with each category.

- **Check Fraud:** Frequently included words such as "check" and "deposited."
- **Wire Fraud:** Frequently included words such as "wire," "requested," and "fraudulent."
- **Account Takeover:** Included terms such as "login," "online," and "banking."

These differences reflect the types of activities described in each category.

### Co-occurrence and Bigrams

Co-occurrence analysis identifies words that appear near one another within a specified context window.

Bigrams identify pairs of consecutive words.

These methods provide more information about how words are used together rather than looking only at individual word counts.

For fraud analysis, these relationships may help distinguish language associated with different types of suspicious activity.

### Visualization

I created a visualization comparing the most frequently used words across all three fraud categories.

The charts make it easier to see differences in vocabulary and identify terms that appear more frequently within specific categories.

[View Phase 5 Fraud Text Exploration Notebook](notebooks/phase5_fraud_text_exploration.ipynb)

## Interpretation and Limitations

The results demonstrate that different types of fraud descriptions can have recognizable vocabulary patterns.

For example, check fraud descriptions focus on checks and deposits, while wire fraud descriptions emphasize transfers and payment requests. Account takeover descriptions contain more references to login activity and online banking.

These findings show how basic NLP techniques could be useful when exploring larger collections of fraud alerts or case notes.

However, this project uses only 12 fictional descriptions. The results are not representative of actual fraud activity, and word frequencies alone cannot determine whether a transaction or account activity is fraudulent.

Additional data, context, and more advanced analysis would be necessary before applying these techniques to real-world fraud detection.

## Project Files

- [pyproject.toml](pyproject.toml) - Project configuration and dependencies.
- [src/nlp/nlp_corpus_explore.py](src/nlp/nlp_corpus_explore.py) - Custom fraud corpus analysis script.
- [notebooks/phase4_context_window_comparison.ipynb](notebooks/phase4_context_window_comparison.ipynb) - Technical modification comparing context windows.
- [notebooks/phase5_fraud_text_exploration.ipynb](notebooks/phase5_fraud_text_exploration.ipynb) - Custom fraud text exploration.
- [tests/](tests/) - Automated tests.
- [docs/](docs/) - Project report and documentation.
- [zensical.toml](zensical.toml) - Documentation configuration.

## Run the Project

Follow the [Professional Python Workflow Guide](https://denisecase.github.io/pro-analytics-02/) to set up your machine and project environment.

From a VS Code terminal in the project root, run:

```shell
uv sync
uv run python -m nlp.nlp_corpus_explore
```

Close the visualization window after viewing the chart so the script can finish executing.

The analysis displays token frequencies, category comparisons, co-occurrence information, bigram frequencies, and visualizations.

A successful execution displays:

```text
Pipeline executed successfully!
```

## Verification

Run the following commands to check formatting, code quality, and automated tests:

```shell
uv run ruff check .
uv run ruff format --check .
uv run python -m pytest
```

These checks help verify that the project runs correctly and follows the expected Python coding standards.

## Project Documentation

The project documentation includes the analytical question, corpus description, technical modification, results, visualizations, interpretation, and limitations.

- [GitHub Repository](https://github.com/ajerineg-coder/nlp-03-text-exploration-custom)
- [Project Documentation](https://ajerineg-coder.github.io/nlp-03-text-exploration-custom/)
- [Project Report](docs/index.md)
- [Phase 4 Notebook](notebooks/phase4_context_window_comparison.ipynb)
- [Phase 5 Notebook](notebooks/phase5_fraud_text_exploration.ipynb)

The documentation is configured for publication using Zensical and GitHub Pages.

## CI/CD and GitHub Actions

This project includes continuous integration and continuous deployment (CI/CD) workflows for checking code quality and publishing documentation.

- [CI: Python and Documentation Checks](https://github.com/ajerineg-coder/nlp-03-text-exploration-custom/actions/workflows/ci-python-zensical.yml)
- [CD: Documentation Deployment](https://github.com/ajerineg-coder/nlp-03-text-exploration-custom/actions/workflows/deploy-zensical.yml)

## Developer Reference

Follow the [Professional Python Workflow Guide](https://denisecase.github.io/pro-analytics-02/) for detailed instructions and troubleshooting.

### Initialize and Update the Python Environment

From the VS Code terminal:

```shell
uvx pup-clean --delete
uv self update
uv python pin 3.14
uv python install
uv lock --upgrade
uv sync
uv audit
```

### Set Up and Run Git Hooks

Git hooks help check project files before changes are committed and pushed.

```shell
uvx prek install --force
uvx prek update --freeze --cooldown-days 7

git add -A
uvx prek run --all-files
uvx prek run --all-files
```

### Run Common Chores

Run code quality checks, automated tests, and documentation builds:

```shell
uv run ruff check . --fix
uv run ruff format .
uv run ty check
uv run python -m pytest
uv run python -m zensical build
```

### Git Add-Commit-Push to GitHub

After making changes, save the work to GitHub:

```shell
git add -A
git commit -m "Complete custom fraud text exploration"
git push -u origin main
```

## Developer Notes

- Use the **UP ARROW** and **DOWN ARROW** in the terminal to scroll through previous commands.
- Use **Command + F** on macOS to search within a file.
- Use **Command + S** to save changes in VS Code.
- Run verification checks before committing and pushing changes.

## Developer Tools

This project uses the following tools:

- [uv](https://docs.astral.sh/uv/) - Python environments and dependencies.
- [Ruff](https://docs.astral.sh/ruff/) - Python linting and formatting.
- [ty](https://docs.astral.sh/ty/) - Python type checking.
- [pytest](https://docs.pytest.org/) - Automated Python testing.
- [prek](https://prek.j178.dev/) - Git hooks and automated checks.
- [Zensical](https://zensical.org/) - Project documentation.

## Links

- [GitHub Repository](https://github.com/ajerineg-coder/nlp-03-text-exploration-custom)
- [Hosted Documentation](https://ajerineg-coder.github.io/nlp-03-text-exploration-custom/)
- [Professional Python Workflow Guide](https://denisecase.github.io/pro-analytics-02/)
- [Citation](CITATION.cff)
- [License](LICENSE)
