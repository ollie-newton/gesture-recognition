from pathlib import Path
import pandas as pd
import numpy as np
import plotly.express as px
from visualise_data import line_plot

#create a filepath to the original df
MATCH_DATA_FILEPATH = Path(__file__).parent.joinpath('data', 'raw_data.csv')
cols = ['Ext Raw',	'Ext Env',	'Flex Raw',	'Flex Env']
#read df to variable with columns used in csv file
df_raw = pd.read_csv(MATCH_DATA_FILEPATH, usecols=cols)

print(df_raw)

fig = px.line(df_raw, y='Ext Env')

fig.show()