import pandas as pd
import streamlit as st

from tables.correspondency import test_table_dict


def create_inputs(test_table):
    inputs = {}
    clean_table = test_table.drop(columns=["Pc", "De"])

    for i in range(0, len(clean_table.columns), 3):
        col1, col2, col3 = st.columns(3)
        with col1:
            if i < len(clean_table.columns):
                column = clean_table.columns[i]
                inputs[column] = st.text_input(f"Ingresa datos para {column}", "")
        with col2:
            if i + 1 < len(clean_table.columns):
                column = clean_table.columns[i + 1]
                inputs[column] = st.text_input(f"Ingresa datos para {column}", "")
        with col3:
            if i + 2 < len(clean_table.columns):
                column = clean_table.columns[i + 2]
                inputs[column] = st.text_input(f"Ingresa datos para {column}", "")
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
    processed_column: pd.Series = df[column].apply(process_cell)

    # Finding the index
    if (processed_column <= value).any():
        index = processed_column[
            processed_column <= value].idxmax()  # The highest index where the value is less or equal
    else:
        index = processed_column.idxmin()

    return df.loc[index, "Pc"]  # Returning the 'Pc' value corresponding to the found index


def test_process(inputs, selected_test):
    # Code to process user inputs goes here
    new_inputs = {key: float(value) for key, value in inputs.items() if value != ""}

    try:
        # Read the CSV into a DataFrame
        table = pd.read_csv(test_table_dict[selected_test])

        # Create a list to hold both input and output data for display
        results_list = []

        # Process each input and find corresponding output, then add to the list
        for column in new_inputs:
            # Use find_index function to compute the output for each test
            output_value = find_index(table, column, new_inputs[column])
            # Append both input and output to the results list
            results_list.append({'Test': column, 'Input': new_inputs[column], 'Output': output_value})

        # Convert the results list to a DataFrame for nicer display
        results_df = pd.DataFrame(results_list)

        # Display the combined input and output data in table format
        st.markdown("### Resultados:")
        st.table(results_df)
    except KeyError:
        # If there's a KeyError, display only the inputs as the test was not found
        st.markdown("### User Inputs:")
        # Convert user inputs to a DataFrame for display
        inputs_df = pd.DataFrame(new_inputs.items(), columns=['Test', 'Input'])
        st.table(inputs_df)

        st.markdown("### Selected Test:")
        st.write(selected_test)
        # Display an error message if the selected test is not found
        st.error("The selected test was not found in the database.")
