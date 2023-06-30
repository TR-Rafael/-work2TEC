import re
import random
import numpy as np
import pandas as pd


def convert_range_to_random(range_string):
    range_values = re.findall(r'\d+', range_string)
    if len(range_values) == 2:
        start = int(range_values[0])
        end = int(range_values[1])
        if not any(np.isnan([start, end])):
            return random.sample(range(start, end + 1), 1)[0]
    return np.nan


def treat_data(df: pd.DataFrame):
    replace_dict = {'< 9': '0 - 9', '> 100': '100 - 110'}
    df["age"].replace(replace_dict, inplace=True)
    df["age"] = df["age"].apply(convert_range_to_random)
    return df
