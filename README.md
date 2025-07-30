# 🏦 Banking App Review Analytics

## 📌 Business Objective

The goal of this project is to **collect, analyze, and interpret customer reviews** from mobile banking applications to:

- Identify user pain points and feature requests
- Track sentiment trends across banking platforms
- Extract actionable insights for product teams and stakeholders
- Explore ethical AI explainability in financial consumer feedback

These insights empower banks to make data-informed decisions that improve user experience and service quality.

---

## Features

- Automated scraping of Google Play reviews for major Ethiopian banking apps
- Encoded CSV output with standardized fields for analytics
- Structured logging for traceability
- Modular preprocessing pipeline for cleaning and preparing review text
- Sentiment analysis and thematic modeling using modern NLP techniques
- Visual analytics and reporting via Jupyter notebooks
- Oracle database integration for data storage and reporting
- Comprehensive unit tests for core data utilities and modeling functions

---

## Project Structure
project-root/
├── config/
│   └── settings.py
├── data/ 
│   ├── processed/                # Processed datasets
│   └── raw/                     # Raw datasets
│       └── scraped_reviews/     # Output CSVs from scraping jobs and logs             
│           └── scraper.log
├── notebooks/                   # Exploratory and modeling notebooks
│   ├── Data_Preprocessing.ipynb
│   ├── Sentiment_and_Thematic_Analysis.ipynb
│   ├── Insight and Reccomendataion.ipynb
│   └── README.md
├── scripts/                     # Utility scripts for data collection and integration
│   ├── scrape_google_play_reviews.py   # Main script for scraping Google Play reviews
│   ├── load_data.py                    # Script for loading data into databases
│   ├── oracle_setup.py                 # Script for Oracle DB setup
│   └── README.md
├── src/                         # Source code for reusable functions and models
│   ├── utils/                   # Data loading, cleaning, text preprocessing, plotting
│   │   ├── utils.py
│   │   ├── keyword_text_processor.py
│   │   └── plot_utils.py
│   ├── models/                  # Sentiment analysis and topic modeling modules
│   │   ├── sentiments.py
│   │   └── keyword_and_topicmodeling.py
│   ├── core/                    # Core logic and integrations (e.g., oracle_core.py)
│   │   └── oracle_core.py
│   └── services/                # (reserved for future expansion)
├── tests/
│   ├── unit/                    # Unit tests for core utilities and models
│   │   ├── test_utils.py
│   │   ├── test_keyword_text_processor.py
│   │   └── test_keyword_and_topicmodeling.py
│   └── integration/             # (reserved for integration tests)
├── .env
├── requirements.txt
├── pyproject.toml
└── README.md

---

## Getting Started

1. **Clone this repository**
2. **Set up your `.env` file** with:
    - BASE_DATA_DIR=/absolute/path/to/your/data
3. **Install dependencies:**
```bash
pip install -r requirements.txt
```
4. **Run the scraper:**
```bash
python scripts/scrape_google_play_reviews.py
```

**NOTE** - before running the scripts below make sure that you have created the database in oracle and set up the necessary credentials in the .env file

5. **Set up Oracle database and create tables:**
```bash
python scripts/oracle_setup.py
```
6. **Load processed and raw data and bank detail into your database:**
```bash
python scripts/load_data.py
```

---

## 📘 Notebook Workspace

Jupyter notebooks in the `notebooks/` directory guide inspection, cleaning, modeling, and exploratory analysis.

- **Data_Preprocessing.ipynb**: Establishes the foundational steps for processing raw Google Play Store review data across three Ethiopian banks. Loads, inspects, and cleans data for downstream modeling.
- **Sentiment_and_Thematic_Analysis.ipynb**: Provides a complete workflow for extracting sentiment and thematic insights using modern NLP techniques. Includes sentiment scoring, topic modeling, and theme mapping for Dashen Bank, CBE, and BOA.
- **Insight and Reccomendataion.ipynb**: Presents a comprehensive analysis of user reviews for all three banks, synthesizing both sentiment and thematic findings to deliver actionable business insights and recommendations. Includes:
  - Sentiment analysis comparison across banks
  - Thematic breakdowns and top user concerns
  - Actionable recommendations for each bank
  - Visualizations of sentiment trends, rating distributions, keyword clouds, and more

See `notebooks/README.md` for detailed notebook summaries.

---

## 📊 Plotting Utilities

The project includes a suite of reusable plotting functions in `src/utils/plot_utils.py` for visual analytics:
- `plot_sentiment_trends`: Line plot of sentiment scores over time by bank
- `plot_rating_distributions`: Histogram of rating distributions by bank
- `plot_keyword_clouds`: Word clouds of extracted keywords per bank
- `plot_theme_distributions`: Bar plot of theme frequencies by bank
- `plot_sentiment_counts`: Bar plot of sentiment label counts by bank
- `plot_sentiment_variability`: Bar plot of sentiment score variability
- `plot_sentiment_vs_rating`: Scatter plot of sentiment score vs. rating

These functions support the visualizations in the analysis notebooks and can be reused for custom reporting.

---

##  Unit Testing

Unit tests are provided in `tests/unit/` to ensure reliability of core data utilities and modeling functions:
- `test_utils.py`: Tests data loading, cleaning, and review text cleaning functions in `src/utils/utils.py`.
- `test_keyword_text_processor.py`: Tests the keyword preprocessing function in `src/utils/keyword_text_processor.py`.
- `test_keyword_and_topicmodeling.py`: Tests topic extraction and label mapping in `src/models/keyword_and_topicmodeling.py` using mock objects.

Run all tests with:
```bash
pytest tests/unit
```

Continuous integration is set up via GitHub Actions to run these tests automatically on Windows environments.

---

## 📦 Source Modules Overview

- **src/utils/utils.py**: Data loading, cleaning, and lightweight review text cleaning utilities
- **src/utils/keyword_text_processor.py**: Advanced text preprocessing for keyword and topic modeling
- **src/utils/plot_utils.py**: Visualization utilities for sentiment, rating, and theme analysis
- **src/models/sentiments.py**: Loads and applies a pretrained DistilBERT sentiment analysis model
- **src/models/keyword_and_topicmodeling.py**: Topic modeling, keyword extraction, and theme mapping utilities
- **src/core/oracle_core.py**: Oracle database connection and data loading logic

---

## License

This project is provided for educational and research purposes. See LICENSE for details.
