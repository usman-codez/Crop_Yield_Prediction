from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import pickle

# Load model and preprocessor
dt = pickle.load(open('dt.pkl', 'rb'))
preprocessor = pickle.load(open('prepro.pkl', 'rb'))

# Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        Area = request.form['Area']
        Item = request.form['Item']
        Year = request.form['Year']
        average_rain_fall_mm_per_year = request.form['average_rain_fall_mm_per_year']
        pesticides_tonnes = request.form['pesticides_tonnes']
        avg_temp = request.form['avg_temp']

        # Create dataframe from input
        features_df = pd.DataFrame([[Area, Item, Year, average_rain_fall_mm_per_year, pesticides_tonnes, avg_temp]],
                                   columns=['Area', 'Item', 'Year', 'average_rain_fall_mm_per_year','pesticides_tonnes', 'avg_temp'])
        # Transform input
        transformed_features = preprocessor.transform(features_df)
        # Predict
        predicted_value = dt.predict(transformed_features)

        #Make prediction output clean and appealing
        predicted_value = float(predicted_value[0])
        predicted_value = round(predicted_value, 2)
        return render_template('index.html', predicted_value=predicted_value)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
