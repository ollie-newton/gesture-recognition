from pathlib import Path
import pandas as pd
from create_windows import overlapping_windows
from visualise_data import line_plot


#create a filepath to the original df
MATCH_DATA_FILEPATH = Path(__file__).parent.joinpath('data', 'data_1.csv')
cols = ['raw extension','env ext', 'raw flex', 'env flex']
#read df to variable with columns used in csv file
df = pd.read_csv(MATCH_DATA_FILEPATH, usecols=cols)
df['ENV'] = df['env ext'] + df['env flex']
windows = overlapping_windows(df,200,100)

line_plot(df)

