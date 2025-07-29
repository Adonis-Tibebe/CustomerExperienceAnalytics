import pandas as pd
import logging
import os
import sys

sys.path.append(os.path.abspath("../"))
from src.core.oracle_core import (
    load_review_raw,
    load_review_processed,
    load_bank_detail
)
from src.utils.utils import load_data, clean_data

logging.basicConfig(level=logging.INFO, format="%(asctime)s — %(levelname)s — %(message)s")

def main():
    raw_csv = "../data/processed/cleaned_reviews.csv"
    processed_csv = "../data/processed/reviews with sentiments and themes.csv"

    # Load review_raw
    df_raw = load_data(raw_csv)
    logging.info("Loading review_raw...")
    load_review_raw(df_raw)

    # Load review_processed
    df_processed = load_data(processed_csv)
    df_processed = clean_data(df_processed)
    logging.info("Loading review_processed...")
    load_review_processed(df_processed)

    # Load bank_detail from processed
    logging.info("Loading bank_detail (derived)...")
    load_bank_detail(df_processed)

    logging.info("✅ Data loading complete.")

if __name__ == "__main__":
    main()