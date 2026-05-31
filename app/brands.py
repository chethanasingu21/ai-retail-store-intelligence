import pandas as pd

CSV_PATH = "data/Brigade_Bangalore_10_April_26 (1)bc6219c.csv"

def get_top_brands():

    df = pd.read_csv(CSV_PATH)

    result = (
        df.groupby("brand_name")["GMV"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    return result.to_dict()