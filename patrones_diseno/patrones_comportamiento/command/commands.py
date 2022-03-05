from invoker import Invoker
from text import Text
from colorama import init, Fore

init(autoreset=True)

class Write(Invoker):
    # atributos
    data: str
    text: Text
    
    # constructor
    def __init__(self, text: Text, data: str):
        self.text = text
        self.data = data

    @property
    def text_details(self) -> str:
        return f'{self.text.data_in_text}'
    
    def execute(self) -> None:
        self.text.write_on(self.data)
        print(f"{Fore.GREEN}[Writed] - {self.data} - {self.text_details}")
        
    def undo(self) -> None:
        self.text.delete_last_writed()
        print(f"{Fore.RED}[undid writed] - {self.data} - {self.text_details}")
        
    def redo(self) -> None:
        self.text.write_on(self.data)
        print(f"{Fore.BLUE}[redid writed] - {self.data} - {self.text_details}")