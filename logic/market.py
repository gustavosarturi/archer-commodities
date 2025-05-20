import pandas as pd

def load_prices(path="data/prices.csv"):
    df = pd.read_csv(path, parse_dates=["date"])
    return df.sort_values("date")
