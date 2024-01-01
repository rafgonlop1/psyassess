import pandas as pd
import streamlit as st

from tables.correspondency import test_table_dict


def create_inputs(test_table):
    inputs = {}
    clean_table = test_table.drop(columns=["Pc", "De"])
    for column in clean_table.columns:
        input_value = st.text_input(f"Ingresa datos para {column}", "")
        inputs[column] = input_value
    return inputs


# Function to find the appropriate index
def find_index(df, column, value):
    # Function to convert ranges and conditions into manageable numbers
    def process_cell(cell):
        if "-" in cell:  # It's a range
            return float(cell.split("-")[1])  # Take the upper end of the range
        elif cell.startswith("<"):
            return float(cell[1:]) - 0.5  # Slightly less than the lower limit
        elif cell.startswith(">"):
            return float(cell[1:]) + 0.5  # Slightly more than the upper limit
        else:
            return float(cell)  # It's a normal number

    # Processing the desired column
    processed_column = df[column].apply(process_cell)

    # Finding the index
    if any(processed_column <= value):
        index = processed_column[processed_column <= value].idxmax()  # The highest index where the value is less or equal
    else:
        index = processed_column.idxmin()

    return df.loc[index, "Pc"]  # Returning the 'Pc' value corresponding to the found index


def test_process(inputs, selected_test):
    # Code to process user inputs goes here
    # Delete keys with empty values
    new_inputs = {}
    for key in inputs:
        if inputs[key] != "":
            new_inputs[key] = inputs[key]

    try:
        # Read the table
        table = pd.read_csv(test_table_dict[selected_test])

        # Find the index for each column
        outputs = {}
        for column in new_inputs:
            outputs[column] = find_index(table, column, float(new_inputs[column]))

        st.write("Salidas del usuario:", outputs)
    except KeyError:
        st.write("Entradas del usuario:", new_inputs)
        st.write("Prueba seleccionada:", selected_test)
        st.write("No se encontró la prueba seleccionada en la base de datos.")
