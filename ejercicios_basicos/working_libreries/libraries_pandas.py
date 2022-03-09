# trabajando con la libreria pandas

import pandas as pd

df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
print(df)

df_new = pd.DataFrame({'name': ["Shanel", "Carmel", "Candelario"], 'gender': ["Female","Male","Male"], 'age':[23,45,67]})
print(df_new)


# ------------------------------------------------------------------------------

'''
 Conviertiendo un archivo Excel en HTML con pandas
'''

archivo_excel = pd.read_excel('ejemplo_excel.xlsx')
print(type(archivo_excel))
html_final: str = archivo_excel.to_html()
print(html_final)