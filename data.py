import yfinance as yf
import numpy as np
import pandas as pd

TICKER = "SPY"
START  = "2021-01-01"
END    = "2027-01-01"


def download_spy(ticker=TICKER, start=START, end=END) -> pd.Series:
    """
    Download SPY daily closing prices, returned as a Series.
    """
    raw = yf.download(ticker, start=start, end=end, auto_adjust=True)["Close"]
    if isinstance(raw, pd.DataFrame):
        raw = raw.iloc[:, 0]
    raw = raw.dropna()
    raw.name = "SPY"
    return raw


