from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def normalise(feature_df):

    # create a MinMaxScaler object
    scaler = MinMaxScaler()

    cols_to_normalize = ['meanEE', 'meanEF', 'varRE', 'varRF']
    df_normalized = feature_df.copy()
    df_normalized[cols_to_normalize] = scaler.fit_transform(feature_df[cols_to_normalize])

    # copy the string column B to the normalized dataframe
    df_normalized['Label'] = feature_df['Label']

    return df_normalized
