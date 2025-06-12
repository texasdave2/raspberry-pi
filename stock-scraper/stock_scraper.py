import requests
from bs4 import BeautifulSoup
import csv
from pathlib import Path
from datetime import datetime

endpoint = "gainers"
output_file = "stock_data_log.csv"

def scrape_stock_data():
    response = requests.get(f"https://www.google.com/finance/markets/{endpoint}")
    soup = BeautifulSoup(response.text, "html.parser")
    list_items = soup.find_all("li")
    scraped_data = []

    for item in list_items:
        try:
            divs = item.find_all("div")
            ticker = divs[3].text.strip()
            name = divs[6].text.strip()
            percent_container = item.find("div", class_="NN5r3b")
            percent_divs = percent_container.find_all("div", class_="JwB6zf") if percent_container else []
            percent_gain = percent_divs[0].text.strip().replace('%', '') if percent_divs else None

            if ticker and name and percent_gain:
                scraped_data.append({
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "ticker": ticker,
                    "name": name,
                    "percent_gain": percent_gain
                })

            if len(scraped_data) >= 10:
                break
        except Exception:
            continue

    return scraped_data

def append_to_csv(data, filename):
    file_exists = Path(filename).exists()
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        fieldnames = ["timestamp", "ticker", "name", "percent_gain"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    data = scrape_stock_data()
    append_to_csv(data, output_file)
    print(f"Appended {len(data)} records to {output_file}.")

