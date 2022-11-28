from app_module import db

class Product(db.Model):  # type: ignore
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, db_index=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Float)
    
    def __init__(self,name,price):
        self.name = name
        self.price = price
        
    
    def __str__(self):
        return (
            f'Id: {self.id}, '
            f'Nombre: {self.name}, ' 
            f'Apellido: {self.price}, '
        )
        
    def __repr__(self):
        return f"<Product {self.name}>"