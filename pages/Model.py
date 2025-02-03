import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
import joblib
from keras.src.legacy.saving import legacy_h5_format


st.set_page_config(layout="centered")

# Load the trained model
model = model = legacy_h5_format.load_model_from_hdf5('./trained_model.h5',custom_objects={'mae':'mae'})

# Define the categorical columns and missing value placeholder
categorical_cols = ['Purchase Type', 'Payment Method', 'Railcard', 'Ticket Class', 'Ticket Type', 
                    'Departure Station', 'Arrival Destination', 'Journey Status', 
                    'Reason for Delay', 'Refund Request']
missing_value_placeholder = 'Missing'

# Unique values for each column
purchase_type_options = ['Online', 'Station']
payment_method_options = ['Contactless', 'Credit Card', 'Debit Card']
ticket_type_options = ['Advance', 'Off-Peak', 'Anytime']
ticket_class_options = ['Standard', 'First Class']
railcard_options = ['Adult', 'Disabled', 'Senior','Missing']
departure_station_options = ['London Paddington', 'London Kings Cross', 'Liverpool Lime Street',
                             'London Euston', 'York', 'Manchester Piccadilly', 'Birmingham New Street',
                             'London St Pancras', 'Oxford', 'Reading', 'Edinburgh Waverley', 'Bristol Temple Meads']
arrival_destination_options = ['Liverpool Lime Street', 'York', 'Manchester Piccadilly', 'Reading',
                               'London Euston', 'Oxford', 'Durham', 'London St Pancras', 'Birmingham New Street',
                               'London Paddington', 'Bristol Temple Meads', 'Tamworth', 'London Waterloo',
                               'Sheffield', 'Wolverhampton', 'Leeds', 'Stafford', 'Doncaster', 'Swindon', 'Nottingham',
                               'Peterborough', 'Edinburgh', 'Crewe', 'London Kings Cross', 'Leicester', 'Nuneaton',
                               'Didcot', 'Edinburgh Waverley', 'Coventry', 'Wakefield', 'Cardiff Central', 'Warrington']
journey_status_options = ['On Time', 'Delayed', 'Cancelled']
reason_for_delay_options = ['Signal Failure', 'Technical Issue', 'Weather Conditions', 'Weather', 'Staffing',
                            'Staff Shortage', 'Signal failure', 'Traffic','Missing']
refund_request_options = ['No', 'Yes']

# Function to handle missing values in categorical columns
def handle_missing_values(df, categorical_cols, placeholder='Missing'):
    for col in categorical_cols:
        df[col] = df[col].fillna(placeholder)
    return df



# Load the trained label encoders
label_encoders = joblib.load("./label_encoders.pkl")
# Function to safely fit and transform categorical columns (use label encoders that were saved with the model)
def safe_label_encoder(df, categorical_cols, label_encoders):
    for col in categorical_cols:
        if col in label_encoders:
            df[col] = df[col].fillna(missing_value_placeholder)
            df[col] = label_encoders[col].transform(df[col].astype(str))
    return df


st.title("Inference Model with Embedding + Regression Model")

st.markdown("""
### Data Preprocessing Steps:
1. **Handle Missing Values**: For categorical columns, missing values are replaced with a placeholder (e.g., 'Missing').
2. **Label Encoding**: Each unique category in a column is encoded as an integer value. This allows us to feed categorical variables into the model.
3. **Model**: The model uses embedding layers for categorical columns and dense layers for regression.

### Model Inference:
You can input data below to get a prediction from the trained model.
""")

# User input for inference using dropdowns
st.subheader("Input Data for Inference")

# Input fields for the user to enter data (using dropdowns)
purchase_type = st.selectbox("Purchase Type", purchase_type_options)
payment_method = st.selectbox("Payment Method", payment_method_options)
railcard = st.selectbox("Railcard", railcard_options)
ticket_class = st.selectbox("Ticket Class", ticket_class_options)
ticket_type = st.selectbox("Ticket Type", ticket_type_options)
departure_station = st.selectbox("Departure Station", departure_station_options)
arrival_destination = st.selectbox("Arrival Destination", arrival_destination_options)
journey_status = st.selectbox("Journey Status", journey_status_options)
reason_for_delay = st.selectbox("Reason for Delay", reason_for_delay_options)
refund_request = st.selectbox("Refund Request", refund_request_options)

# Prepare the input data for the model
new_data = pd.DataFrame({
    'Purchase Type': [purchase_type],
    'Payment Method': [payment_method],
    'Railcard': [railcard],
    'Ticket Class': [ticket_class],
    'Ticket Type': [ticket_type],
    'Departure Station': [departure_station],
    'Arrival Destination': [arrival_destination],
    'Journey Status': [journey_status],
    'Reason for Delay': [reason_for_delay],
    'Refund Request': [refund_request]
})

# Handle missing values and apply label encoding
new_data = handle_missing_values(new_data, categorical_cols, placeholder=missing_value_placeholder)
# Apply the loaded label encoders to the input data
new_data = safe_label_encoder(new_data, categorical_cols, label_encoders)


# Button to trigger prediction
predict_button = st.button("Predict")

if predict_button:

    # Prepare input data for the model
    input_data = [new_data[col].values for col in new_data.columns]
    
    # Prediction using the loaded model
    prediction = model.predict(input_data)

    # Show the final prediction value
    st.subheader("Predicted Price")
    st.write(f"The predicted price for this ticket is: {prediction[0][0]:.2f}")
