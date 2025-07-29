# Scripts 

This directory houses utility scripts and SQL files that support data collection, transformation, database setup, and integration for the broader analytics pipeline.


---

## Script: `scrape_google_play_reviews.py`

### Description
Scrapes customer reviews from Google Play for selected banking apps. Results are aggregated and saved to a timestamped CSV for downstream analysis.

---

### `oracle_setup.py`

**Description:**  
Initializes the Oracle database schema required for storing banking app reviews and related metadata.

**Usage:**
```bash
python oracle_setup.py
```

---

### `load_data.py`

**Description:**  
Loads processed and raw review data, as well as bank details, into the Oracle database for downstream analytics.

**Usage:**
```bash
python load_data.py
```

---

### `bank_reviews_schema.sql`

**Description:**  
SQL dump file for manually creating or restoring the Oracle database schema.  
Can be used directly in Oracle SQL tools or referenced by `oracle_setup.py`.

---

### Key Features

- End-to-end automation for collecting, processing, and storing banking app reviews
- Scrapes reviews from Google Play using app identifiers, with customizable language and country parameters
- Structured extraction: review ID, rating, content, date, bank, and source
- Outputs encoded CSVs to support multilingual content
- Robust logging via both console and file handlers for traceability
- Automated Oracle database schema setup and data loading via dedicated scripts
- Includes SQL dump for manual or scripted schema creation
- Modular design for easy extension and integration with the analytics pipeline

## Script Index

- `scrape_google_play_reviews.py` — Scrapes customer reviews from Google Play for selected banking apps.
- `oracle_setup.py` — Sets up and initializes the Oracle database schema for storing reviews and metadata.
- `load_data.py` — Loads processed and raw review data into the Oracle database.
- `bank_reviews_schema.sql` — SQL dump file for manually creating or restoring the Oracle database schema.

### Usage
```bash
python scrape_google_play_reviews.py