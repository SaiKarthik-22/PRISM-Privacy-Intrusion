# PRISM — Privacy Risk & Intrusion Screening Model 🔐

PRISM is an explainable privacy-analysis system that detects sensitive information, interprets context and intent, estimates privacy risk, explains the decision, and creates a masked version before text is shared.

## Implemented

- Email, phone, Aadhaar-like, PAN-like, UPI-handle and IPv4 detection
- Text preprocessing
- Intent classification: GENERAL, SHARING, REQUESTING, INCIDENT
- Explainable 0–100 privacy-risk scoring
- SAFE / MEDIUM / HIGH / CRITICAL risk levels
- ALLOW / WARN / WARN_AND_MASK / BLOCK decisions
- Automatic privacy-safe masking
- Streamlit web application
- Synthetic starter dataset
- Unit tests and GitHub Actions CI
- TF-IDF + Logistic Regression research baseline
- Optional multi-task transformer architecture for learned intent, risk and entity prediction

## Architecture

```text
User Text → Preprocessing → PII Detection ─┐
                                           ├→ Risk Engine → Decision + Explanation → Mask/Allow/Warn/Block
              └→ Intent Detection ─────────┘
```

## Repository structure

```text
PRISM-Privacy-Intrusion/
├── app.py
├── requirements.txt
├── requirements-ml.txt
├── data/
├── src/
│   ├── preprocessing.py
│   ├── pii_detector.py
│   ├── intent_classifier.py
│   ├── risk_engine.py
│   ├── predictor.py
│   ├── config.py
│   ├── train_baseline.py
│   └── transformer_model.py
├── tests/
├── docs/
└── .github/workflows/ci.yml
```

## Run on Windows

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Run tests

```bash
pytest -q
```

## Run the classical ML baseline

```bash
python -m src.train_baseline
```

## Transformer research phase

Install the optional stack with `pip install -r requirements-ml.txt`. `src/transformer_model.py` defines a shared transformer encoder with three heads: token-level sensitive-entity classification, privacy-intent classification and risk classification. A properly annotated dataset is required before training; the tiny public starter dataset is intentionally not large enough for meaningful transformer training.

## Research direction

Compare: (1) deterministic PRISM baseline, (2) transformer-only model, and (3) hybrid transformer + deterministic rules. Evaluate precision, recall, F1, macro-F1, confusion matrix, calibration and inference latency. See `docs/research_plan.md`.

## Privacy policy for data

Only synthetic examples belong in this public repository. Never commit real personal information. See `data/README.md` and `docs/dataset.md`.

## License

MIT
