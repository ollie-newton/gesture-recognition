from pathlib import Path
import pandas as pd
import numpy as np
from visualise_data import line_plot

#create a filepath to the original df
MATCH_DATA_FILEPATH = Path(__file__).parent.joinpath('data', 'RPS_freq1.csv')
cols = ['Ext Mean',	'Flex Mean',	'Ext Var',	'Flex Var', 'Ext Freq 2','Flex Freq 2','Ext Freq 1','Flex Freq 1','Gesture']
#read df to variable with columns used in csv file
df_feature = pd.read_csv(MATCH_DATA_FILEPATH, usecols=cols)



# MATCH_DATA_FILEPATH = Path(__file__).parent.joinpath('data', 'LABEL2.csv')
# cols = ['Label']
# #read df to variable with columns used in csv file
# df_label = pd.read_csv(MATCH_DATA_FILEPATH, usecols=cols)

df_feature['ENV'] = df_feature['Ext Mean'] + df_feature['Flex Mean'] + df_feature['Ext Var'] + df_feature['Flex Var']


#print(df_feature)

line_plot(df_feature.iloc[399:500,:])

#df_concat = pd.concat([df_feature, df_label], axis = 1)

#df_concat['Raw Ext Var'] = df_concat['Raw Ext Var'].astype(float)

#

#min = df_feature.min()
#print(min)

#df_concat.iloc[2] = df_concat.iloc[2].multiply(3.3)

# df_concat['Label'] = df_concat['Label'].replace('H', 'Handshake')
# df_concat['Label'] = df_concat['Label'].replace('N', 'No Gesture')
# df_concat['Label'] = df_concat['Label'].replace('P', 'Pinch')
# df_concat['Label'] = df_concat['Label'].replace('PI', 'Pinch')
# df_concat['Label'] = df_concat['Label'].replace('PA', 'Paper')
# df_concat['Label'] = df_concat['Label'].replace('PE', 'Peace')
# df_concat['Label'] = df_concat['Label'].replace('R', 'Rock')
# df_concat['Label'] = df_concat['Label'].replace('S', 'Scissors')
#df_feature['Label'] = df_feature['Label'].replace('NaN', 'Nothing')
# df_concat = df_concat[df_concat['Label'] != 'DELETE']
# df_concat = df_concat[df_concat['Label'] != 'Handshake']
# df_concat = df_concat[df_concat['Label'] != 'Pinch']
# df_concat = df_concat[df_concat['Label'] != 'Scissors']
# df_concat = df_concat[df_concat['Label'] != 'Rock']
#df_feature = df_feature[df_feature['Gesture'] != 'N']

#df_feature.drop(df_feature.index[0:400], inplace=True)

df_feature.dropna(inplace=True)

df_feature['Ext Freq 2'] = df_feature['Ext Freq 2'] / 100
df_feature['Ext Freq 1'] = df_feature['Ext Freq 1'] / 100
df_feature['Flex Freq 2'] = df_feature['Flex Freq 2'] / 100
df_feature['Flex Freq 1'] = df_feature['Flex Freq 1'] / 100


#df_feature.fillna("N", inplace=True)


df_feature = round(df_feature.sample(frac=1),2)

print(df_feature)

# print(df_concat)
# print(df_concat.groupby('Label').size())
# print(df_concat.dtypes)

#df_feature.to_csv('freqRPSfeature.csv', index=False)