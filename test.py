import numpy as np
import pandas as pd
import joblib
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder


def process_data(data):

    guest_count = float(data.NumberofGuests)
    quantity = float(data.QuantityofFood)

    wastage_percent = max(((quantity/guest_count)-0.976)*guest_count, 0)

    return wastage_percent


# joblib.dump(process_data, './models/model.joblib')


def prediction():
    # Static values for each variable
    type_of_food = 'Vegetables'
    number_of_guests = 100
    event_type = 'Birthday'
    quantity_of_food = 700
    storage_conditions = 'Refrigerated'
    purchase_history = 'Regular'
    seasonality = 'Summer'
    preparation_method = 'Buffet'
    geographical_location = 'Urban'
    pricing = 'Moderate'

    print(quantity_of_food/number_of_guests)

    # Create a DataFrame with the input data
    input_data = pd.DataFrame({
        'Type of Food': [type_of_food],
        'NumberofGuests': [number_of_guests],
        'Event Type': [event_type],
        'QuantityofFood': [quantity_of_food],
        'Storage Conditions': [storage_conditions],
        'Purchase History': [purchase_history],
        'Seasonality': [seasonality],
        'Preparation Method': [preparation_method],
        'Geographical Location': [geographical_location],
        'Pricing': [pricing]
    })

    # Preprocess the input data
    

    model = joblib.load('./models/model.joblib')

    # # # Make a prediction
    prediction = model(input_data) #model.predict(input_processed)

    # # Format prediction text
    prediction_text = f"Predicted Wastage Food Amount: {prediction:.2f}"
    print(prediction_text)

    # return prediction_text


prediction()