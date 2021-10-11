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
                log.debug("Registros insertados: {}".format(registros))
                return registros
                
    @classmethod
    def actualizar(cls,persona):
        """
            Actualiza registros en la base de datos
        """
        with Conexion.obtener_conexion():
            with Conexion.obtener_cursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
                cursor.execute(cls.__ACTUALIZAR, valores)
                log.debug("Valores actualizados: {}".format(valores))
                registros = cursor.rowcount
                log.debug("Registros actualizados: {}".format(registros))
                return registros

    @classmethod
    def eliminar(cls, persona):
        """
            Elimina registros por el id en la base de datos
        """
        with Conexion.obtener_conexion():
            with Conexion.obtener_cursor() as cursor:
                valores = (persona.id_persona,)
                cursor.execute(cls.__ELIMINAR, valores)
                log.debug("Persona eliminada: {}".format(persona))
                registros = cursor.rowcount
                log.debug("Registro eliminado: {}".format(registros))
                return registros


if __name__ == "__main__":

    # insertando persona
    #persona1 = Persona(nombre="Isabell", apellido="Murphy",email="Bradley.Streich88@yahoo.com")
    #insertando = PersonaDAO.insertar(persona1)
    #log.debug(insertando)

    # actualiando persona
    #persona1 = Persona(id_persona=10,nombre="Isabell", apellido="Murphy",email="Bradley.Streich88@yahoo.com")
    #actualizando = PersonaDAO.actualizar(persona1)
    #log.debug(actualizando)

    # eleimiar un registro
    for i in range(12,27):
        persona1 = Persona(id_persona=i)
        eliminado = PersonaDAO.eliminar(persona1)
        log.debug("Persona eliminada: {}".format(eliminado))

    # seleccionando objetos
    personas_final = PersonaDAO.seleccionar()
    for registro in personas_final:
        log.debug(registro)