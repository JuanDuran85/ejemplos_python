from abc import ABC, abstractmethod

class Invoker(ABC):
    
    # metodos abstractos
    @abstractmethod
    def execute(self) -> None: ...
    
    @abstractmethod
    def undo(self) -> None: ...
    
    @abstractmethod
    def redo(self) -> None: ...