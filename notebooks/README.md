# Notebooks

This directory hosts structured Jupyter notebooks for various stages of the Google Play Review pipeline. Each notebook is designed to handle a specific task in the overall workflow, including inspection, preprocessing, modeling, and analysis.

## Notebook Index

### `Data_Preprocesing.ipynb`
Introduces core processing steps for raw scraped review data:
- Loads Google Play reviews collected across three major Ethiopian banks
- Applies foundational structural cleaning via `clean_data()` (duplicate and null removal, date parsing)
- Prepares text data for sentiment analysis with `clean_review_text()` through lightweight, BERT-compatible cleaning

This notebook provides the baseline for modeling and thematic exploration tasks that follow.

---

### `Sentiment_and_Thematic_Analysis.ipynb`
Provides a complete workflow for extracting sentiment and thematic insights from Google Play user reviews of Dashen Bank, Commercial Bank of Ethiopia (CBE), and Bank of Abyssinia (BOA) using modern NLP techniques.

- **Setup and Data Loading**: Imports libraries, loads cleaned review data, and previews key columns.
- **Sentiment Analysis**: Loads a pretrained DistilBERT model, applies batch sentiment inference, and summarizes confidence scores for negative reviews.
- **Thematic Analysis Pipeline**:
  - Text preprocessing (lemmatization, stopword removal, emoji stripping, normalization)
  - TF-IDF n-gram extraction (trigrams and four-grams)
  - LDA topic modeling (5 topics per bank)
  - Manual topic labeling and mapping to reviews
- **Theme Mapping**: Assigns top 3 most likely themes to each review and saves results.
- **Data Integration and Export**: Merges annotated DataFrames for all banks and exports the final dataset.
- **Utility and Modularization**: Uses reusable functions and modules for maintainability.
- **Conclusion**: Delivers a robust, modular pipeline for extracting actionable sentiment and thematic insights, ready for business or research analysis.

---

Additional notebooks may be added to this directory as the project progresses, each expanding upon earlier stages and contributing to the full analytical pipeline.