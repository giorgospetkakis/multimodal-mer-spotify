from sklearn import preprocessing
import numpy as np
import pandas as pd
import csv

# Import csv file 
df = pd.read_csv("data/raw/SpotifyData.csv", sep=",")
df = df[["id","artist","title","key","mode","mood","duration_ms","tempo","danceability","energy","loudness","speechiness","acousticness","instrumentalness","liveness","valence"]]
categ = np.array(df.iloc[:,3:5]) 
raw = np.array(df.iloc[:, 5:])

# Standardize data
scaler = preprocessing.StandardScaler()
scaled_df = scaler.fit_transform(raw[:,1:])
scaled_df = np.hstack((categ, scaled_df))
scaled_df = np.hstack((scaled_df, np.zeros((scaled_df.shape[0], 4))))

# Create binary columns
for i, row in enumerate(raw):
    print(row)
    if (row[0] == 'happy'):
        scaled_df[i,-4] = 1
    if (row[0] == 'sad'):
        scaled_df[i,-3] = 1
    if (row[0] == 'angry'):
        scaled_df[i,-2] = 1
    if (row[0] == 'relaxed'):
        scaled_df[i,-1] = 1

# Rename columns and clean up data frame
print(scaled_df)
scaled_df = pd.DataFrame(scaled_df, columns=["key", "mode"] + list(df.columns)[6:] + ["is_happy", "is_sad", "is_angry", "is_relaxed"], index=df["id"])
scaled_df.to_csv('data/preprocessed/spotify-data-preprocessed.csv')