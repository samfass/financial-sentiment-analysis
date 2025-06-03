import yfinance as yf
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def download_stock_data(ticker, start_date, end_date):
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        if data.empty:
            logging.warning(f"No data for {ticker} between {start_date} and {end_date}")
            return None
        return data
    except Exception as e:
        logging.error(f"Download failed for {ticker}: {e}")
        return None
