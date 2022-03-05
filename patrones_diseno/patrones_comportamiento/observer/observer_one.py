"""_summary_

    Patron de diseño: Observer

"""

from abc import ABC, abstractmethod
class Observer(ABC):
    @abstractmethod
    def update(self): ...
class Obervable(ABC):    
    @abstractmethod
    def attach(self, observer: Observer) -> None: ...
    
    @abstractmethod
    def detach(self, observer: Observer) -> None: ...
    
    @abstractmethod
    def notify(self) -> None: ...
    
class YouTubeChannel(Obervable):
    
    __channel_suscriber: list = []
    __last_video_posted: str = ""
    
    def attach(self, observer: Observer) -> None:
        self.__channel_suscriber.append(observer)
        
    def detach(self, observer: Observer) -> None:
        self.__channel_suscriber.remove(observer)
        
    def notify(self) -> None:
        for suscriber in self.__channel_suscriber:
            suscriber.update()
    
    def add_new_video(self,title: str) -> None:
        self.__last_video_posted = title
        self.notify()
        print(f"Nuevo video Agregado al canal")
            
    @property
    def last_video_posted(self) -> str:
        return self.__last_video_posted
    
class Suscriptor(Observer):
    
    def __init__(self,observable: YouTubeChannel):
        self.observable = observable
        
          
    def update(self) -> None:
        print(f"Nuevo video")
        print(f"{self.observable.last_video_posted}")
    

if __name__ == '__main__':
    canal = YouTubeChannel()
    sus1 = Suscriptor(canal)
    sus2 = Suscriptor(canal)
    
    canal.attach(sus1)
    canal.attach(sus2)
    
    canal.add_new_video("Video de Python")
    canal.add_new_video("Video de Django")
    