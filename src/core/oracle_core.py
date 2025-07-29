import pandas as pd
import oracledb
import os 
import sys

sys.path.append(os.path.abspath("../../"))
from config.settings import get_db_credentials

def get_oracle_connection():
    creds = get_db_credentials()
    dsn = oracledb.makedsn(creds["host"], creds["port"], service_name=creds["service_name"])
    return oracledb.connect(user=creds["username"], password=creds["password"], dsn=dsn)

def load_review_raw(df):
    with get_oracle_connection() as conn:
        cursor = conn.cursor()
        for _, row in df.iterrows():
            cursor.execute("""
                INSERT INTO BANK_REVIEWS.review_raw (
                    review_id, review, rating, review_date, bank, source, review_clean
                ) VALUES (:1, :2, :3, TO_DATE(:4, 'YYYY-MM-DD'), :5, :6, :7)
            """, (
                row["review_id"], row["review"], row["rating"],
                row["date"], row["bank"], row["source"], row["review_clean"]
            ))
        conn.commit()

def load_review_processed(df):
    with get_oracle_connection() as conn:
        cursor = conn.cursor()
        for _, row in df.iterrows():
            cursor.execute("""
                INSERT INTO BANK_REVIEWS.review_processed (
                    review_id, review, rating, review_date, bank, source, review_clean,
                    sentiment_label, sentiment_score, keyword_ready, identified_theme
                ) VALUES (:1, :2, :3, TO_DATE(:4, 'YYYY-MM-DD'), :5, :6, :7, :8, :9, :10, :11)
            """, (
                row["review_id"], row["review"], row["rating"], row["date"],
                row["bank"], row["source"], row["review_clean"],
                row["sentiment_label"], row["sentiment_score"],
                row["keyword_ready"], row["identified_theme"]
            ))
        conn.commit()

def load_bank_detail(df):
    summary = (
        df.groupby("bank")
        .agg(
            num_reviews=("review_id", "count"),
            avg_rating=("rating", "mean"),
            positive_sentiment_count=("sentiment_label", lambda x: (x == "POSITIVE").sum()),
            negative_sentiment_count=("sentiment_label", lambda x: (x == "NEGATIVE").sum()),
            neutral_sentiment_count=("sentiment_label", lambda x: (x == "NEUTRAL").sum())
        )
        .reset_index()
    )
    summary["bank_id"] = summary["bank"].apply(
        lambda x: "BOA" if "BOA" in x else ("CBE" if "CBE" in x else "Dashen")
        )  # simple ID generation
    summary["source_of_data"] = "Google Play"

    with get_oracle_connection() as conn:
        cursor = conn.cursor()
        for _, row in summary.iterrows():
            cursor.execute("""
                INSERT INTO BANK_REVIEWS.bank_detail (
                    bank_id, bank_name, source_of_data, num_reviews, avg_rating,
                    positive_sentiment_count, negative_sentiment_count, neutral_sentiment_count
                ) VALUES (:1, :2, :3, :4, :5, :6, :7, :8)
            """, (
                row["bank_id"], row["bank"], row["source_of_data"], int(row["num_reviews"]),
                float(row["avg_rating"]), int(row["positive_sentiment_count"]),
                int(row["negative_sentiment_count"]), int(row["neutral_sentiment_count"])
            ))
        conn.commit()