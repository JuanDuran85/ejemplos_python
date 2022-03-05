class Text:
    
    # atributos
    data_in_text: str = ""
    data_cache: str = ""
    spaces_to_delete: int
    pointers: list = [0]
    current_pointers: int = 0
    
    # metodos
    def write_on(self, data: str) -> str:
        self.pointers.append(len(self.data_in_text))
        self.current_pointers += 1
        self.data_in_text += data
        self.data_cache = self.data_in_text
        return self.data_in_text
    
    def delete_last_writed(self) -> str:
        self.data_in_text = self.data_in_text[0:self.pointers[self.current_pointers]]
        self.current_pointers -= 1
        self.pointers.pop()
        return self.data_in_text
    
    def delete_by_spaces(self, spaces: int) -> str:
        self.pointers.append(len(self.data_in_text))
        self.current_pointers += 1
        self.data_in_text = self.data_in_text[0:self.pointers[self.current_pointers]]
        return self.data_in_text
    
    def return_spaces_deleted(self) -> str:
        self.data_in_text = self.data_cache[0:self.pointers_self.current_pointers]
        self.pointers.pop()
        self.current_pointers -= 1
        return self.data_in_text
    
    def copy(self) -> None:
        self.data_cache = self.data_in_text
        
    def short(self) -> None:
        self.copy()
        self.data_in_text = ''
        
    def paste(self) -> str:
        self.pointers.append(len(self.data_in_text))
        self.current_pointers += 1
        self.data_in_text += self.data_cache
        return self.data_in_text
        