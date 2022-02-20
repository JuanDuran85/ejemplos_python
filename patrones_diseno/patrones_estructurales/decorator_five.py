''' 
Patron decorador
'''
from abc import ABC, abstractmethod

class Enemy(ABC):
    @abstractmethod
    def compute_damage(self, recive_atack: str) -> int: ...

class EnemyDecorator(Enemy):
    decorator_enemy: Enemy
    
    def __init__(self,enemy_to_decorate: Enemy):
        self.decorator_enemy = enemy_to_decorate
        
    def compute_damage(self, recive_attack: str) -> int: ...
    

def helement_decorator(cls):
    def wrapper(*args, **kwargs):
        def new_compute_damage(self, recive_attack: str) -> int:
            if recive_attack == 'Daño a la cabeza':
                print("Tengo casco... daño 0")
                return 0
            print("Daño fuera de la cabeza, 100 de daño")
            return 100
        setattr(cls, 'compute_damage', new_compute_damage)
        return cls(*args, **kwargs)
    return wrapper

def armor_decorator(cls):
    def wrapper(*args, **kwargs):
        def new_compute_damage(self, recive_attack: str) ->int:
            if recive_attack == "Daño al cuerpo":
                print("Tengo armadura, daño 0")
                return 0
            print("Daño fuera de la armadura, 100 de daño")
            return 100
        setattr(cls, 'compute_damage', new_compute_damage)
        return cls(*args, **kwargs)
    return wrapper

def set_items(items: list):
    def decorator(cls):
        def wrapper(*args, **kwargs):
            def new_compute_damage(self, recive_attack: str) -> int:
                if recive_attack in items:
                    print("Daño 0")
                    return 0
                print("Daño 100")
                return 100
            setattr(cls, 'compute_damage', new_compute_damage)
            return cls(*args, **kwargs)
        return wrapper
    return decorator

def choice_decorator() -> list:
    choosing: bool = True
    list_items: list = []
    
    while choosing:    
        insert_user = int(input(""" Con que desea equipar al enemigo?
[1] Usar Casco
[2] Usar Armadura
[3] Usar Pantalones
[4] Atacar al enemigo
    >>>: """))
        equipamiento = {
            1: 'Daño a la cabeza',
            2: 'Daño al cuerpo',
            3: 'Daño a las piernas',
        }
        
        if insert_user != 4:
            list_items.append(equipamiento.get(insert_user))
        else:
            choosing = False
            return list_items

def tipo_de_ataque() -> str:
    try:
        insert_ataque = int(input("""
    [1]. Ataque a la cabeza
    [2]. Ataque al cuerpo
    [3]. Ataque a las piernas    
    >>>: """))
        ataques = {
            1: 'Daño a la cabeza',
            2: 'Daño al cuerpo',
            3: 'Daño a las piernas'
        }
        if ataques.get(insert_ataque):
             return ataques.get(insert_ataque)
    except Exception:
        print('No se ha ingresado un ataque valido...')

@set_items(choice_decorator())
class ConcreteEnemy(Enemy):
    def compute_damage(self, recive_attack: str) -> int:
        print('Enemigo desduno, daño de 100 puntos...')
        return 100

def main() -> None:
    enemigo_concreto = ConcreteEnemy()
    enemigo_concreto.compute_damage(tipo_de_ataque())
    
if __name__ == "__main__":
    main()