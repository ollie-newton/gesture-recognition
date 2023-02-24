import numpy as np
import pandas as pd

def overlapping_windows(df, window_size, overlap):
    no_windows = round(df.shape[0] / (window_size-overlap) - 1)

    newer_df = pd.DataFrame()

    for i in range(0,no_windows):

        new_df = pd.DataFrame(df.iloc[i*(window_size-overlap):window_size+i*(window_size-overlap),:])
        new_df = new_df.reset_index(drop=True)
        newer_df = pd.concat([newer_df, new_df], axis=1)

    return newer_df