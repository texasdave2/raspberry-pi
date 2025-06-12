import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

url = "https://finance.yahoo.com/markets/stocks/gainers/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', {'class': 'W(100%)'})
rows = table.find_all('tr')[1:6]  # Top 5 gainers

csv_file = 'top_gainers.csv'
csv_columns = ['Timestamp', 'Symbol', 'Name', 'Price', 'Change', '% Change']

with open(csv_file, 'a', newline='') as file:
    writer = csv.writer(file)
    if file.tell() == 0:
        writer.writerow(csv_columns)

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    for row in rows:
        cols = row.find_all('td')
        writer.writerow([
            timestamp,
            cols[0].text.strip(),
            cols[1].text.strip(),
            cols[2].text.strip(),
            cols[3].text.strip(),
            cols[4].text.strip()
        ])

