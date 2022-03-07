class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria
        
    def __str__(self):
        return f'{self.nombre} - {self.telefono} - {self.categoria}'