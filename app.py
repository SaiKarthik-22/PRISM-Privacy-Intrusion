"""PRISM Streamlit application."""

import streamlit as st
from src.predictor import analyze

st.set_page_config(page_title="PRISM Privacy Analyzer", page_icon="🔐", layout="wide")
st.title("🔐 PRISM — Privacy Risk & Intrusion Screening Model")
st.caption("Explainable privacy analysis with sensitive-data detection, intent analysis, risk scoring and masking.")

text = st.text_area(
    "Enter text to analyze",
    height=180,
    placeholder="Example: Please send my Aadhaar 1234 5678 9012 to user@example.com",
)

if st.button("Analyze Privacy Risk", type="primary"):
    if not text.strip():
        st.warning("Please enter some text.")
    else:
        result = analyze(text)
        risk = result["risk"]
        c1, c2, c3 = st.columns(3)
        c1.metric("Risk Score", f"{risk.score}/100")
        c2.metric("Risk Level", risk.level)
        c3.metric("Intent", result["intent"])

        st.subheader("Decision")
        st.info(risk.action)

        st.subheader("Detected Sensitive Information")
        if result["findings"]:
            for finding in result["findings"]:
                st.write(f"**{finding.kind}** — `{finding.value}` — severity {finding.severity}/5")
        else:
            st.success("No supported PII pattern detected.")

        st.subheader("Why PRISM made this decision")
        for reason in risk.reasons:
            st.write(f"• {reason}")

        st.subheader("Privacy-safe version")
        st.code(result["masked_text"])

st.divider()
st.caption("Baseline research implementation — add a trained transformer model in the next phase for learned context classification.")
