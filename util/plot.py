import pandas as pd
import plotly.graph_objects as go

# Importing Self-Created Local Modules
from util.scraper import Scraper
from util.column_converter import Column_Converter

class PlotGraph:
    """
    PlotGraph Class: This class contains functions that help plot a candlestick style graph for the financial data
    that is passed to it in the form of a Pandas DataFrame.

    Parameters:
    - Stock: Pandas DataFrame that contains the history of the past 90 days of a particular stock.
    """
    def __init__(self, stock):
        # Initializing objects of classes that are to be used in the PlotGraph class
        self.cc = Column_Converter()
        self.stock = stock
        
        # Calling the necessary functions in correct order to eliminate need for calling functions manually
        # This enables us to directly call the class and see the results
        self.convert_columns()
        self.plot()
    
    def __repr__(self):
        """
        Representation of PlotGraph class is defined here.
        The representation is show when an object of the class is printed.
        """
        return "Graph Plotter"

    def plot(self):
        """
        The main function of the PlotGraph class.
        It initializes a figure using the plotly.graph_objects library and then adds the supplied data to the figure
        in the form of a candlestick graph plot.

        **Not meant to be used as a standalone function but is called when an object of the PlotGraph class is created**
        """

        # Initializing the figure
        fig = go.Figure(data=[go.Candlestick(
                          x=self.stock['Date'],
                          open=self.stock['Open'],
                          high=self.stock['High'],
                          low=self.stock['Low'],
                          close=self.stock['Close*'])],
                        )

        # Customizing the layout the figure with parameters like size, margin and background color
        fig.update_layout(
            autosize=True,
            margin=dict(l=20, r=20, t=20, b=20),
            paper_bgcolor="LightSteelBlue",
        )

        # Displaying the figure
        fig.show()

    def convert_columns(self):
        """
        This function contains calls to the column_converter local module using the cc object of class Column_Converter, 
        which has been initialized in the class __init__() function.
        """
        # Converting columns that are supposed to be numeric to float values
        self.stock = self.cc.convert_column_to_float(self.stock, self.stock.columns[1:])
        # Converting the column which represents date and time to actual date time format
        self.stock = self.cc.convert_column_to_datetime(self.stock, [self.stock.columns[0]])

if __name__ == "__main__":
    """
    Testing Code.
    Executed only when this file is directly executed.
    """
    # Creating instance of Scraper Class
    scr = Scraper()
    # Scraping data of Apple Stock using scrape_table() function from Scraper Class
    apple = scr.scrape_table("https://finance.yahoo.com/quote/AAPL/history?p=AAPL")
    # Plotting the data of apple stock using PlotGraph Class
    plotter = PlotGraph(apple)