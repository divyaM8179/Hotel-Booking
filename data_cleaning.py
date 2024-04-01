from data_analysis import data_analysis
from sklearn.preprocessing import LabelEncoder

def data_cleaning():
    data = data_analysis()
    label_encoder = LabelEncoder()
    columns_to_encode = ['Booking_ID']
    for col in columns_to_encode:
        data[col] = label_encoder.fit_transform(data[col])

    data['type_of_meal_plan'] = data['type_of_meal_plan'].replace({'Meal Plan 1', 'Not Selected', 'Meal Plan 2', 'Meal Plan 3'}, {0, 1, 2, 3})
    data['room_type_reserved'] = data['room_type_reserved'].replace({'Room_Type 1', 'Room_Type 4', 'Room_Type 6', 'Room_Type 2', 'Room_Type 5', 'Room_Type 7', 'Room_Type 3'}, {0, 1, 2, 3, 4, 5, 6})
    data['market_segment_type'] = data['market_segment_type'].replace({'Online', 'Offline', 'Corporate', 'Complementary', 'Aviation'}, {0, 1, 2, 3, 4})
    data['booking_status'] = data['booking_status'].replace({'Not_Canceled', 'Canceled'}, {0, 1})

    data.drop('Booking_ID', axis=1, inplace=True)

    return data

data_cleaning()