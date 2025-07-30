from src.utils.keyword_text_processor import preprocess_for_keywords

def test_preprocess_for_keywords():
    text = "Wow! This is 100% amazing 😊. Running, runs, ran."
    result = preprocess_for_keywords(text)
    # Should remove digits, punctuation, emojis, stopwords, and lemmatize
    assert "amazing" in result
    assert "run" in result  # lemmatized
    assert "%" not in result
    assert "😊" not in result
    assert "this" not in result  # stopword 