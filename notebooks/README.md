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

Additional notebooks may be added to this directory as the project progresses, each expanding upon earlier stages and contributing to the full analytical pipeline.