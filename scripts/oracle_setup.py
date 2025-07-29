# scripts/oracle_setup.py

import logging
import oracledb
import os
import sys

sys.path.append(os.path.abspath("../"))
from config.settings import get_db_credentials  

# 🔧 Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s",
    handlers=[logging.StreamHandler()]
)

def create_tables():
    creds = get_db_credentials()  # Grab credentials from .env
    dsn = oracledb.makedsn(creds["host"], creds["port"], service_name=creds["service_name"])

    try:
        # Enable Thin mode implicitly
        with oracledb.connect(user=creds["username"], password=creds["password"], dsn=dsn) as conn:
            cursor = conn.cursor()

            tables = {
                "review_raw": """
                CREATE TABLE BANK_REVIEWS.review_raw (
                    review_id VARCHAR2(100) PRIMARY KEY,
                    review CLOB,
                    rating NUMBER,
                    review_date DATE,
                    bank VARCHAR2(255),
                    source VARCHAR2(100),
                    review_clean CLOB
                )
                """,
                "review_processed": """
                CREATE TABLE BANK_REVIEWS.review_processed (
                    review_id VARCHAR2(100) PRIMARY KEY,
                    review CLOB,
                    rating NUMBER,
                    review_date DATE,
                    bank VARCHAR2(255),
                    source VARCHAR2(100),
                    review_clean CLOB,
                    sentiment_label VARCHAR2(50),
                    sentiment_score FLOAT,
                    keyword_ready CLOB,
                    identified_theme CLOB
                )
                """,
                "bank_detail": """
                CREATE TABLE BANK_REVIEWS.bank_detail (
                    bank_id VARCHAR2(100) PRIMARY KEY,
                    bank_name VARCHAR2(255) NOT NULL,
                    source_of_data VARCHAR2(255),
                    num_reviews INT,
                    avg_rating FLOAT,
                    positive_sentiment_count INT,
                    negative_sentiment_count INT,
                    neutral_sentiment_count INT
                )
                """
            }

            for table_name, ddl in tables.items():
                cursor.execute(f"""
                    SELECT COUNT(*)
                    FROM user_tables
                    WHERE table_name = UPPER('{table_name}')
                """)
                exists = cursor.fetchone()[0] > 0

                if exists:
                    logging.info(f"Table '{table_name}' already exists — skipping creation.")
                else:
                    logging.info(f"Creating table '{table_name}'...")
                    cursor.execute(ddl)
                    logging.info(f"Table '{table_name}' created successfully.")

    except oracledb.Error as e:
        logging.error(f"Oracle error: {e}")
    except Exception as e:
        logging.error(f"General error: {e}")

if __name__ == "__main__":
    create_tables()