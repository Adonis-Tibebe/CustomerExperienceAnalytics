import numpy as np
from src.models.keyword_and_topicmodeling import extract_topic_keywords, map_topics_to_labels

class MockLDA:
    def __init__(self):
        self.components_ = np.array([[0.1, 0.9, 0.0], [0.2, 0.3, 0.5]])
    def transform(self, X):
        # Return a fixed topic distribution for two samples
        return np.array([[0.2, 0.8], [0.7, 0.3]])

def test_extract_topic_keywords():
    model = MockLDA()
    feature_names = ["apple", "banana", "cherry"]
    result = extract_topic_keywords(model, feature_names, top_n=2)
    assert "Topic 1" in result and "Topic 2" in result
    assert result["Topic 1"] == ["banana", "apple"]
    assert result["Topic 2"] == ["cherry", "banana"]

def test_map_topics_to_labels():
    lda = MockLDA()
    X = np.zeros((2, 3))
    theme_labels = {0: "Fruit", 1: "Veggie"}
    labels = map_topics_to_labels(lda, X, theme_labels)
    assert labels == [["Veggie", "Fruit"], ["Fruit", "Veggie"]] 