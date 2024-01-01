import pandas as pd

from tables.correspondency import test_table_dict


def load_tests():
    # Code to load the list of available tests goes here
    return list(test_table_dict.keys())


def load_test_table(test):
    # Code to load data for the specific test goes here
    # Simulating data loading with a sample DataFrame
    try:
        table = pd.read_csv(test_table_dict[test])

        return table
    except KeyError:
        return pd.DataFrame({
            "Columna1": [1, 2, 3],
            "Columna2": [4, 5, 6]
        })
