import pandas as pd

class Column_Converter:
    """
    Helps santise the recieved data by converting the strings to the data types they are supposed to represent.
    """
    def convert_column_to_float(self, df, columns):
        """
        Converts columns from str to float
        """
        for column in columns: 
            df[column] = pd.to_numeric(df[column].str.replace(',','').str.replace('%',''))
        return df

    def convert_column_to_datetime(self, df, columns):
        """
        Converts entire columns from str to datetime
        """
        for column in columns:
            df[column] = pd.to_datetime(df[column])
        return df

    def format_symbol_column(self, df):
        """
        Removes everything after `.` in Symbol column of scraped table
        """
        symbol_column = df["Symbol"]
        new_symbol_column = []
        for symbol in symbol_column:
            symbol = symbol.split(".")[0]
            new_symbol_column.append(symbol)
        df["Symbol"] = new_symbol_column
        return df

    def revert_scaled_number(self, number):
        """
        Helps convert scale like M: Million to actual numeric values
        """
        mapping = {'M': 1000000, 'B': 1000000000, 'T': 1000000000000}
        scale = number[-1]
        if scale not in ['M','B','T']:
            return float(number.replace(',',''))
        return float(number[0:-1].replace(',','')) * mapping[scale]

    def remove_column(self, column, df=pd.DataFrame()):
        """
        Removes specified column
        """
        # Using Pandas drop() function to drop a column
        df.drop(f"{column}", axis=1, inplace=True)
        return df

if __name__ == '__main__':
    from util.scraper import Scraper
    from config import *
    scr = Scraper()
    cc = Column_Converter()
    table = scr.scrape_table(STOCK_GAINERS_URL)
    print("\nBefore any changes:\n")
    print(table)
    print("\nRemoved 52 week range:\n")
    table = cc.remove_column("52-week range", table)
    print(table)
    print("\nRemoved .NS from symbol column:\n")
    table = cc.format_symbol_column(table)
    print(table)
    
