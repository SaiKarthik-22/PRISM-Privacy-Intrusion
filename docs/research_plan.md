# Research Plan

## Baseline

Evaluate PII precision/recall/F1, intent accuracy/F1, risk classification macro-F1 and masking accuracy.

## Learned model

Train a transformer-based multi-task model with shared text representation and two heads:

- token classification for sensitive entities
- sequence classification for privacy intent/risk

## Hybrid improvement

Combine transformer confidence with deterministic rules. High-confidence structured identifiers such as PAN and Aadhaar can receive rule-based overrides, while contextual risk is learned from the transformer.

## Evaluation

Use train/validation/test splits without leakage. Report precision, recall, F1, confusion matrix, calibration and inference latency. Compare the deterministic baseline, transformer-only model and hybrid model.
