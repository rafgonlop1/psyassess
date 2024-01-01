import streamlit as st


def create_inputs(test_table):
    inputs = {}
    for column in test_table.columns:
        input_value = st.text_input(f"Ingresa datos para {column}", "")
        inputs[column] = input_value
    return inputs


def test_process(inputs, selected_test):
    # Code to process user inputs goes here
    # For now, we just print the inputs
    st.write("Entradas del usuario:", inputs)
