import os
import pandas as pd
import tempfile
import pytest
from src.utils.utils import load_data, clean_data, clean_review_text

def test_load_data(tmp_path):
    # Create a small CSV
    csv_path = tmp_path / "test.csv"
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    df.to_csv(csv_path, index=False)
    loaded = load_data(str(csv_path))
    assert loaded.equals(df)

def test_clean_data():
    df = pd.DataFrame({
        "a": [1, 1, 2, None],
        "b": [3, 3, 4, 5],
        "date": ["2020-01-01", "2020-01-01", "2020-01-02", "2020-01-03"]
    })
    cleaned = clean_data(df, date_columns=["date"])
    # Should drop duplicate and null
    assert cleaned.shape[0] == 2
    assert pd.api.types.is_datetime64_any_dtype(cleaned["date"])

def test_clean_review_text():
    text = "<b>Hello</b> visit http://test.com @user!"
    cleaned = clean_review_text(text)
    assert "<b>" not in cleaned
    assert "http" not in cleaned
    assert "@user" not in cleaned
    assert "Hello" in cleaned 