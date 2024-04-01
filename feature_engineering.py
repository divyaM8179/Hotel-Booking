from data_cleaning import data_cleaning
import pandas as pd
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler

def feat_eng():
    data = data_cleaning()
    print(data.dtypes)

    print("values--------------", data['booking_status'].value_counts())

    data.to_csv("hotel_reservations.csv", index=False)

    return data

feat_eng()