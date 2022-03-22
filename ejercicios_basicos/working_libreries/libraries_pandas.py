"""_summary_

    Trabajando con la libreria Pandas

"""

# trabajando con la libreria pandas

import numpy as np
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
series_nueva_ordenar: pd.Series = pd.Series(np.arange(4), index=['d', 'b', 'a', 'c'])
print(series_nueva_ordenar)
# ordenacion y clasificacion de series
print("Series nueva por ordenar")
print(series_nueva_ordenar.sort_index())
print(series_nueva_ordenar.sort_values())
# para borrar se usa el drop
resulta_delete: pd.Series = series_nueva_ordenar.drop('c')
print(resulta_delete)

# borrar fila y/o columna en dataframa
print(" \r -------------------------------------------- \n")
lista_valores_nueva = np.arange(9).reshape(3,3)
lista_indices: list = ['c', 'b', 'a']
lista_columnas = ['c1', 'c2', 'c3']
dataframe_por_ordenar = pd.DataFrame(lista_valores_nueva, index=lista_indices, columns=lista_columnas)
print(dataframe_por_ordenar)
borrar_elemento = dataframe_por_ordenar.drop('c1', axis=1)
print(borrar_elemento)
borrar_elemento = dataframe_por_ordenar.drop('a')
print(borrar_elemento)

# seleccionando datos de una serie
print(" \r -------------------------------------------- \n")
lista_valores_nueva = np.arange(3)
lista_indices: list = ['i1', 'i2', 'i3']
series_nueva: pd.Series = pd.Series(lista_valores_nueva, index=lista_indices)
print(series_nueva)
print(series_nueva[2])
print(series_nueva['i2'])
print(series_nueva['i1':'i2'])
series_nueva = series_nueva * 2
print(series_nueva[series_nueva > 3])


# -----------------------------------------------------------------------------------------
# seleccionar datos en dataframe
print(" --- -------- ------------------------------- \n")
lista_valores_nueva = np.arange(25).reshape(5,5)
lista_indices: list = ['i1', 'i2', 'i3', 'i4', 'i5']
lista_columnas = ['c1', 'c2', 'c3', 'c4', 'c5']
dataframe = pd.DataFrame(lista_valores_nueva, index=lista_indices, columns=lista_columnas)
print(dataframe)
print(dataframe['c2'])
print(dataframe['c2']['i4'])
print(dataframe[['c3','c4']])
print(dataframe[dataframe['c3'] > 15])
print(dataframe > 20)
print(dataframe.loc['i3'])

# operaciones sobre series y dataframes
lista_valores = np.arange(4).reshape(2,2)
lista_indices: list = ['b', 'a']
lista_columnas = ['1', '2']
dataframe = pd.DataFrame(lista_valores, index=lista_indices, columns=lista_columnas)
print(dataframe)
lista_valores_dos = np.arange(9).reshape(3,3)
lista_indices_dos: list = ['c', 'a', 'b']
lista_columnas_dos = ['1', '2','3']
dataframe_dos = pd.DataFrame(lista_valores_dos, index=lista_indices_dos, columns=lista_columnas_dos)
print(dataframe_dos)

print(dataframe + dataframe_dos)
resultado_suma = dataframe + dataframe_dos

print(dataframe.add(dataframe_dos, fill_value=0))

#------------------------------------------------------------------------------------
print("\n")
# estadiisticas con dataframes y series
lista_valores = np.arange(25).reshape(5,5)
lista_indices: list = ['i1', 'i2', 'i3', 'i4', 'i5']
lista_columnas = ['c1', 'c2', 'c3', 'c4', 'c5']
dataframe_estadisticas = pd.DataFrame(lista_valores, index=lista_indices, columns=lista_columnas)
print(dataframe_estadisticas)
# suma por columa
print(dataframe_estadisticas.sum())
# suma por fila
print(dataframe_estadisticas.sum(axis=1))
# el minimo valor
print(dataframe_estadisticas.min())
# el maximo valor
print(dataframe_estadisticas.max(axis=1))
# para ver cual es el indice con el menor valor
print(dataframe_estadisticas.idxmin())
# serie de valores estadisticos para un dataframe
print(dataframe_estadisticas.describe())


#------------------------------------------------------------------------------------
print("\n")
print("Valores nulos en Series y DataFrame".center(50, "-"))
# trabajando con valores nulos
lista_valores: list = ['3','0',np.nan,'-4','9']
series_nulos: pd.Series = pd.Series(lista_valores, index=list('abcde'))
print(series_nulos)
# ver cuales son nulos
print(series_nulos.isnull())
# borrar valores nulos
nueva_series_borrada = series_nulos.dropna()
print(nueva_series_borrada)

# con dataframes
lista_valores: list = [[3,0,-2],[np.nan,2,-2],[9,5,np.nan]]
lista_indices: list = list('123')
lista_columnas: list = list('abc')
dataframe_nulos = pd.DataFrame(lista_valores, index=lista_indices, columns=lista_columnas)
print(dataframe_nulos)
# valores nulos
print(dataframe_nulos.isnull())
# borrar valores nulos, borrando toda la fila que contenga algun elemento nulo
print(dataframe_nulos.dropna())
# rellenar los nulos con algun valor de forma rapida
print(dataframe_nulos.fillna(0))


# ----------------------------------------------------------------------------------------
# construyendo dataframe desde pagina web con pandas
# ----------------------------------------------------------------------------------------
print("\n--------------------------------")

url_web: str = 'https://es.wikipedia.org/wiki/Anexo:Selecciones_de_f%C3%BAtbol_campeonas_del_mundo'
dataframe_puro = pd.read_html(url_web)
print(dataframe_puro)


dataframe_resultante = dataframe_puro[0]
print(dataframe_resultante)




