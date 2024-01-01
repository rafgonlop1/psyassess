import pandas as pd


def load_tests():
    # Code to load the list of available tests goes here
    return ["Prueba 1", "Prueba 2", "Prueba 3"]


def load_test_table(test):
    # Code to load data for the specific test goes here
    # Simulating data loading with a sample DataFrame
    if test == "Prueba 1":
        return pd.DataFrame({
            "Columna1": [1, 2, 3],
            "Columna2": [4, 5, 6]
        })
    elif test == "Prueba 2":
        return pd.DataFrame({
            "Columna1": [1, 2, 3, 4],
            "Columna2": [4, 5, 6, 7],
            "Columna3": [8, 9, 10, 11]
        })
    else:
        return pd.DataFrame({
            "Columna1": [1, 2, 3],
            "Columna2": [4, 5, 6]
        })
