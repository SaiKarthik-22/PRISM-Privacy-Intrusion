from src.pii_detector import detect_pii, mask_text
from src.intent_classifier import classify_intent
from src.risk_engine import calculate_risk


def test_email_detection_and_masking():
    text = "Contact user@example.com today"
    findings = detect_pii(text)
    assert any(f.kind == "EMAIL" for f in findings)
    assert "[EMAIL_MASKED]" in mask_text(text, findings)


def test_pan_detection():
    findings = detect_pii("PAN ABCDE1234F")
    assert any(f.kind == "PAN" for f in findings)


def test_sharing_intent():
    assert classify_intent("send my details to the team") == "SHARING"


def test_high_risk_action():
    findings = detect_pii("send ABCDE1234F to user@example.com")
    result = calculate_risk(findings, "SHARING")
    assert result.score >= 50
    assert result.action in {"WARN_AND_MASK", "BLOCK"}
