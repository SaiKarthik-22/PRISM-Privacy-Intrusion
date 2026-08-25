from src.predictor import analyze


def test_end_to_end_pipeline():
    result = analyze("Please send my PAN ABCDE1234F to user@example.com")
    assert result["intent"] == "SHARING"
    assert result["risk"].score >= 50
    assert "[PAN_MASKED]" in result["masked_text"]
    assert "[EMAIL_MASKED]" in result["masked_text"]
