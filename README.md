# ckd-wemanity
Chronic Kidney Disease Binary Classification

This project was emailed to me as an initial screening test for Wemanity Group.

***

## Assignment

"You must generate an application that can be used across biomedical data science projects.  The dataset used for the proof of concept can help physicians better understand chronic kidney disease (CKD) using numerous measurements and biomarkers that have been collected.

You have been tasked to write modularised reusable code that other similar datasets and
similar projects can use to help a physician understand 1. risk factors for CKD and 2. potential CKD subtypes."

Interestingly, there is no indication to train a prediction model or produce predictions.

The first part will take a look at what factors are seemingly always significant or never significant in positive cases.  The second will attempt to show positive cases in at least two common groups.

## Data Set

https://archive.ics.uci.edu/ml/datasets/Chronic_Kidney_Disease#

This data set was made public in 2015, the result of a study done in Tamilnadu, India.  It contains 24 independent variables -- features of a patient's blood -- which we can use to indicate the dependent variable "class".  Class is a binary value which indicates that a patient does or does not have Chronic Kidney Disease.  There are 400 independent observations.

This data contains null values, and it does not have standardized data types.  It is provided for free by University of California Irvine (whoo! go Anteaters!) in a .rar archive, with all relevant information in .arff.


## Usage Instructions

Start with the following, from the root directory:

    source venv/bin/activate
    pip install -r requirements.txt

### if CKD_clean.csv is present

Enjoy analysis.ipynb

### if CKD_clean.csv is not present

Make sure you also have installed a .rar archive extractor like rar,unrar,7z.

Assuming your data is also in the same 22:1 format in a .arff and compressed in .rar, this code should run fine.

Run the preprocessing.ipynb notebook and examine any errors. Then, continue with analysis.ipynb.

### Predictions

You can generate a new predictor model with predictions.ipynb
Open the notebook, read the comments, and run both blocks.

To make predictions from a .csv file (already run through the preprocessing notebook), but with the target column removed,
just run the following:

    python3 predict.py dummy.csv model.pkl dummy_predictions.csv

argments are filenames input.csv, model.pkl, output.csv

## Files

 * Chronic_Kidney_Disease.rar -- Initial data set download
 * preprocessing.ipynb -- Jupyter notebook for cleaning and exploring data
 * analysis.ipynb -- Jupyter notebook containing analytical information
 * LICENSE -- Software license, go ahead and use it
 * arffToCsv.py -- File converter from github user haloboy777
 * predictions.ipynb -- Jupyter notebook for generating a prediction model
 * model.pkl -- Python pickle of Naive Bayes Classifier
 * predict.py -- Script that classifies people with or without CKD