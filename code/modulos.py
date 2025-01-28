import pandas as pd

def explore_missing(datos):
    """
    Analyzes missing values in a DataFrame and provides statistics.

    Parameters:
    ----------
    datos : pd.DataFrame
        The input DataFrame to analyze.

    Returns:
    -------
    None.
    Prints the following statistics:
        - Number of complete rows (rows without missing values).
        - Proportion of complete rows relative to the total.
        - Proportion of non-missing values relative to the total number of cells.
        - A DataFrame summarizing missing values per column
    """

    # Cantidad de casos completos
    complete_cases = datos.dropna().shape[0]
    print("Complete cases:", complete_cases)

    # Proporción de casos completos
    prop_complete_cases = complete_cases / len(datos)
    print("Proportion of complete cases:", prop_complete_cases)

    # Proporción de valores (celdas) completas
    total_cells = datos.size
    total_complete = datos.count().sum()
    prop_complete = total_complete / total_cells
    print("Proportion of complete cells:", prop_complete)

    # Estadísticas por variable (valores faltantes)
    missing_summary = datos.isnull().sum().reset_index()
    missing_summary.columns = ['Variable', 'Missing Count']
    missing_summary['Missing Proportion'] = missing_summary['Missing Count'] / len(datos)
    print("\nMissing values by column:")
    print(missing_summary)

import pandas as pd


# Crear tablas con frecuencia absoluta y porcentaje
def create_frequency_table(column, column_name):
    """
    Creates a frequency table with both absolute frequency (N) and percentage for a given column in a DataFrame.
    The function also adds a row with total counts and percentage values.


    Args:
    column (pd.Series): The input column (Series) from a DataFrame for which the frequency table will be created.
    column_name (str): The name of the column, which will be used as the header in the resulting frequency table.

    Returns:
    pd.DataFrame: A DataFrame containing the frequency table with the following columns:
        - column_name: The unique values/categories in the input column.
        - N: The absolute frequency of each value/category.
        - Percentage: The percentage of each value/category based on the total count.
    """

    freq_table = column.value_counts(dropna=False).reset_index()
    freq_table.columns = [column_name, "N"]
    freq_table["Percentage"] = (freq_table["N"] / column.size * 100).round(2)
    
    # Agregar fila de totales
    total_row = pd.DataFrame({
        column_name: ["Total"],
        "N": [freq_table["N"].sum()],
        "Percentage": [freq_table["Percentage"].sum()]
    })
    freq_table = pd.concat([freq_table, total_row], ignore_index=True)
    return freq_table