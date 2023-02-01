import pandas as pd
import numpy as np

class HeartDisease:
  def __init__(self):
    # Import dataset
    columns = ['age', 'sex', 'cp', 'testbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'num']
    self.df = pd.read_csv('processed.cleveland.data', header=None, names=columns)

  def fullData(self):
    return self.df
    
  def throwMissing(self):
    # Clean up the data by throwing out entries with missing 'ca' or 'thal' data
    throwdf = self.df
    throwdf = throwdf[throwdf['ca'] != '?']
    throwdf = throwdf[throwdf['thal'] != '?']
    throwdf['ca'] = throwdf['ca'].astype('float64')
    throwdf['thal'] = throwdf['thal'].astype('float64')
    return throwdf
  
  def modeMissing(self):
    # Clean up the data by replacing missing 'ca' and 'thal' data with their modes
    modedf = self.df
    modedf.ca.replace('?', modedf.ca.mode()[0], inplace=True)
    modedf.thal.replace('?', modedf.thal.mode()[0], inplace=True)
    modedf['ca'] = modedf['ca'].astype('float64')
    modedf['thal'] = modedf['thal'].astype('float64')
    return modedf

  def reduceSick(df):
    # Reduce sick values to one value (1) for simplicity 
    df['num'] = df['num'].replace(2, 1)
    df['num'] = df['num'].replace(3, 1)
    df['num'] = df['num'].replace(4, 1)
    return df

  def scaleFeatures(x):
    # Scale features using standard scaler
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x)
    return x_scaled