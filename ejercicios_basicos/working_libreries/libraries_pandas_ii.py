"""_summary_

    Trabajando con la libreria Pandas para analisis de datos con dataframes

"""

import pandas as pd

dataframe_uno: pd.DataFrame = pd.DataFrame({'lkey': ['foo', 'bar', 'baz', 'foo'],'value': [1, 2, 3, 5]})
print(dataframe_uno)

dataframe_dos: pd.DataFrame = pd.DataFrame({'rkey': ['foo', 'bar', 'baz', 'foo'],'value': [5, 6, 7, 8]})
print(dataframe_dos)


# ---------------------------------------
# mezcla de dataframe
print("\n union de dataframas con merge \n")
print(dataframe_uno.merge(dataframe_dos, left_on='lkey', right_on='rkey'))


# ------------------------------------------------------------------------------------------------------
# creando una hoja de calculo con pandas

data_file: pd.DataFrame = pd.DataFrame([[100,433,10],[34,10,0],[75,125,5]], index=["Python 101","Python 201","wxPython"], columns=["Price","Students","Rating"])
data_file.to_excel("pandas_excel.xlsx",sheet_name="ejemplo_python_excel")


