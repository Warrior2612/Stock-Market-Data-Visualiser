import requests
import pandas as pd
from bs4 import BeautifulSoup

from config import *

class Scraper:
    """
    Scraper Class: It handles the main functionality of scraping data in form of tables from the given url or stock name,
    through its functions scrape_table() and stock_grabber() respectively.
    """
    def __repr__(self):
        """
        Representation of scraper class is defined here.
        The representation is show when an object of the class is printed.
        """
        return "Scraper Class"

    def scrape_table(self, url):
        """
        This function scrapes a table from the given url and returns it as a Pandas DataFrame.
        Beautiful Soup and Requests libraries are used for scraping the table.
        Pandas is used for storing the table as a DataFrame (table).

        Parameters:
        - URL: A String containing url of website to scrape.
        """
        soup = BeautifulSoup(requests.get(url).text, features="html.parser")
        headers = [header.text for listing in soup.find_all('thead') for header in listing.find_all('th')]
        raw_data = {header:[] for header in headers}

        for rows in soup.find_all('tbody'):
            for row in rows.find_all('tr'):
                if len(row) != len(headers): continue
                for idx, cell in enumerate(row.find_all('td')):
                    raw_data[headers[idx]].append(cell.text)

        return pd.DataFrame(raw_data)[:90]

    def stock_grabber(self, stock_name):
        """
        This function accepts the name of desired stock and returns a Pandas DataFrame,
        containing its data in a tabular form.
        It does so by calling another function in its class scrape_table().

        Parameters:
        - Stock Name: A String that contains name of stock whose data is to be retrieved.
        """
        return self.scrape_table(f"https://finance.yahoo.com/quote/{stock_name}.NS/history?p={stock_name}.NS")

if __name__ == '__main__':
    scr = Scraper()
    print("\nMutual Funds:")
    print(scr.scrape_table(MUTUAL_FUNDS_URL))
    print("\nCryptocurrencies:\n")
    print(scr.scrape_table(CRYPTOCURRENCIES_URL))
    print("\nICICIBank last 10 days history:\n")
    print(scr.stock_grabber("ICICIBANK")[:10])