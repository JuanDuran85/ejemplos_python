from pprint import pprint as pp
# profundizando en diccionarios
# Los diccionarios guardan un orden a diferencia de los set
# los diccionarios son mutables, pero las llaves deben ser inmutables
# los diccionarios no tienen llaves duplicadas, por lo tanto, si existe la llave la modifica o actualiza, si no existe la crea.
# si no se encuentra una llave, se genera o lanza una exception de key error

diccionario = {'nombre': 'Juan', 'apellido': 'Perez', 'edad': 23}

# metodo get recupera una llave, si no existe no lanza una exception. Se puede regresar un valor en el caso que no exista la llave
print(diccionario.get('Nombre', 'No se enconetró la referencia'))

# el metodo ser modifica el diccionario, si no se encuentra la llava agrega el valor por defecto
nombre = diccionario.setdefault('Nombre', 'No se encontró la llave')
print(diccionario)

# imprimir con pprint
pp(diccionario, sort_dicts=True)

# obtener las primeras tres llaves del diccionario
print("\n obtener las primeras tres llaves del diccionario \n")
diccionario_usuarios = {
    'nombre': 'Maria',
    'edad': 23,
    'ciudad': 'Paris',
    'pais': 'Francia',
    'admin': True,
    'correo': 'maria@correo.com',
    'programas': ['Python', 'JavaScript', 'C++'],
}

print(f"{diccionario_usuarios = }")
for index, values in enumerate(diccionario_usuarios.items()):
    if index > 2:
        break
    print(values)

contador = 0
for values in diccionario_usuarios:
    print(values, diccionario_usuarios.get(values))
    contador += 1
    if contador > 2:
        break

# si se cuales son las llaves (nunca cambiaran)
for contador_index in ['nombre', 'edad', 'ciudad']:
    print(contador_index, diccionario_usuarios[contador_index])


# Se puede crear una tabla indexada a partir de una lista con multiples diccionarios
#

data_mock: list[dict] = [
    {
        'id': 1,
        'first_name': 'Denna',
        'last_name': 'Gonzalez',
        'email': 'dgonzalez0@barnesandnoble.com',
        'gender': 'Female',
        'ip_address': '108.36.200.73',
        'country': 'France'
    }, 
    {
        'id': 2,
        'first_name': 'Anthony',
        'last_name': 'Frie',
        'email': 'afrie1@qq.com',
        'gender': 'Male',
        'ip_address': '5.114.252.29',
        'country': 'France'
    }, 
    {
        'id': 3,
        'first_name': 'Angelita',
        'last_name': 'Oxtaby',
        'email': 'aoxtaby2@redcross.org',
        'gender': 'Female',
        'ip_address': '237.59.190.5',
        'country': 'Sweden'
    }, 
    {
        'id': 4,
        'first_name': 'Rutledge',
        'last_name': 'Minshall',
        'email': 'rminshall3@oracle.com',
        'gender': 'Male',
        'ip_address': '64.7.220.177',
        'country': 'Morocco'
    }, 
    {
        'id': 5,
        'first_name': 'Fin',
        'last_name': 'Jiroutka',
        'email': 'fjiroutka4@drupal.org',
        'gender': 'Male',
        'ip_address': '253.81.63.142',
        'country': 'Portugal'
    }, 
    {
        'id': 6,
        'first_name': 'Ibby',
        'last_name': 'Bradnick',
        'email': 'ibradnick5@hostgator.com',
        'gender': 'Female',
        'ip_address': '154.201.151.79',
        'country': 'United States'
    }, 
    {
        'id': 7,
        'first_name': 'Dena',
        'last_name': 'Blinco',
        'email': 'dblinco6@studiopress.com',
        'gender': 'Female',
        'ip_address': '29.46.11.160',
        'country': 'Spain'
    }, 
    {
        'id': 8,
        'first_name': 'Case',
        'last_name': 'Martlew',
        'email': 'cmartlew7@auda.org.au',
        'gender': 'Male',
        'ip_address': '53.21.76.250',
        'country': 'Japan'
    }, 
    {
        'id': 9,
        'first_name': 'Ashlin',
        'last_name': 'Mullaly',
        'email': 'amullaly8@nhs.uk',
        'gender': 'Male',
        'ip_address': '95.161.192.195',
        'country': 'Portugal'
    }, 
    {
        'id': 10,
        'first_name': 'Diego',
        'last_name': 'Shemmin',
        'email': 'dshemmin9@merriam-webster.com',
        'gender': 'Male',
        'ip_address': '123.158.156.192',
        'country': 'Japan'
    }, 
    {
        'id': 11,
        'first_name': 'Ailsun',
        'last_name': 'Keogh',
        'email': 'akeogha@boston.com',
        'gender': 'Female',
        'ip_address': '11.215.125.107',
        'country': 'Spain'
    }, 
    {
        'id': 12,
        'first_name': 'Bethena',
        'last_name': 'Coppen',
        'email': 'bcoppenb@wired.com',
        'gender': 'Female',
        'ip_address': '85.215.199.9',
        'country': 'Sweden'
    }, 
    {
        'id': 13,
        'first_name': 'Esta',
        'last_name': 'Garthside',
        'email': 'egarthsidec@cloudflare.com',
        'gender': 'Female',
        'ip_address': '50.118.156.75',
        'country': 'Sweden'
    }, 
    {
        'id': 14,
        'first_name': 'Immanuel',
        'last_name': 'Radford',
        'email': 'iradfordd@psu.edu',
        'gender': 'Male',
        'ip_address': '27.113.205.241',
        'country': 'China'
    }, 
    {
        'id': 15,
        'first_name': 'Genia',
        'last_name': 'Trengrove',
        'email': 'gtrengrovee@mashable.com',
        'gender': 'Female',
        'ip_address': '178.81.118.74',
        'country': 'Spain'
    }, 
    {
        'id': 16,
        'first_name': 'Josefina',
        'last_name': 'De Carteret',
        'email': 'jdecarteretf@mtv.com',
        'gender': 'Female',
        'ip_address': '170.0.124.51',
        'country': 'France'
    }, 
    {
        'id': 17,
        'first_name': 'Franz',
        'last_name': 'Briston',
        'email': 'fbristong@cnn.com',
        'gender': 'Male',
        'ip_address': '17.230.248.93',
        'country': 'Poland'
    }, 
    {
        'id': 18,
        'first_name': 'Pierce',
        'last_name': 'Foye',
        'email': 'pfoyeh@themeforest.net',
        'gender': 'Male',
        'ip_address': '178.14.54.40',
        'country': 'Spain'
    }, 
    {
        'id': 19,
        'first_name': 'Thayne',
        'last_name': 'Couvert',
        'email': 'tcouverti@flavors.me',
        'gender': 'Male',
        'ip_address': '1.53.73.172',
        'country': 'China'
    }, 
    {
        'id': 20,
        'first_name': 'Noach',
        'last_name': 'Aleksashin',
        'email': 'naleksashinj@google.com',
        'gender': 'Male',
        'ip_address': '72.196.62.76',
        'country': 'Portugal'
    }]

data_table_by_country: dict[str,list] = {}

for data_obj in data_mock:
    data_from_country: list = []
    country_obj: str = str(data_obj['country'])
    
    if (not data_table_by_country.get(country_obj)):
        data_table_by_country.setdefault(country_obj, [data_obj])

    data_from_country = data_table_by_country.get(country_obj) or []
    data_from_country.append(data_obj)
    data_table_by_country[country_obj] = data_from_country
    
print(data_table_by_country)