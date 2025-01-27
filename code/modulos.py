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
