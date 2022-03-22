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