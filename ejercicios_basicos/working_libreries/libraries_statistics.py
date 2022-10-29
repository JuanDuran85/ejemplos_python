import statistics as st

#--------------------------------------------------------------------------------------------
# Media Aritmetica
# Utilizando el metodo mean, se puede calcular la media aritmetica de una lista de numeros
#--------------------------------------------------------------------------------------------
print("Media Aritmetica".center(50, "-"))
values_to_media = [4,6,7,2,1,3,9,7,5,4]
media_result = st.mean(values_to_media)
print(media_result)
#--------------------------------------------------------------------------------------------

print("\n")

#--------------------------------------------------------------------------------------------
# Mediana
# Utilizando el metodo median, se puede calcular la mediana de una lista de numeros
#--------------------------------------------------------------------------------------------
print("Mediana".center(50, "-"))
values_to_mediana = [4,6,7,2,1,3,9,7,5,4]
mediana_result = st.median(values_to_media)
print(mediana_result)
#--------------------------------------------------------------------------------------------

print("\n")

#--------------------------------------------------------------------------------------------
# Moda
# Utilizando el metodo mode, se puede calcular la moda de una lista de numeros
#--------------------------------------------------------------------------------------------
print("Moda".center(50, "-"))
values_to_moda = [4,6,7,2,1,3,9,7,5,4]
moda_result = st.mode(values_to_moda)
print(moda_result)
#--------------------------------------------------------------------------------------------

print("\n")

#--------------------------------------------------------------------------------------------
# Desviación Estándar
# Utilizando el metodo stdev, se puede calcular la desviación estándar de una lista de numeros
#--------------------------------------------------------------------------------------------
print("Desviación Estándar".center(50, "-"))
values_to_desviacion_estandar = [4,6,7,2,1,3,9,7,5,4]
desviacion_estandar_result = st.stdev(values_to_desviacion_estandar)
print(desviacion_estandar_result)
#--------------------------------------------------------------------------------------------

print("\n")

#--------------------------------------------------------------------------------------------
# Desviación Estándar de la Población
# Utilizando el metodo pstdev, se puede calcular la desviación estándar de la poblacion de una lista de numeros
#--------------------------------------------------------------------------------------------
print("Desviación Estándar de la Población".center(50, "-"))
values_to_dep = [4,6,7,2,1,3,9,7,5,4]
dep_result = st.pstdev(values_to_dep)
print(dep_result)
#--------------------------------------------------------------------------------------------

print("\n")

#--------------------------------------------------------------------------------------------
# Varianza
# Utilizando el metodo variance, se puede calcular la Varianza de una lista de numeros
#--------------------------------------------------------------------------------------------
print("Varianza".center(50, "-"))
values_to_varianza = [4,6,7,2,1,3,9,7,5,4]
varianza_result = st.variance(values_to_varianza)
print(varianza_result)
#--------------------------------------------------------------------------------------------

print("\n")

#--------------------------------------------------------------------------------------------
# Varianza Poblacional
# Utilizando el metodo pvariance, se puede calcular la Varianza Poblacional de una lista de numeros
#--------------------------------------------------------------------------------------------
print("Varianza Poblacional".center(50, "-"))
values_to_varianza_poblacional = [4,6,7,2,1,3,9,7,5,4]
varianza_poblacional_result = st.pvariance(values_to_varianza_poblacional)
print(varianza_poblacional_result)
#--------------------------------------------------------------------------------------------

print("\n")

#--------------------------------------------------------------------------------------------
# Regresion Lineal
# Utilizando el metodo mean, se puede calcular la media aritmetica de una lista de numeros
#--------------------------------------------------------------------------------------------
print("Varianza Poblacional".center(50, "-"))
data_one = [4,6,7,2,1,3,9,7,5,4]
data_two = [1,2,3,4,5,6,7,8,9,0]
result = st.linear_regression(data_one, data_two)
print(result)
#--------------------------------------------------------------------------------------------