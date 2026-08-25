"""Deterministic PII detector for the PRISM baseline."""

import re
from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Finding:
    kind: str
    value: str
    start: int
    end: int
    severity: int


PATTERNS = {
    "EMAIL": (re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I), 3),
    "PHONE": (re.compile(r"(?<!\d)(?:\+?91[- .]?)?[6-9]\d{9}(?!\d)"), 3),
    "AADHAAR": (re.compile(r"(?<!\d)\d{4}[ -]?\d{4}[ -]?\d{4}(?!\d)"), 5),
    "PAN": (re.compile(r"\b[A-Z]{5}\d{4}[A-Z]\b", re.I), 5),
    "UPI": (re.compile(r"\b[a-zA-Z0-9._-]{2,}@[a-zA-Z]{2,}\b"), 4),
    "IP_ADDRESS": (re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"), 2),
}


def detect_pii(text: str) -> List[Finding]:
    findings: List[Finding] = []
    for kind, (pattern, severity) in PATTERNS.items():
        for match in pattern.finditer(text):
            findings.append(Finding(kind, match.group(), match.start(), match.end(), severity))
    findings.sort(key=lambda x: (x.start, -(x.end - x.start)))

    # Remove overlapping detections, retaining the higher-severity finding.
    selected: List[Finding] = []
    for item in sorted(findings, key=lambda x: (-x.severity, x.start, x.end)):
        if not any(item.start < x.end and x.start < item.end for x in selected):
            selected.append(item)
    return sorted(selected, key=lambda x: x.start)


def mask_text(text: str, findings: List[Finding]) -> str:
    output = text
    for finding in sorted(findings, key=lambda x: x.start, reverse=True):
        replacement = f"[{finding.kind}_MASKED]"
        output = output[:finding.start] + replacement + output[finding.end:]
    return output
