import pandas as pd

def data_load():
    df = pd.read_csv("Hotel Reservations.csv")

    return df

data_load()
