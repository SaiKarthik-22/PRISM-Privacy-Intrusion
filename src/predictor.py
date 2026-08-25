"""End-to-end baseline prediction pipeline."""

from .preprocessing import normalize_text
from .pii_detector import detect_pii, mask_text
from .intent_classifier import classify_intent
from .risk_engine import calculate_risk


def analyze(text: str) -> dict:
    clean = normalize_text(text)
    findings = detect_pii(clean)
    intent = classify_intent(clean)
    risk = calculate_risk(findings, intent)
    return {
        "text": clean,
        "intent": intent,
        "findings": findings,
        "risk": risk,
        "masked_text": mask_text(clean, findings),
    }
