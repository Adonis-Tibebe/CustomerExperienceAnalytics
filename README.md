# 🏦 Banking App Review Analytics

## 📌 Business Objective

The goal of this project is to **collect, analyze, and interpret customer reviews** from mobile banking applications to:

-  Identify user pain points and feature requests
-  Track sentiment trends across banking platforms
-  Extract insights for product teams and stakeholders
-  Explore ethical AI explainability in financial consumer feedback

Ultimately, these insights will empower banks to make data-informed decisions that improve user experience and service quality.

---

## Implementation Overview

### ✅ Current Capabilities
- Automated scraping of Google Play reviews for key Ethiopian banking apps
- Encoded CSV output with standardized fields for downstream analytics
- Structured logging via both file and console for traceability
- Modular preprocessing pipeline for cleaning and preparing review text

### Initial Components
- `scrape_google_play_reviews.py`: Primary script for collecting structured review data
- `config/settings.py`: Loads base directories from environment or configuration
- `.env`: Stores project-level config variables (e.g., base output paths)
- `notebooks/`: Contains exploratory and task-specific Jupyter notebooks
- `src/utils/`: Reusable utilities for data loading and cleaning


More scripts and modules (e.g. NLP, dashboards, calendar converters) will be added incrementally as we expand.

---

## Project Structure
project-root/
├── config/
│   └── settings.py
├── data/ 
|   ├──processed                # contains processed datasets
|   └──raw                      # containes raw datasets
|       └──scraped_reviews/           # Output CSVs from scraping jobs and loggs             
│           └── scraper.log
├── notebooks/                 # Exploratory and modeling notebooks
│   ├── Data_Preprocessing.ipynb      # Initial cleaning and structuring of raw reviews
│   ├── Sentiment_and_Thematic_Analysis.ipynb  # Sentiment scoring and thematic extraction using NLP
│   └── README.md                     # Notebook index and summaries
├── src/                      # Source code for reusable functions and models
│   ├── utils/                # Data loading, cleaning, and text preprocessing utilities
│   ├── models/               # Sentiment analysis and topic modeling modules
│   ├── services/               # (future expansion)
|   └──core/                    # (future expansion)
├── .env
├── requirements.txt
└── README.md


---

##  Getting Started

1. Clone this repository
2. Set up your `.env` file with:
    - BASE_DATA_DIR=/absolute/path/to/your/data
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. run the scrapper:
```bash
python scripts/scrape_google_play_reviews.py
```

## 📘 Notebook Workspace

Jupyter notebooks in the `notebooks/` directory guide inspection, cleaning, modeling, and exploratory analysis.

- `Data_Preprocessing.ipynb` initializes the review pipeline by preparing raw data for sentiment analysis.
- `Sentiment_and_Thematic_Analysis.ipynb` performs sentiment scoring and thematic extraction using modern NLP techniques, leveraging modular functions from the `src` directory.

Additional notebooks will be added as analytical tasks expand.

## Recent Changes

- Added `Sentiment_and_Thematic_Analysis.ipynb` for advanced sentiment and thematic analysis.
- Refactored and modularized core functions into the `src/` directory (`utils/`, `models/`).
- Updated `notebooks/README.md` with detailed summaries for each notebook.