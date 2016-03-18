import numpy as np
import pandas as pd


def remove_invalid_data(path):
    """ Takes a path to a water pumps csv, loads in pandas, removes
        invalid columns and returns the dataframe.
    """
    df = pd.read_csv(path, index_col=0)
    return df


def gimme_the_mean(series):
    if isinstance(series, float):
        return series

    return np.mean(series)
