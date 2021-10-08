import psycopg2

conexion = psycopg2.connect(user='postgres', password='1234',
                            host='127.0.0.1', port='5432', database='test_db')

try:
    # crear un cursos para ejecutar sentencias sql en postgres
    cursor = conexion.cursor()
    # creamos la sentencia a ejecutar
    sentancia_sql = 'SELECT * FROM persona'
    # ejecutamos la sentencia
    cursor.execute(sentancia_sql)
    # obtenemos los resultados
    registros = cursor.fetchall()

    print(registros)

    # cerrar el cursor y la conexion
    cursor.close()
    conexion.close()
except (Exception, psycopg2.DatabaseError) as error:
    print("El error fue: {}".format(error))

    
