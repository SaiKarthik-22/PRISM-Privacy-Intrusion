"""Train/evaluate a simple TF-IDF baseline on the synthetic dataset.

This is a reproducible research baseline, not the final transformer model.
"""

from pathlib import Path
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "privacy_dataset.csv"


def main():
    df = pd.read_csv(DATA)
    x_train, x_test, y_train, y_test = train_test_split(
        df["text"], df["risk_label"], test_size=0.25, random_state=42, stratify=df["risk_label"]
    )
    vectorizer = TfidfVectorizer(ngram_range=(1, 2), lowercase=True)
    X_train = vectorizer.fit_transform(x_train)
    X_test = vectorizer.transform(x_test)
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print(classification_report(y_test, pred, zero_division=0))


if __name__ == "__main__":
    main()
