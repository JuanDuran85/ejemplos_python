"""_summary_

Abstract Factory: Son factorias abstractas o factorias de otras factorias. Crea factorias de otras factorias.

"""

from abc import ABC, abstractmethod

# -------------------------------------------------
# Clases abstractas
# -------------------------------------------------  
    
class Background(ABC):
    @abstractmethod
    def create_background(self) -> str: ...

class DarkBackground(Background):
    def create_background(self) -> str:
        return "Dark Background para APP"

class LightBackground(Background):
    def create_background(self) -> str:
        return "Light Background para APP"

# ------------------------------------------------- 
#  
# ------------------------------------------------- 

class AbstractFactory(ABC):
    @abstractmethod
    def create_background(self) -> Background: ...
    
    @abstractmethod
    def create_side_bar(self) -> str: ...
    
    @abstractmethod
    def create_nav_bar(self) -> str: ...
    
# ------------------------------------------------- 
#    Factorias
# ------------------------------------------------- 

class DarkThemeFactory(AbstractFactory):
    
    def create_background(self) -> DarkBackground:
        return DarkBackground()
    
    def create_side_bar(self) -> str:
        return "Dark SideBar de la APP"
    
    def create_nav_bar(self) -> str:
        return "Dark NavBar de la APP" 


class LightThemeFactory(AbstractFactory):
    
    def create_background(self) -> LightBackground:
        return LightBackground()
    
    def create_side_bar(self) -> str:
        return "Light SideBar de la APP"
    
    def create_nav_bar(self) -> str:
        return "Light NavBar de la APP"

