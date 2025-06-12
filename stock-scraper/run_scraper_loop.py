import time
from datetime import datetime, timedelta
from stock_scraper import scrape_stock_data, append_to_csv  # assuming you saved the scraper functions in stock_scraper.py

output_file = "data_log.csv"
duration_minutes = 60
interval_seconds = 180  # 3 minutes
end_time = datetime.now() + timedelta(minutes=duration_minutes)

print(f"Starting scraper loop. Will run every 3 minutes for {duration_minutes} minutes.")

while datetime.now() < end_time:
    print(f"\nScraping at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    data = scrape_stock_data()
    append_to_csv(data, output_file)
    print(f"Appended {len(data)} records. Sleeping for 3 minutes...")
    time.sleep(interval_seconds)

print("Scraping session complete.")

