import csv
import os
import sys
import logging
from datetime import datetime
from google_play_scraper import reviews, Sort

sys.path.append(os.path.abspath("../"))
from config.settings import get_base_data_dir

# Load base directory from .env
base_dir = get_base_data_dir()

# 📁 Define file path for log
log_path = os.path.join(base_dir, 'scraped_reviews', 'scraper.log')

# Create handlers
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler(log_path, encoding='utf-8')

# Set logging level
console_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.INFO)

# Define formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to root logger
logging.basicConfig(level=logging.INFO, handlers=[console_handler, file_handler])


def scrape_play_store_reviews(app_id, bank_name, count=500, lang='en', country='us'):
    """Fetch reviews for a single banking app."""
    logging.info(f"🔍 Scraping reviews for {bank_name}")
    try:
        result, _ = reviews(
            app_id,
            lang=lang,
            country=country,
            sort=Sort.NEWEST,
            count=count,
            filter_score_with=None
        )

        structured_data = []
        for entry in result:
            structured_data.append({
                'review_id': entry['reviewId'],  # 🆔 Newly added column
                'review': entry['content'],
                'rating': entry['score'],
                'date': entry['at'].strftime('%Y-%m-%d'),
                'bank': bank_name,
                'source': 'Google Play'
            })

        return structured_data

    except Exception as e:
        logging.error(f"❌ Failed scraping for {bank_name}: {e}")
        return []

def main():
    # 🔗 Define bank apps
    bank_apps = {
        'Commercial Bank of Ethiopia (CBE)': 'com.combanketh.mobilebanking',
        'Bank of Abyssinia (BOA)': 'com.boa.boaMobileBanking',
        'Dashen Bank': 'com.dashen.dashensuperapp'
    }

    # 📁 Define save path
    output_dir = 'scraped_reviews'
    main_path = os.path.join(base_dir, output_dir)
    os.makedirs(main_path, exist_ok=True)
    logging.info(f"📂 Output directory: {main_path}")

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_file = os.path.join(main_path, f'all_bank_reviews_{timestamp}.csv')

    # 🧾 CSV Header
    fieldnames = ['review_id', 'review', 'rating', 'date', 'bank', 'source']

    all_reviews = []

    for bank_name, app_id in bank_apps.items():
        bank_reviews = scrape_play_store_reviews(app_id, bank_name)
        logging.info(f"📝 Collected {len(bank_reviews)} reviews for {bank_name}")
        all_reviews.extend(bank_reviews)

    # 🗃️ Write to single CSV
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_reviews)

    logging.info(f"✅ Aggregated {len(all_reviews)} reviews into {output_file}")

if __name__ == '__main__':
    main()