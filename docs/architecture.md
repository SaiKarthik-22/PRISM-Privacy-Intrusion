# PRISM Architecture

## Pipeline

1. **Preprocessing** — normalize whitespace and input text.
2. **PII detection** — identify email, phone, Aadhaar, PAN, UPI and IP address patterns.
3. **Intent detection** — classify the text into GENERAL, SHARING, REQUESTING or INCIDENT.
4. **Risk engine** — combine sensitive-data severity and intent into a 0–100 risk score.
5. **Decision layer** — ALLOW, WARN, WARN_AND_MASK or BLOCK.
6. **Explanation** — return human-readable reasons.
7. **Masking** — replace detected values with safe placeholders.

## Research extension

The baseline is intentionally deterministic. The next model can use a transformer encoder with a classification head for intent/risk classification and a token-classification head for learned PII detection. A hybrid ensemble can combine learned probabilities with high-precision deterministic rules.
