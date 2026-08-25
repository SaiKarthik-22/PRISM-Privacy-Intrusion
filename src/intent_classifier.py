"""Rule-based intent classifier used by the baseline model."""


def classify_intent(text: str) -> str:
    t = text.lower()
    if any(k in t for k in ["send", "share", "post", "upload", "forward", "publish"]):
        return "SHARING"
    if any(k in t for k in ["give me", "tell me", "find", "get", "show"]):
        return "REQUESTING"
    if any(k in t for k in ["leak", "stolen", "hack", "breach", "exposed"]):
        return "INCIDENT"
    return "GENERAL"
