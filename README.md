# PRISM — Privacy Risk & Intrusion Screening Model

PRISM is a text-only privacy analysis system that detects sensitive information, interprets context and intent, estimates privacy risk, explains the decision, and proposes safe masking before text is shared.

## Features

- PII and sensitive-data detection
- Context-aware privacy risk scoring
- Intent classification (normal, sharing, requesting, warning)
- Privacy-risk categories: SAFE, MEDIUM, HIGH, CRITICAL
- Explainable findings
- Automatic masking of detected sensitive data
- Streamlit web application
- Unit tests for core components

## Project flow

```text
User Text
   ↓
Preprocessing
   ↓
PII / Sensitive Data Detection
   ↓
Intent Detection
   ↓
Risk Scoring
   ↓
Explanation
   ↓
Mask / Warn / Allow / Block
```

## Run locally

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Project status

This repository starts with a deterministic baseline that is easy to test and extend. A later research phase can add a supervised NLP/transformer model and compare it with the baseline.
