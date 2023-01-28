import pandas as pd
import numpy as np

def cleanData():
  # Import dataset
  columns = ['age', 'sex', 'cp', 'testbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'num']
  df = pd.read_csv('processed.cleveland.data', header=None, names=columns)

  # Clean up the data by throwing out entries with missing 'ca' or 'thal' data
  df = df[df['ca'] != '?']
  df = df[df['thal'] != '?']
  df['ca'] = df['ca'].astype('float64')
  df['thal'] = df['thal'].astype('float64')
  
  return df