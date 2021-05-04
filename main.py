from util.scraper import Scraper
from util.column_converter import Column_Converter
from util.plot import PlotGraph
from config import *

from termcolor import colored
import time

scr = Scraper()
cc = Column_Converter()

while(True):
    most_active_table = scr.scrape_table(MOST_ACTIVE_STOCKS_URL)
    most_active_table = cc.remove_column("52-week range", most_active_table)
    print("\n")
    print(colored(cc.format_symbol_column(most_active_table), "green"))

    x = input("\n\nPlease enter the stock symbol from the list whose data you wish to visualize or if you wish to quit type in q: ")
    if x == "q":
        exit()
    print(f"\nYou wish to view {x} stock graph!")

    try:
        chosen_stock = scr.stock_grabber(x, most_active_table)
        PlotGraph(chosen_stock)
    except Exception as e:
        print(colored(f"Error: No such stock exists in our database! Please try again", "red"))
        time.sleep(2)