"""_summary_

    Patron de diseño: Factory Method.
    Provee una interfaz o clase abstracta (creator) que permite encapsular la lógica de creación de los objetos en subclases y éstas deciden qué clase instanciar. Los objetos se crean a partir de un método (factory method) y no a través de un constructor como se hace normalmente. Además, los ConcreteCreators devuelven siempre la interfaz (Product), esto permite que el cliente trate a los productos por igual, tengan una implementación u otra.
    
    Es un patron creacional que nos permite encapsular la logica de creacion de objetos mediante una clase abstracta o una interfaz que seria una factoria o fabrica.
"""

# creacion de la factoria (Factory Method) para un logger.

import datetime as dt
from colorama import init, Fore, Back, Style
from abc import ABC, abstractmethod

init(autoreset=True)

# clase abstracta
class Logger(ABC):
    
    @abstractmethod
    def info(self, message=None, object=None): ...
    
    @abstractmethod
    def warning(self, message=None, object=None): ...
    
    @abstractmethod
    def error(self, message=None, object=None): ...
    
    @abstractmethod
    def debug(self, message=None, object=None): ...
    
# clases que la logger factory instanciara posteriormente    
class LoggerConsola(Logger):
    
    def info(self, message=None, object=None):
        print(f"{str(dt.datetime.now())} {Fore.GREEN} [INFO] {message, str(object)} {Style.RESET_ALL}")
        
    def warning(self, message=None, object=None):
        print(f"{str(dt.datetime.now())} {Fore.YELLOW} [WARNING] {message, str(object)} {Style.RESET_ALL}")
        
    def error(self, message=None, object=None):
        print(f"{str(dt.datetime.now())} {Fore.RED} [ERROR] {message, str(object)} {Style.RESET_ALL}")
        
    def debug(self, message=None, object=None):
        print(f"{str(dt.datetime.now())} {Fore.BLUE} [DEBUG] {message, str(object)} {Style.RESET_ALL}")

log_file = "file.log"
class LoggerFile(Logger):
    
    def __file_open(self, message=None, object=None, type_message=None):
        with open(log_file, "a") as file_logger:
            data = f"{str(dt.datetime.now())} [{type_message}] {message, str(object)}\n"
            file_logger.writelines(data)
    
    def info(self, message=None, object=None):
        self.__file_open(message, object, "INFO")
        
    def warning(self, message=None, object=None):
        self.__file_open(message, object, "WARNING")

    def error(self, message=None, object=None):
        self.__file_open(message, object, "ERROR")
        
    def debug(self, message=None, object=None):
        self.__file_open(message, object, "DEBUG")

class LoggerEmail(Logger):
    def info(self, message=None, object=None):
        print(f"{str(dt.datetime.now())} Mail [INFO] {message, str(object)}")
    
    def warning(self, message=None, object=None):
        print(f"{str(dt.datetime.now())} Mail [WARNING] {message, str(object)}")
    
    def error(self, message=None, object=None):
        print(f"{str(dt.datetime.now())} Mail [ERROR] {message, str(object)}")
    
    def debug(self, message=None, object=None):
        print(f"{str(dt.datetime.now())} Mail [DEBUG] {message, str(object)}")

# creando la factory
class LoggerFactory(ABC):
    @abstractmethod
    def get_logger(self, type): ...  
    
# factory de los logger que tenemos
class LoggerFactoryImpl(LoggerFactory):
    def get_logger(self,type) -> Logger:
        try:
            options = {
                'c': LoggerConsola,
                'f': LoggerFile,
                'e': LoggerEmail
            }

            return options.get(type)()
        except Exception as e:
            print(f"Error al ingresar la opcion: {e}")
            raise e

def main() -> None:
    type_loger = str(input("""
    [c]Para salida por consola.
    [f]Para salida por archivo.
    [e]Para salida por email.
    Ingrese el tipo de logger que desea: """))
    logger = LoggerFactoryImpl().get_logger(type_loger)
    logger.info("Mensaje Generico para Info", "mensaje info")
    logger.warning("Mensaje Generico para Warning", "mensaje warning")
    logger.error("Mensaje Generico para Error", "mensaje error")
    logger.debug("Mensaje Generico para Debug", "mensaje debug")

if __name__ == '__main__':
    main()