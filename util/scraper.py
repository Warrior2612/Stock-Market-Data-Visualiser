import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

class Scraper:

    def __init__(self):
        """
        Placeholder
        """
    
    def __repr__(self):
        return "Scraper Class"

    def scrape_table(self, url):
        soup = BeautifulSoup(requests.get(url).text, features="html.parser")
        headers = [header.text for listing in soup.find_all('thead') for header in listing.find_all('th')]
        raw_data = {header:[] for header in headers}

        for rows in soup.find_all('tbody'):
            for row in rows.find_all('tr'):
                if len(row) != len(headers): continue
                for idx, cell in enumerate(row.find_all('td')):
                    raw_data[headers[idx]].append(cell.text)

        return pd.DataFrame(raw_data)[:90]

    def stock_grabber(self, stock_name, df=pd.DataFrame()):
        # if f"{stock_name}.NS" in df["Symbol"].values:
        return self.scrape_table(f"https://finance.yahoo.com/quote/{stock_name}.NS/history?p={stock_name}.NS")
        # else:
            # raise Exception("No such stock name exists in our list! Please try again")