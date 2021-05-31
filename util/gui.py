from tkinter import *
from pandastable import Table

from util.scraper import Scraper
from util.plot import PlotGraph

scr = Scraper()

CHOICE=""

class StockApp(Frame):
        """Basic test frame for the table"""

        def __init__(self, df, parent=None):
            self.parent = parent
            self.df = df
            Frame.__init__(self)
            self.main = self.master
            self.main.geometry('')
            self.main.title('Stock Market Data Visualizer')
            f = Frame(self.main)
            f.pack(fill=BOTH,expand=1)
            self.table = pt = Table(f, dataframe=df,
                                    showtoolbar=True, showstatusbar=True)
            self.table.autoResizeColumns()
            self.color_table()
            self.table.redraw()
            bp = Frame(self.main)
            bp.pack(side=TOP)
            textBox=Text(bp, height = 5, width = 20)
            textBox.pack(side=LEFT,fill=BOTH,)
            self.textBox = textBox;
            b=Button(bp,text='View Graph', command=lambda: self.gui_to_plot(textBox.get("1.0",'end-1c')))
            b.pack(side=LEFT,fill=BOTH,)
            q=Button(bp, text="Quit", command=quit)
            q.pack()
            pt.show()
            return

        def gui_to_plot(self, input):
            self.textBox.delete("1.0",'end')
            CHOICE = input.strip();
            try:
                chosen_stock = scr.stock_grabber(CHOICE)
                PlotGraph(chosen_stock)
            except Exception as e:
                pass

        def quit(self):
            self.main.destroy()
            exit()

        def color_table(self):
            j = 0
            k = 0
            change_column = list(self.df['% change'])

            for i in range(len(change_column)):
                if float(change_column[j].replace('%','')) < float(change_column[i].replace('%','')):
                    j = i
                if float(change_column[k].replace('%','')) > float(change_column[i].replace('%','')):
                    k = i

            self.table.setRowColors(rows=range(50), clr='#d1ffff', cols='all')
            self.table.setRowColors(rows=[j], clr='#00FF00', cols='all')
            self.table.setRowColors(rows=[k], clr='#FF0000', cols='all')
            self.table.columncolors['Symbol'] = '#03cffc'


def call_gui(df):
    app = StockApp(df)
    app.mainloop()