"""_summary_

  El patron strategy permite encapsular una serie de algoritmos para que pueden ser intercambiables

"""

from abc import ABC, abstractmethod
import datetime

class PriceStrategy(ABC):
    
    @abstractmethod
    def compute_price(self, amount: int or float) -> float: ...
    
class CardPrice(PriceStrategy):
    
    __interes_present: float = 0.1
    
    def compute_price(self, amount: int or float) -> float:
        return amount + amount * self.__interes_present
    
class CashPrice(PriceStrategy):
    
    __discount_present: float = 0.15
    
    def compute_price(self, amount: int or float) -> float:
        return amount - amount * self.__discount_present
    
class ClientPrice(PriceStrategy):
    
    __discount_present: float = 0.25
    
    def compute_price(self, amount: int or float) -> float:
        return amount - amount * self.__discount_present
    
class DaysDiscount(PriceStrategy):
    
    __days_discount: list = [2,4,6]
    __discount_present: float = 0.15

    def compute_price(self, amount: int or float) -> float:
        if (datetime.datetime.today().day+1) in self.__days_discount:
            return amount - amount * self.__discount_present
        return amount
        
        
def set_strategy(option: int) -> PriceStrategy:
    
    strategies = {
        1: CashPrice(),
        2: CardPrice(),
        3: ClientPrice(),
        4: DaysDiscount()
    }
    
    return strategies[option]

if __name__ == '__main__':
    strategy = int(input("""
[1] - Precio en efectivo
[2] - Precio con tarjeta
[3] - Precio para clinete recurrente
[4] - Descuento del dia
>>>: """))
    
    amount: float or int = float(input("Ingrese el monto total sin descuento: "))
    total: float = set_strategy(strategy).compute_price(amount)
    print(f"El monto total es: {total}")
    
    