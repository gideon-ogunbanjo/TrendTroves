# TrendTroves - House Price Prediction Model
### Overview:
This project implements a machine learning model for predicting house prices based on various features. The model is deployed using a Flask server, allowing users to interact with it through a web interface.

### Technologies Used:
1. Flask: Used as the backend server to host the machine learning model and handle user requests.
2. HTML/CSS/JavaScript: Used for the frontend to create a user-friendly interface for interacting with the model.
3. jQuery: JavaScript library used for simplifying AJAX requests.
4. Scikit-Learn: Python library for machine learning, used to build and train the house price prediction model.

### Project Structure:
- index.html: HTML file for the user interface.
- style.css: CSS file for styling the HTML page.
- server.py: Main Flask application that handles routing and serves the HTML page.
- util.py: Module containing utility functions for loading the machine learning model and making predictions.
- model.pkl: Serialized machine learning model file.
- columns.json: JSON file containing the data columns used by the model.

## Getting Started
### How to Use:
- Fill in the input fields:

- Area (Square Feet): Enter the square footage of the house.
- Bedrooms: Choose the number of bedrooms.
- Bathrooms: Choose the number of bathrooms.
- Location: Select the location from the dropdown.
- Click the "Estimate Price" button to see the predicted house price.

### Creator:
Gideon Ogunbanjo