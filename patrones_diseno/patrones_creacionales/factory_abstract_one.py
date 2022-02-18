"""_summary_

Abstract Factory

El propósito de Abstract Factory es proporcionar una interfaz para crear familias de objetos relacionados, sin especificar clases concretas. Normalmente, el cliente crea una implementación concreta de la fábrica abstracta y luego utiliza la interfaz genérica de la misma para crear los objetos concretos.

Son factorias abstractas o factorias de otras factorias. Crea factorias de otras factorias.

"""

from abc import ABC, abstractmethod

# -------------------------------------------------
# Clases abstractas
# -------------------------------------------------  
class CloudStorage(ABC):
    @abstractmethod
    def show(self) -> str: ...
    
class Mail(ABC):
    @abstractmethod
    def show(self) -> str: ...
    
# ------------------------------------------------- 
# clases especificas en relacion con las clases abstractas   
# ------------------------------------------------- 
class GoogleCloudStorage(CloudStorage):
    def show(self) -> str:
        return "Google Cloud Storage... Show"
    
class MicrosoftCloudStorage(CloudStorage):
    def show(self) -> str:
        return "Microsoft Cloud Storage... Show"
    
class GoogleMail(Mail):
    def show(self) -> str:
        return "Google Mail... Show"
    
class MicrosoftMail(Mail):
    def show(self) -> str:
        return "Microsoft Mail... Show"
    
# --------------------------------------------------
# Factorias abstractas
# --------------------------------------------------

class AbstractFactory(ABC):
    @abstractmethod
    def create_cloud_storage(self) -> CloudStorage: ...
    
    @abstractmethod
    def create_mail(self) -> Mail: ...
    
# --------------------------------------------------
# Factorias normales para cada ente dependientes de la fabrica abstracta
# --------------------------------------------------

class GoogleFactory(AbstractFactory):
    
    def create_cloud_storage(self) -> CloudStorage:
        return GoogleCloudStorage()
    
    def create_mail(self) -> Mail:
        return GoogleMail()
    
class MicrosoftFactory(AbstractFactory):
    def create_cloud_storage(self) -> CloudStorage:
        return MicrosoftCloudStorage()
    
    def create_mail(self) -> Mail:
        return MicrosoftMail()