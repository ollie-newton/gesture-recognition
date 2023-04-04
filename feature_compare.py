from pathlib import Path
import pandas as pd
import numpy as np
import plotly.express as px
from visualise_data import line_plot

#create a filepath to the original df
MATCH_DATA_FILEPATH = Path(__file__).parent.joinpath('freqRPSfeature.csv')
cols = ['Ext Mean',	'Flex Mean',	'Ext Var',	'Flex Var', 'Ext Freq 2','Flex Freq 2','Gesture']
#read df to variable with columns used in csv file
df_feature = pd.read_csv(MATCH_DATA_FILEPATH, usecols=cols)

df_feature['Gesture'] = df_feature['Gesture'].replace('P', 'Paper')
df_feature['Gesture'] = df_feature['Gesture'].replace('R', 'Rock')
df_feature['Gesture'] = df_feature['Gesture'].replace('S', 'Scissors')

df_feature['Ext Freq 2'] = df_feature['Ext Freq 2'] * 100
df_feature['Flex Freq 2'] = df_feature['Flex Freq 2'] * 100


print(df_feature)

fig = px.scatter(df_feature, x = "Ext Freq 2", y="Flex Freq 2", color="Gesture")
#fig.update_layout(xaxis_range=[0.5, None], yaxis_range=[0.5, None])

fig.show()