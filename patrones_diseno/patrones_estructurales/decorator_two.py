"""_summary_

Aplicando Patron Decorator con clases abstractas

"""

from abc import ABC, abstractmethod

# -----------------------------------------------------------------------------------------------
# ejemplo de decorator para agregar funcionalidades de negrita y subrayar a una escritura simple.
# -----------------------------------------------------------------------------------------------

# clase abstracta base
class Text(ABC):
    @abstractmethod
    def write_text(self): ...

# clase de texto base o inicio de escritura sin decorador
class BaseText(Text):
    def write_text(self, texto):
        print(f"excribiendo texto: {texto}")

# clase para decordar de forma generica
class TextDecorator(Text):
    __decorated_text: Text
    
    def __init__(self, decorated_text: Text):
        self.__decorated_text = decorated_text

    def write_text(self, texto):
        self.__decorated_text.write_text(texto)


# clases para decorar de forma especifica
class BoldTextDecorator(TextDecorator):
    
    def boldTextDecorator(self, decorated_text: Text):
        return super().__decorated_text
    
    def write_text(self, texto):
        print(f"Agregando negrita al <b>{texto}</b>")
        return super().write_text(texto)
    
class UnderlineTextDecorator(TextDecorator):
    
    def underlineTextDecorator(self, decorated_text: Text):
        return super().__decorated_text
    
    def write_text(self, texto):
        print(f"Agregando subrayado al <u>{texto}</u>")
        return super().write_text(texto)
texto_ejemplo = "Texto base ingresado"    
base_text = BaseText()
base_text.write_text(f"{texto_ejemplo}")
bold_text = BoldTextDecorator(base_text)
bold_text.write_text(f"{texto_ejemplo}")
underline_text = UnderlineTextDecorator(base_text)
underline_text.write_text(f"{texto_ejemplo}")
underline_text = UnderlineTextDecorator(bold_text)
underline_text.write_text(f"{texto_ejemplo}")
    