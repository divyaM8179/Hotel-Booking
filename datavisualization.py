from data_cleaning import data_cleaning
from data_analysis import data_analysis
import pandas as pd
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")
import numpy as np
	@@ -12,72 +14,63 @@
import plotly.graph_objects as go
import io
from PIL import Image

def data_vis():
    data = data_cleaning()
    print(data)

    df=data_analysis()


    top_products = df['type_of_meal_plan'].value_counts().head(10).index.tolist()
    filtered_df = df[df['type_of_meal_plan'].isin(top_products)]

    product_counts = filtered_df['type_of_meal_plan'].value_counts()

    fig = go.Figure(data=[go.Pie(labels=product_counts.index, values=product_counts.values)])

    fig.update_layout(
        template='plotly_dark',
        title='Top 10 Products by Occurrences in Transactions'
    )

    fig.write_image("pie_chart.jpg")  


    dist_df = df['type_of_meal_plan'].value_counts().rename_axis('type_of_meal_plan').reset_index(name='count')
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=dist_df['type_of_meal_plan'],
        y=dist_df['count']
    ))
    fig.update_layout(template="plotly_dark", title="Distribution - Type of meal plan")
    fig.write_image("meal_plan_distribution.jpg")

#-----------------------------

    car_df = df['required_car_parking_space'].value_counts().rename_axis('required_car_parking_space').reset_index(name='count')
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=car_df['required_car_parking_space'],
        y=car_df['count']
    ))
    fig.update_layout(template="plotly_dark", title="Distribution - Required Car Parking Space")
    fig.write_image("Required_Car_Parking_Space.jpg")

#-------------------------------------------

    market_df = df['market_segment_type'].value_counts().rename_axis('market_segment_type').reset_index(name='count')
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=market_df['market_segment_type'],
        y=market_df['count']
    ))
    fig.update_layout(template="plotly_dark", title="Distribution - Market Segment Type")
    fig.write_image("Market_Segment_Type.jpg")


    columns_to_remove = ['arrival_year', 'arrival_month', 'arrival_date', 'no_of_week_nights', 'no_of_weekend_nights', 'no_of_previous_cancellations']
    df=data.drop(columns=columns_to_remove,axis=1)
    y=df.corr().columns.tolist()
    z=df.corr().values.tolist()
    z_text = np.around(z, decimals=4) # Only show rounded value (full value on hover)
    fig = ff.create_annotated_heatmap(z,x=y,y=y,annotation_text=z_text,colorscale=px.colors.sequential.Cividis_r,showscale=True)
    fig.update_layout(template='plotly_dark', width=1000, height=700)
    # fig.show()
    fig.write_image("img.jpg")


    return data

data_vis()
