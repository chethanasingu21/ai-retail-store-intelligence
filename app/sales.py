import pandas as pd

CSV_PATH = "data/Brigade_Bangalore_10_April_26 (1)bc6219c.csv"

def get_sales_metrics():

    df = pd.read_csv(CSV_PATH)

    buyers = len(df)

    revenue = float(df["GMV"].sum())

    return {
        "buyers": buyers,
        "revenue": revenue
    }