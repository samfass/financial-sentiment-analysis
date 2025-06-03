import pynance as pn

def fetch_stock_data(symbol, start_date, end_date):
    """
    Fetch historical stock data using PyNance.

    Parameters:
        symbol (str): Stock ticker (e.g., 'AAPL')
        start_date (str): Start date in 'YYYY-MM-DD'
        end_date (str): End date in 'YYYY-MM-DD'

    Returns:
        DataFrame: Historical stock data
    """
    try:
        data = pn.data.get(symbol, start=start_date, end=end_date)
        return data
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

if __name__ == "__main__":
    print(fetch_stock_data("AAPL", "2022-01-01", "2022-12-31"))
