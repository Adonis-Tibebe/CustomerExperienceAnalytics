# Notebooks

This directory hosts structured Jupyter notebooks for all stages of the Google Play Review analytics pipeline. Each notebook is designed to handle a specific task in the overall workflow, including inspection, preprocessing, modeling, and analysis.

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

### `Insight and Reccomendataion.ipynb`
Presents a comprehensive analysis of user reviews for Dashen Bank, Commercial Bank of Ethiopia (CBE), and Bank of Abyssinia (BOA), synthesizing both sentiment and thematic findings to deliver actionable business insights and recommendations.

- **Sentiment Analysis**:
  - Dashen Bank leads with the highest average sentiment score and consistent user satisfaction, reflecting strong emotional resonance and trust.
  - CBE follows with generally positive feedback but greater variability, indicating some friction points.
  - BOA has the lowest sentiment scores and a predominance of negative reviews, highlighting significant user dissatisfaction.

- **Theme Analysis**:
  - Dashen is praised for seamless transactions and reliability, with minor issues around OTP and loading.
  - BOA faces criticism for app crashes, usability, and trust, with nostalgia for previous versions.
  - CBE is commended for ease of use and international access, but users request more features and better update transparency.

- **Recommendations**:
  - Dashen Bank: Leverage its “Super App” reputation with UX showcases and new features; address OTP/login issues; expand financial tools.
  - BOA: Prioritize app stability and performance improvements; reintroduce the app with clear communication about updates; enhance onboarding and feedback mechanisms.
  - CBE: Improve update delivery and transparency; address security and customization requests, especially for international users.

- **Visual Insights**: Includes visualizations of sentiment trends, rating distributions, keyword clouds, theme frequencies, and the relationship between sentiment and ratings, providing a holistic view of user experience and perception.

This notebook delivers a conclusive synthesis of the analytical pipeline, translating data-driven findings into practical recommendations for product and business strategy.

---

Additional notebooks may be added to this directory as the project evolves, each expanding upon earlier stages and contributing to the full analytical pipeline.