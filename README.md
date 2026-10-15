# HMI Job Summarizer

A human–machine interaction coursework project exploring extractive text summarization in Python. The summarizer scores sentences using word-frequency information and selects the highest-scoring sentences for a short summary.

## How it works

The approach uses NLTK frequency utilities and Python's `heapq.nlargest` to select top-ranked sentences. This is an extractive baseline: it selects sentences from the original text rather than generating new wording.

## Requirements

- Python 3
- NLTK

Install the dependency:

```bash
python -m pip install nltk
```

Depending on the tokenizer and data used by the implementation, NLTK resources may also need to be downloaded before running it.

## Run

Inspect the entry-point script and invoke it with Python, for example:

```bash
python Summarizer.py
```

This is a small academic prototype, not a production summarization service. Future improvements could include input validation, tests for empty or short text, reproducible dependency versions, and a clear command-line interface.