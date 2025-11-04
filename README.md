# Crop Yield Prediction using Machine Learning
This project predicts the **crop yield (in tonnes)** based on important factors such as rainfall, pesticide usage, temperature, and year.  
It uses **Machine Learning (Decision Tree Regressor)** to help farmers and researchers estimate how much crop can be produced under given conditions.

## Project Overview
- Built a **machine learning model** to predict crop yield.  
- Used **Flask** to create a simple **web interface** for user input.  
- The user can enter features like:
  - Area  
  - Crop Item  
  - Year  
  - Average Rainfall (mm/year)  
  - Pesticides used (tonnes)  
  - Average Temperature (°C)  
- The model then predicts the **expected crop yield**

## Technologies Used
- Python  
- Pandas, NumPy, Scikit-learn  
- Flask (for web app)  
- HTML, CSS, Bootstrap (for front-end)

## How It Works
1. The user enters crop details on the web form.  
2. Data is preprocessed using the saved preprocessor.  
3. The trained ML model predicts the yield.  
4. The result is displayed on the web page in a clean and friendly way.

5. *If you like this project, don’t forget to give it a star!*
