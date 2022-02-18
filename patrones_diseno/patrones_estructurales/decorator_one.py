"""_summary_

Patron Decorator: mantiene una referencia al Component asociado. Implementa la interfaz de la super clase Component, delegando en el Component asociado. El Decorator, en general, añade comportamiento antes o después de un método que ya existe en el Component. Por ende, ofrece una alternativa cuando no es posible extender el comportamiento de un objecto a traves de la herencia.

"""
# ----------------------------------------------------------------------
# ejemplo de decorator basico
# ----------------------------------------------------------------------

def permisos(roles: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if 'client' in roles:
                print("Acceso permitido")
                return func(*args, **kwargs)
            
            print("Acceso denegado")
        return wrapper
    return decorator

# ----------------------------------------------------------------------
# funcion base para aplicar el decorator
# ----------------------------------------------------------------------
@permisos(['admin','super'])
def saludar():
    print("Hola desde funcion basica...")
    

if __name__ == '__main__':
    saludar()