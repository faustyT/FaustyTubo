{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "bfdb7b16",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import joblib\n",
    "import numpy as np\n",
    "\n",
    "# Load the saved Random Forest model\n",
    "model = joblib.load(\"random_forest_model.pkl\")\n",
    "\n",
    "# Streamlit app title\n",
    "st.title(\"House Price Prediction App\")\n",
    "st.write(\"This app predicts house prices based on user inputs using a Random Forest model.\")\n",
    "\n",
    "# Sidebar for user input\n",
    "st.sidebar.header(\"Input Features\")\n",
    "\n",
    "def user_input():\n",
    "    # Example input fields based on your dataset features\n",
    "    bedrooms = st.sidebar.number_input(\"Number of Bedrooms\", min_value=1, max_value=10, value=3)\n",
    "    bathrooms = st.sidebar.number_input(\"Number of Bathrooms\", min_value=1.0, max_value=10.0, value=2.0)\n",
    "    sqft_living = st.sidebar.number_input(\"Living Area (sqft)\", min_value=500, max_value=10000, value=1800)\n",
    "    sqft_lot = st.sidebar.number_input(\"Lot Area (sqft)\", min_value=1000, max_value=100000, value=5000)\n",
    "    floors = st.sidebar.number_input(\"Number of Floors\", min_value=1.0, max_value=4.0, value=1.0)\n",
    "    waterfront = st.sidebar.selectbox(\"Waterfront (0 = No, 1 = Yes)\", [0, 1])\n",
    "    grade = st.sidebar.slider(\"Grade\", min_value=1, max_value=13, value=7)\n",
    "    yr_built = st.sidebar.number_input(\"Year Built\", min_value=1900, max_value=2024, value=2000)\n",
    "\n",
    "    # Collecting inputs into a numpy array\n",
    "    features = np.array([[bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, grade, yr_built]])\n",
    "    return features\n",
    "\n",
    "# Get user input\n",
    "input_features = user_input()\n",
    "\n",
    "# Predict button\n",
    "if st.button(\"Predict Price\"):\n",
    "    prediction = model.predict(input_features)\n",
    "    st.subheader(\"Predicted House Price:\")\n",
    "    st.write(f\"${prediction[0]:,.2f}\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
