import numpy as np
import json
import os

def extract_topic_keywords(model, feature_names, top_n=10):
    topic_dict = {}
    for topic_idx, topic in enumerate(model.components_):
        top_keywords = [feature_names[i] for i in topic.argsort()[:-top_n - 1:-1]]
        topic_dict[f"Topic {topic_idx + 1}"] = top_keywords
    return topic_dict

def map_topics_to_labels(lda_model, tfidf_matrix, theme_labels):
    topic_distributions = lda_model.transform(tfidf_matrix)
    top_labels = []
    for dist in topic_distributions:
        if np.all(dist == 0):
            continue
        idxs = dist.argsort()[-3:][::-1]
        top_labels.append([theme_labels[i] for i in idxs])
    print("✅ Topics mapped to labels")
    return top_labels

def save_topics_with_labels(bank, topic_keywords, theme_labels, save_path):
    """
    Combines topic keywords with manually assigned labels and saves to JSON.
    
    Args:
        bank: name of the bank to be processed
        topic_keywords: dict with topic_id as keys and list of keywords.
        theme_labels: dict with topic_id as keys and readable labels.
        save_path: directory to save the JSON file.
    """
    labeled_topics = {
        f"Topic {i+1}": {
            "label": theme_labels[i],
            "keywords": topic_keywords[f"Topic {i+1}"]
        }
        for i in range(len(theme_labels))
    }
    os.makedirs(save_path, exist_ok=True)
    file_path = os.path.join(save_path, f"{bank}_theme_map.json")
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(labeled_topics, f, indent=4, ensure_ascii=False)
    print(f"✅ Saved to: {file_path}")