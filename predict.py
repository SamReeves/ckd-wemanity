#!/usr/bin/env python3

import os
import sys
import pandas as pd
import numpy as np
import sklearn as sk
import joblib

# Load a clean .csv file with 24 independent variables and no target variable
def load_data(data_path):
    df = pd.read_csv(data_path)
    return df

# Load model from a .pkl file
def load_model(model_path):
    model = joblib.load(model_path)
    return model

# Predict target variable from the loaded model and the loaded data
def predict(model, df):
    predictions = model.predict(df)
    return predictions

# Save predictions to a .csv file
def save_predictions(predictions, output_path):
    np.savetxt(output_path, predictions, delimiter=",")
    return

# Main function
def main():
    # Load data
    data_path = sys.argv[1]
    df = load_data(data_path)
    # Load model
    model_path = sys.argv[2]
    model = load_model(model_path)
    # Predict
    predictions = predict(model, df)
    # Save predictions
    output_path = sys.argv[3]
    save_predictions(predictions, output_path)

if __name__ == "__main__":
    main()