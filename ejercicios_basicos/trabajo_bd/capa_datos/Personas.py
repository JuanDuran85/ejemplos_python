from logger_base import log

class Persona:
    def __init__(self,id_persona=None, nombre=None, apellidos=None, email=None):
        self.__id_persona = id_persona
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__email = email

    @property
    def id_persona(self):
        return self.__id_persona

    @id_persona.setter
    def id_persona(self, id_persona):
        self.__id_persona = id_persona

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, apellidos):
        self.__apellidos = apellidos
        
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    def __str__(self):
        return "Id: {}. Nombre: {}, Apellidos: {}, Email: {}".format(self.id_persona,self.nombre, self.apellidos, self.email)

if __name__ == "__main__":
    persona = Persona(1, "Juan", "Pérez", "jp@email.com")
    log.debug(persona)