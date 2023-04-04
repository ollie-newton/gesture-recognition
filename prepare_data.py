from pathlib import Path
import pandas as pd
from create_windows import overlapping_windows
from visualise_data import line_plot
from create_feature import time_features
from normalise import normalise


#create a filepath to the original df
MATCH_DATA_FILEPATH = Path(__file__).parent.joinpath('data', 'data_1.csv')
cols = ['raw extension','env ext', 'raw flex', 'env flex']
#read df to variable with columns used in csv file
df = pd.read_csv(MATCH_DATA_FILEPATH, usecols=cols)
df['ENV'] = df['env ext'] + df['env flex']
windows = overlapping_windows(df,200,100)

#line_plot(df.iloc[5000:,:])

#create a filepath to the original df
MATCH_DATA_FILEPATH = Path(__file__).parent.joinpath('data', 'labels_1_rps.csv')
cols = ['Label']
#read df to variable with columns used in csv file
feature_df = pd.read_csv(MATCH_DATA_FILEPATH, usecols=cols)

print(windows)

features = time_features(windows, feature_df)


print(features)

norm_features = normalise(features)

print(norm_features)

norm_features.to_csv('features.csv', index=False)

