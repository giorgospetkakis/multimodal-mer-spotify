from sklearn import preprocessing
import numpy as np
import pandas as pd
import csv

# Import csv file 
df = pd.read_csv("data/raw/SpotifyData.csv", sep=",")
raw = np.array(df.iloc[:,3:])

# Standardize data
scaler = preprocessing.StandardScaler()
scaled_df = scaler.fit_transform(raw[:,1:])
scaled_df = np.hstack((scaled_df, np.zeros((scaled_df.shape[0], 4))))

# Create binary columns
for i, row in enumerate(raw):
    if (row[0] == 'happy'):
        scaled_df[i,-4] = 1
    if (row[0] == 'sad'):
        scaled_df[i,-3] = 1
    if (row[0] == 'angry'):
        scaled_df[i,-2] = 1
    if (row[0] == 'relaxed'):
        scaled_df[i,-1] = 1

# Rename columns and clean up data frame
scaled_df = pd.DataFrame(scaled_df, columns=list(df.columns)[4:] + ["is_happy", "is_sad", "is_angry", "is_relaxed"])
scaled_df.to_csv('data/preprocessed/spotify-data-preprocessed.csv')