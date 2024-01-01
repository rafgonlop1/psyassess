import streamlit as st

from data import load_tests, load_test_table
from utils import create_inputs, test_process


def main():
    st.title("PsyAssess - Herramienta de Corrección de Pruebas de Diagnóstico")

    st.write(
        "Bienvenido a PsyAssess, una herramienta interactiva para la corrección y análisis de pruebas de diagnóstico.")

    # Load available tests
    tests = load_tests()

    # Create a dropdown menu to select a test
    selected_test = st.selectbox("Selecciona una prueba de diagnóstico", tests)

    # Load data for the selected test
    test_table = load_test_table(selected_test)

    # Add toggle checkbox
    if st.checkbox('Mostrar Datos de la Prueba Seleccionada'):
        st.write("Datos de la Prueba Seleccionada:")
        st.dataframe(test_table, hide_index=True)

    # Create input fields for each column
    test_inputs = create_inputs(test_table)

    # Submit button
    if st.button("Enviar"):
        test_process(test_inputs, selected_test)


if __name__ == "__main__":
    main()
