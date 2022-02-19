"""[sumary] 
    Aplicando Patron Decorator con clases abstractas
"""

# ejemplo de patron decorador con juego

from abc import ABC, abstractmethod

# clase abstracta base
class Enemy(ABC):
    @abstractmethod
    def compute_damage(self, recive_attack: str) -> int: ...
       
# clase para enemigo generico   
class ConcreteEnemy(Enemy):
    def compute_damage(self, recive_attack: str) -> int:
        print('Daño de 100 puntos...')
        return 100
    
# clase para decorar enemigo
class EnemyDecorator(Enemy):
    decorated_enemy: Enemy
    
    def __init__(self, enemy_to_decorate: Enemy):
        self.decorated_enemy = enemy_to_decorate

    def compute_damage(self, recive_attack: str) -> int: ...
    
# clase para armaduras como decoradores
class ElementDecorator(EnemyDecorator):
    
    def compute_damage(self, recive_attack: str) -> int:
        if recive_attack == 'Daño a la cabeza':
            print('Llevo casco no me haces daño...')
            return 0
        print('100 puntos de daño...')
        return 100
    
# funcion con el tipo de daño al enemigo
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

def main() -> None:
    enemigo_desnudo = ConcreteEnemy()
    enemigo_con_casco = ElementDecorator(enemigo_desnudo)
    enemigo_con_casco.compute_damage(tipo_de_ataque())
    
if __name__ == "__main__":
    main()