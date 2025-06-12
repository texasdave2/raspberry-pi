import time
import sys
import select
from datetime import datetime, timedelta
from stock_scraper import scrape_stock_data, append_to_csv

output_file = "data_log.csv"
duration_minutes = 60
interval_seconds = 180  # 3 minutes
end_time = datetime.now() + timedelta(minutes=duration_minutes)

print("Starting scraper loop. Press 'q' then Enter at any time to quit.")

def check_for_quit():
    # Check if there's input ready (non-blocking)
    if select.select([sys.stdin], [], [], 0)[0]:
        user_input = sys.stdin.readline().strip()
        if user_input.lower() == 'q':
            return True
    return False

while datetime.now() < end_time:
    if check_for_quit():
        print("Quit command received. Exiting loop.")
        break

    print(f"\nScraping at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    data = scrape_stock_data()
    append_to_csv(data, output_file)
    print(f"Appended {len(data)} records. Sleeping for 3 minutes... (press 'q' + Enter to quit)")

    for _ in range(interval_seconds):
        if check_for_quit():
            print("Quit command received during sleep. Exiting loop.")
            exit()
        time.sleep(1)

print("Scraping session complete.")

