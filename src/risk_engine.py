"""Explainable privacy risk scoring for PRISM."""

from dataclasses import dataclass
from typing import List
from .pii_detector import Finding


@dataclass(frozen=True)
class RiskResult:
    score: int
    level: str
    action: str
    reasons: List[str]


def calculate_risk(findings: List[Finding], intent: str) -> RiskResult:
    score = 0
    reasons = []
    if findings:
        score += min(60, sum(f.severity * 8 for f in findings))
        reasons.append(f"Detected {len(findings)} sensitive data item(s).")
        kinds = ", ".join(sorted({f.kind for f in findings}))
        reasons.append(f"Sensitive types: {kinds}.")
    if intent == "SHARING":
        score += 25
        reasons.append("The text indicates an intention to share or publish information.")
    elif intent == "REQUESTING":
        score += 10
        reasons.append("The text requests potentially sensitive information.")
    elif intent == "INCIDENT":
        score += 20
        reasons.append("The text suggests a privacy/security incident.")

    score = min(100, score)
    if score >= 75:
        level, action = "CRITICAL", "BLOCK"
    elif score >= 50:
        level, action = "HIGH", "WARN_AND_MASK"
    elif score >= 25:
        level, action = "MEDIUM", "WARN"
    else:
        level, action = "SAFE", "ALLOW"
    if not reasons:
        reasons.append("No high-risk privacy indicators were detected.")
    return RiskResult(score, level, action, reasons)
