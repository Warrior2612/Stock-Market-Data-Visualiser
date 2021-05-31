# Importing Self-Created Local Modules
from util.scraper import Scraper
from util.column_converter import Column_Converter
from util.plot import PlotGraph
from util.gui import call_gui
from config import MOST_ACTIVE_STOCKS_URL_50

# Initializing objects of Scraper and Column_Converter classes
scr = Scraper()
cc = Column_Converter()

# An infinite loop to execute testing code that ends only when user enters their choice to exit program
while(True):
    # Scraping the table of most active stocks from the url MOST_ACTIVE_STOCKS_URL imported from config.py,
    # by using scrape_table() function of Scraper class
    most_active_table = scr.scrape_table(MOST_ACTIVE_STOCKS_URL_50)
    # Removing the unwanted columns from table
    most_active_table = cc.remove_column("52-week range", most_active_table)
    most_active_table = cc.format_symbol_column(most_active_table)
    call_gui(most_active_table)