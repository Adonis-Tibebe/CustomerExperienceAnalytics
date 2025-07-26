# Scripts 

This directory houses utility scripts that support data collection, transformation, and integration for the broader analytics pipeline.

---

## Current Script: `scrape_google_play_reviews.py`

### Description
Scrapes customer reviews from Google Play for selected banking apps. Results are aggregated and saved to a timestamped CSV for downstream analysis.

### Key Features
-  Targets apps via their Google Play identifiers
-  Customizable language and country parameters
-  Structured extraction with review ID, rating, content, date, and source
-  Encoded CSV output to support multilingual content
-  Robust logging via both console and file handlers

### Usage
```bash
python scrape_google_play_reviews.py