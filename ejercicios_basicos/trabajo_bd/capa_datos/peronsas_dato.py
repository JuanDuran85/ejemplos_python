# DAO - Data Access Object
# Patron de diseño para cominicarse con la base de datos
# Aqui se encuentran las operaciones CRUD de una clase de Entidad (Persona en este caso)

from logger_base import log
from conexion import Conexion
from Personas import Persona

class PersonaDAO():
    """ 
      DAO - Data Access Object  
    """

    __SELECCIONAR = "SELECT * FROM persona ORDER BY id_persona"
    __INSERTAR = "INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)"
    __ACTUALIZAR = "UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s"
    __ELIMINAR = "DELETE FROM persona WHERE id_persona = %s"

    @classmethod
    def seleccionar(cls):
        """
            Selecciona todos los registros de la tabla persona
        """
        with Conexion.obtener_cursor() as cursor:
            cursor.execute(cls.__SELECCIONAR)
            registros = cursor.fetchall()
            log.debug(registros)
            personas = []
            for registro in registros:
                persona = Persona(*registro)
                log.debug(persona)
                personas.append(persona)
            return personas

    @classmethod
    def insertar(cls,persona):
        """
            Inserta nuevos registros en la base de datos
            persona sera un objeto de la clase Persona
        """
        with Conexion.obtener_conexion():
            with Conexion.obtener_cursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls.__INSERTAR, valores)
                log.debug("Persona insertada: {}".format(persona))
                registros = cursor.rowcount
                log.debug("Registros modificados: {}".format(registros))
                return registros
                

if __name__ == "__main__":

    # insertando persona
    persona1 = Persona(nombre="Isabell", apellido="Murphy",email="Bradley.Streich88@yahoo.com")
    insertando = PersonaDAO.insertar(persona1)
    log.debug(insertando)

    # seleccionando objetos
    personas_final = PersonaDAO.seleccionar()
    for registro in personas_final:
        print(registro)