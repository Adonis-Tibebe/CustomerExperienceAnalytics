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
│   ├── processed/                # Contains processed datasets
│   └── raw/                      # Contains raw datasets
│       └── scraped_reviews/      # Output CSVs from scraping jobs and logs             
│           └── scraper.log
├── notebooks/                    # Exploratory and modeling notebooks
│   ├── Data_Preprocessing.ipynb
│   ├── Sentiment_and_Thematic_Analysis.ipynb
│   └── README.md
├── scripts/                      # Utility scripts for data collection and integration
│   ├── scrape_google_play_reviews.py   # Main script for scraping Google Play reviews
│   ├── load_data.py                    # Script for loading data into databases or other systems
│   ├── oracle_setup.py                 # Script for Oracle DB setup and integration
│   └── README.md
├── src/                          # Source code for reusable functions and models
│   ├── utils/                    # Data loading, cleaning, and text preprocessing utilities
│   ├── models/                   # Sentiment analysis and topic modeling modules
│   ├── core/                     # Core logic and integrations (e.g., oracle_core.py for Oracle DB)
│   └── services/                 # (future expansion)
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

**NOTE** - before running the scripts below make sure that you have created the database in oracle and set up the necessary credentials in the .env file

5. Set up Oracle database and create tables
```bash
python scripts/oracle_setup.py
```
6. Load processed and raw data and bank detail into your database:
```bash
python scripts/load_data.py
```

## 📘 Notebook Workspace

Jupyter notebooks in the `notebooks/` directory guide inspection, cleaning, modeling, and exploratory analysis.

- `Data_Preprocessing.ipynb` initializes the review pipeline by preparing raw data for sentiment analysis.
- `Sentiment_and_Thematic_Analysis.ipynb` performs sentiment scoring and thematic extraction using modern NLP techniques, leveraging modular functions from the `src` directory.

Additional notebooks will be added as analytical tasks expand.

### Components
- `scrape_google_play_reviews.py`: Primary script for collecting structured review data
- `load_data.py`: Script for loading processed data into databases or other systems
- `oracle_setup.py`: Script for setting up and integrating with Oracle databases
- `src/core/oracle_core.py`: Core logic for Oracle DB operations and integration
- `config/settings.py`: Loads base directories from environment or configuration
- `.env`: Stores project-level config variables (e.g., base output paths)
- `notebooks/`: Contains exploratory and task-specific Jupyter notebooks
- `src/utils/`: Reusable utilities for data loading and cleaning

## Recent Changes

- Added `Sentiment_and_Thematic_Analysis.ipynb` for advanced sentiment and thematic analysis.
- Refactored and modularized core functions into the `src/` directory (`utils/`, `models/`).
- Updated `notebooks/README.md` with detailed summaries for each notebook.
- Added `oracle_setup.py` and `load_data.py` scripts for database integration and data loading.
- Added `src/core/oracle_core.py` for Oracle DB operations.
