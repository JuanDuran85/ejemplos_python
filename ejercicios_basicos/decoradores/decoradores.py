"""_summary_

    Decoradores
    - Un decorador recibe una funcion y retorna otra funcion. Se utiliza para extender     funcionalidades
    - Permite extender y modificar el comportamiento de una funcion. Recibe como parametro una funcion distinta y retorna otra funcion.

"""

# 1. Funcion como decorador (a)
# 2. Funcion a decorar (b)
# 3. Funcion decorada (c)


import time


def funcion_decorador_a(funcion_a_decorar_b):
    def funcion_decorada_c(*args, **kwargs):
        print("Hola soy la funcion decorada")
        resultado = funcion_a_decorar_b(*args, **kwargs)
        print("Adios soy la funcion decorada")
        return resultado

    return funcion_decorada_c

@funcion_decorador_a
def mostrar_mensaje():
    print("Hola desde funcion mostrar mensaje")
    
mostrar_mensaje()

@funcion_decorador_a
def sumar(a, b):
    return a + b

resultado = sumar(1, 2)
print(f'resultado suma: {resultado}')


# ---------------------------------------------------------------------------------------

# funcion decoradora
def upper_case(function_in):
    def envolt_function(*args: tuple, **kwargs: dict) -> str:
        original_result: str = function_in(*args, **kwargs)
        modify_result: str = original_result.upper()
        return modify_result
    return envolt_function


# decorador
@upper_case
# funcion a decorar
def function_to_decorate(text_in: str) -> str:
    return text_in

print(function_to_decorate('mensaje para decorar a mayusculas'))

# ---------------------------------------------------------------------------------------
# decoradores multiples

def negrita(function_in):
    def envolt_function(*args: tuple, **kwargs: dict) -> str:
        return f"<strong>{function_in(*args, **kwargs)}</strong>"
    return envolt_function

def enfatizar(function_in):
    def envolt_function(*args: tuple, **kwargs: dict) -> str:
        return f"<em>{function_in(*args, **kwargs)}</em>"
    return envolt_function

@negrita
@enfatizar
def mensaje() -> str:
    return "Mensaje con HTML"

print(mensaje())

# --------------------------------------------------------------------------------------
# decoradores, funciones con varios argumentos

def decorador_argumentos(function_in):
    def envolt_function(*args: tuple[str], **kwargs: dict) -> str:
        list_in: list = []
        for value in args:
            list_in.append(value.upper())  # type: ignore
        return function_in(*list_in, **kwargs)
    return envolt_function

@decorador_argumentos
def ejemplo_mensaje(titulo: str, nombre: str) -> str:
    return f"{titulo}. {nombre}"

print(ejemplo_mensaje("Sr", "Juan"))


# --------------------------------------------------------------------------------------
# decoradores con argumentos

def to_html(tag: str = "div"):
    def to_html_decorator(function_in):
        def envolt_function(*args: tuple, **kwargs: dict) -> str:
            return f"<{tag}>{function_in(*args, **kwargs)}</{tag}>"
        return envolt_function
    return to_html_decorator

@to_html('strong')
def mensaje_with_html(text_in: str) -> str:
    return text_in

print(mensaje_with_html('Mensaje con HTML'))



#----------------------------------------------------------------
# decoradores

def retry(exception, max_tries=5):
    def retry_decorator(func):
        def _wrapper(*args, **kwargs):
            tries = 0
            while True:
                try:
                    return func(*args, **kwargs)
                except exception as error:
                    tries += 1
                    if tries <= max_tries:
                        time.sleep(10)
                    else:
                        raise error
        return _wrapper
    return retry_decorator

@retry(Exception)
def may_fail():
    print("Ejecutando funcion fail")
    return mensaje_with_html("Nuevo mennsaje HTML")