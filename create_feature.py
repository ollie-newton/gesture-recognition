import pandas as pd
import numpy as np
import plotly.express as px


def time_features(windowed_df, feature_df):

    feature_df['meanEE'] = 0
    feature_df['meanEF'] = 0
    feature_df['varRE'] = 0
    feature_df['varRF'] = 0
    for i in range(0,len(feature_df)):

        meanEE = np.mean(windowed_df.iloc[:, (5*i+1)])
        feature_df.iloc[i, 1] = meanEE

        meanEF = np.mean(windowed_df.iloc[:, (5*i+3)])
        feature_df.iloc[i, 2] = meanEF

        varRE = np.var(windowed_df.iloc[:, (5*i)])
        feature_df.iloc[i, 3] = varRE

        varRF = np.var(windowed_df.iloc[:, (5*i+2)])
        feature_df.iloc[i, 4] = varRF

    pd.set_option('display.max_rows', None)
    return feature_df
    
    # fft_rawFlex = np.fft.fft(windowed_df.iloc[:,2]) #change time compo

    # print(fft_rawFlex)
    # mag_rawFlex = np.abs(fft_rawFlex)

    # fig = px.line(mag_rawFlex)

    # fig.show()