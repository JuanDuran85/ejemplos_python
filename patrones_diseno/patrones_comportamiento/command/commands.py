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
        print(f"{Fore.GREEN}[Writed] - {self.text_details}")
        
    def undo(self) -> None:
        self.text.delete_last_writed()
        print(f"{Fore.RED}[undid writed] - {self.text_details}")
        
    def redo(self) -> None:
        self.text.write_on(self.data)
        print(f"{Fore.BLUE}[redid writed] - {self.text_details}")
        
class DeleteBySpaces(Invoker):
    text: Text
    spaces: int
    
    # constructor
    def __init__(self, text: Text, spaces: str):
        self.text = text
        self.spaces = spaces

    @property
    def text_details(self) -> str:
        return f'{self.text.data_in_text}'
    
    def execute(self) -> None:
        self.text.delete_by_spaces(self.spaces)
        print(f"{Fore.GREEN}[Deleted] - {self.spaces} - {self.text_details}")
        
    def undo(self) -> None:
        self.text.return_spaces_deleted()
        print(f"{Fore.RED}[undid spaces deleted] - {self.spaces} - {self.text_details}")
        
    def redo(self) -> None:
        self.text.delete_by_spaces(self.spaces)
        print(f"{Fore.BLUE}[redid spaces deleted] - {self.spaces} - {self.text_details}")
        
class Short(Invoker):
    text: Text
        # constructor
        
    def __init__(self, text: Text, spaces: str):
        self.text = text

    @property
    def text_details(self) -> str:
        return f'{self.text.data_in_text}'
    
    def execute(self) -> None:
        self.text.short()
        print(f"{Fore.GREEN}[Short] - {self.text_details}")
        
    def undo(self) -> None:
        self.text.paste()
        print(f"{Fore.RED}[undid short] - {self.text_details}")
        
    def redo(self) -> None:
        self.text.short()
        print(f"{Fore.BLUE}[redid short] - {self.text_details}")
    
class Paste(Invoker):
    text: Text
    
    def __init__(self, text: Text, spaces: str):
        self.text = text

    @property
    def text_details(self) -> str:
        return f'{self.text.data_in_text}'
    
    def execute(self) -> None:
        self.text.paste()
        print(f"{Fore.GREEN}[Paste] - {self.text_details}")
        
    def undo(self) -> None:
        self.text.delete_last_writed()
        print(f"{Fore.RED}[undid paste] - {self.text_details}")
        
    def redo(self) -> None:
        self.text.paste()
        print(f"{Fore.BLUE}[redid paste] - {self.text_details}")
        
class Copy(Invoker):
    text: Text
    
    def __init__(self, text: Text, spaces: str):
        self.text = text

    @property
    def text_details(self) -> str:
        return f'{self.text.data_in_text}'
    
    def execute(self) -> None:
        self.text.copy()
        print(f"{Fore.GREEN}[Copy] - {self.text_details}")
        
    def undo(self) -> None:
        return super().undo()
        
    def redo(self) -> None:
        return super().redo()
    
class Batch(Invoker):
    commands: list
    
    def __init__(self, commands: list):
        self.commands = commands
        
    def execute(self) -> None:
        completed_commands: list = []
        try:
            for command in self.commands:
                command.execute()
                completed_commands.append(command)
        except ValueError:
            for command in reversed(completed_commands):
                command.undo()
            raise ValueError
        
    def undo(self) -> None:
        for command in reversed(self.commands):
            command.undo()
            
    def redo(self) -> None:
        for command in self.commands:
            command.redo()