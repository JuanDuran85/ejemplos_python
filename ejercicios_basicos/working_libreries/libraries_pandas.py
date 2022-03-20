"""_summary_

    Trabajando con la libreria Pandas

"""

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

# archivo_excel = pd.read_excel('ejemplo_excel.xlsx')
# print(type(archivo_excel))
# html_final: str = archivo_excel.to_html()
# print(html_final)

# ------------------------------------------------------------------------------
# Series con pandas en python
series1: pd.Series = pd.Series([3,5,7])
print(f"{series1 = }")

# series para notas y asignaturas
cursos: list = ['Matematicas', 'Fisica', 'Quimica', 'Programacion']
notas_cursos_uno: list = [8,9,5,10]
series_notas_uno: pd.Series = pd.Series(notas_cursos_uno, index=cursos)
# para darle nombre a la serie
series_notas_uno.name = 'Series de Notas Finales'
# para cambiar el nombre del indice
series_notas_uno.index.name = "Solo notas"
print(f"{series_notas_uno }")
print(f"{series_notas_uno.index = }")
print(f"{series_notas_uno.values = }")
print(f"{series_notas_uno['Fisica'] = }")
print(f"{series_notas_uno[series_notas_uno >= 9]}")
# conviertiendo una series en diccionario
series_en_diccionario: dict = series_notas_uno.to_dict()
print(f"{series_en_diccionario = }")
# para convertir de un diccionario a una serie
serie_nueva: pd.Series = pd.Series(series_en_diccionario)
print(f"{serie_nueva }")
# otra serie
cursos: list = ['Matematicas', 'Fisica', 'Quimica', 'Programacion']
notas_cursos_dos: list = [7,7,8,8]
series_notas_dos: pd.Series = pd.Series(notas_cursos_dos, index=cursos)
print(series_notas_dos)

# suma de series
series_notas_finales: pd.Series = (series_notas_uno + series_notas_dos) / 2
print(series_notas_finales)

#-----------------------------------------------------------------------------------
print("\n--------------------------------")
# trabajando con dataframes sacandolos del clipboard al ser copiados desde una pagina web
# web con datos: https://es.wikipedia.org/wiki/Copa_Mundial_de_F%C3%BAtbol
dataframe_fifa_goles = pd.read_clipboard()
print(dataframe_fifa_goles)
# mostrar el nombre de las columnas
print(dataframe_fifa_goles.columns)
print(dataframe_fifa_goles['Campeón '])
# para recuperar por el indice
print(dataframe_fifa_goles.loc[7])
# si el dataframe es muy grande se puede mostrar las 5 primeras filas por defecto
print(dataframe_fifa_goles.head())
# para mostrar los cinco ultimos elementos por defecto del dataframes
print(dataframe_fifa_goles.tail())

# dataframes con datos de un diccionario y listas
lista_asignaturas: list = ['Matematicas', 'Fisica', 'Quimica', 'Programacion', 'Historia']
lista_notas: list = [8,9,5,10,7]
diccionario_final: dict = {
    'Asignaturas': lista_asignaturas,
    'Notas': lista_notas,
}
dataframes_notas: pd.DataFrame = pd.DataFrame(diccionario_final)
print(dataframes_notas)

print("-------------------------------------------- \n")
# indices en pandas para series, los indices no se pueden cambiar
lista_valores: list = [1,2,3]
lista_indices: list = ['a', 'b', 'c']
series_final: pd.Series = pd.Series(lista_valores, index=lista_indices)
print(series_final)
print(series_final.index)
print(series_final.index[0])

# ------------------------------------------------------------------------------------
# dataframes con valores, indices y columnas
lista_valores_notas: list = [[6,7,3],[8,9,8],[5,6,7]]
lista_indices_asignaturas: list = ['Matematicas', 'Fisica', 'Quimica']
lista_columnas_nombres: list = ['Maria', 'Luis', 'Josefina']
dataframe: pd.DataFrame = pd.DataFrame(lista_valores_notas, index=lista_indices_asignaturas, columns=lista_columnas_nombres)
print(dataframe)
print(dataframe.loc['Fisica'])
print(dataframe.index)

# eliminar elementos de un dataframe