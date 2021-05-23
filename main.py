from termcolor import colored
import time

# Importing Self-Created Local Modules
from util.scraper import Scraper
from util.column_converter import Column_Converter
from util.plot import PlotGraph
from config import MOST_ACTIVE_STOCKS_URL

# Initializing objects of Scraper and Column_Converter classes
scr = Scraper()
cc = Column_Converter()

# An infinite loop to execute testing code that ends only when user enters their choice to exit program
while(True):
    # Scraping the table of most active stocks from the url MOST_ACTIVE_STOCKS_URL imported from config.py,
    # by using scrape_table() function of Scraper class
    most_active_table = scr.scrape_table(MOST_ACTIVE_STOCKS_URL)
    # Removing the unwanted columns from table
    most_active_table = cc.remove_column("52-week range", most_active_table)
    # Printing a colored and well formatted version of recieved table
    print("\n")
    print(colored(cc.format_symbol_column(most_active_table), "green"))

    # Taking user choice regarding the stock whose data they wish to visualize or if they wish to exit
    choice = input("\n\nPlease enter the stock symbol from the list whose data you wish to visualize or if you wish to quit type in q: ")
    if choice == "q" or choice == "Q":
        print(colored("\nThank you for using our program! Please Come Again!", "magenta"))
        exit()
    print(colored(f"\nYou wish to view {choice} stock graph!", "blue"))

    # Try and Except block to check if stock exists and try to plot graph based on its data
    try:
        chosen_stock = scr.stock_grabber(choice, most_active_table)
        plt = PlotGraph(chosen_stock)
    except Exception as e:
        # Raising an error in case of any error and waiting 2 secs before giving user choice again
        print(colored(f"Error: No such stock exists in our database! Please try again", "red"))
        time.sleep(2)