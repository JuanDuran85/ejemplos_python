import bcrypt
class Usuario:
    def __init__(self, id_usuario=None, username=None, password=None):
        self.__id_usuario = id_usuario
        self.__username = username
        self.__password = password

    @classmethod
    def encrypt(cls, password):
        encry_pass = password.encode('utf-8')
        hashed = bcrypt.hashpw(encry_pass, bcrypt.gensalt(14))
        return hashed.decode('utf-8')

    @property
    def id_usuario(self):
        return self.__id_usuario

    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self.__id_usuario = id_usuario

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username

    @property
    def password(self):
        return Usuario.encrypt(self.__password)
    
    @password.setter
    def password(self, password):
        if len(password) > 6:
            self.__password = password
        else:
            raise ValueError("La contraseña debe tener al menos 6 caracteres")

    def __str__(self):
        return f"{self.id_usuario} {self.username} {self.password}"


if __name__ == '__main__':
    usuario = Usuario(1, 'pepe', '1234')
    print(usuario)