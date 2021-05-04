import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

from util.scraper import Scraper
from util.column_converter import Column_Converter

class PlotGraph:
    def __init__(self, stock):
        self.cc = Column_Converter()
        self.stock = stock
        self.convert_columns()
        self.plot()
    
    def __repr__(self):
        return "Graph Plotter"

    def plot(self):
        fig = go.Figure(data=[go.Candlestick(
                          x=self.stock['Date'],
                          open=self.stock['Open'],
                          high=self.stock['High'],
                          low=self.stock['Low'],
                          close=self.stock['Close*'])],
                        )

        fig.update_layout(
            autosize=True,
            margin=dict(l=20, r=20, t=20, b=20),
            paper_bgcolor="LightSteelBlue",
        )

        fig.show()

    def convert_columns(self):
        self.stock = self.cc.convert_column_to_float(self.stock, self.stock.columns[1:])
        self.stock = self.cc.convert_column_to_datetime(self.stock, [self.stock.columns[0]])

if __name__ == "__main__":
    scr = Scraper()
    apple = scr.scrape_table("https://finance.yahoo.com/quote/AAPL/history?p=AAPL")
    plotter = PlotGraph(apple)