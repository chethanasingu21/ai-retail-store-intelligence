import pandas as pd

CSV_PATH = "data/Brigade_Bangalore_10_April_26 (1)bc6219c.csv"

def get_staff_performance():

    df = pd.read_csv(CSV_PATH)

    result = (
        df.groupby("salesperson_name")["GMV"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    return result.to_dict()