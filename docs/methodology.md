# Methodology

PRISM treats privacy analysis as a multi-stage decision problem rather than a single keyword lookup.

### Stage 1 — Sensitive information
Structured identifiers are detected and assigned severity based on their privacy sensitivity.

### Stage 2 — Context and intent
The system identifies whether the user is sharing, requesting, describing an incident, or making a general statement.

### Stage 3 — Risk fusion
The risk engine combines entity severity and intent. The result is normalized to a 0–100 score and mapped to SAFE, MEDIUM, HIGH or CRITICAL.

### Stage 4 — Action
The system chooses ALLOW, WARN, WARN_AND_MASK or BLOCK and provides explanations.

### Stage 5 — Privacy transformation
Detected identifiers are replaced by type-specific placeholders so the user can safely reuse the text.
