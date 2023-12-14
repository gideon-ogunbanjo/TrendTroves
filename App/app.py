# Libraries
import numpy as np
import streamlit as st
import pickle as pkl
import PIL
import joblib as jbl
import json

st.set_page_config(
    layout = 'centered',
    initial_sidebar_state = 'collapsed',
    page_title = 'TrendTroves'
)

# Loading the model
model_file = 'App/model.pkl'
with open(model_file, 'rb') as file:
    model = pkl.load(file)

# Loading column information
columns_file = 'App/columns.json'
with open(columns_file, 'r') as file:
    columns = json.load(file)['data_columns']
    
# Prediction Function
def predict_price(location, sqft, bath, bedrooms):
    loc_index = np.where(columns == location)[0][0]

    input_data = np.zeros(len(columns))
    input_data[0] = sqft
    input_data[1] = bath
    input_data[2] = bedrooms
    if loc_index >= 0:
        input_data[loc_index] = 1

    return model.predict([input_data])[0]

# Streamlit app
def main():
    st.title('TrendTroves - House Price Prediction Model')

    location = st.selectbox('Select Location', columns[3:])
    sqft = st.slider('Total Square Feet Area', 500, 5000, 1500)
    bath = st.slider('Number of Bathrooms', 1, 5, 2)
    bedrooms = st.slider('Number of Bedrooms', 1, 5, 2)

    if st.button('Predict Price'):
        result = predict_price(location, sqft, bath, bedrooms)
        st.success(f'Predicted Price: ₹{result:.2f} Lakhs')

if __name__ == '__main__':
    main()