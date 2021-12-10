# ejemplos_python

Ejemplos de programacion con Python

# Entorno Virtual para Python

- se instala el entorno virtual

    ```
    pip install virtualenv
    ```

- se configura el entorno virtual con el nombre

    ```
    python -m venv nombre_e_v
    ```

- se ejecuta el entorno virtual

    ```
        source entorno-virtual/Scripts/activate
    ```

- luego se selecciona el entorno virtual creado

# Instalacion de requirements
- Para instalar las librerias
    ```
        pip install -r requirements.txt
    ```
- Para generar el archivo de requirements
    ```
        pip freeze > requirements.txt
    ```

# Usando servidor local para json
- Instalacion de json-server
  ```
    npm install -g json-server
  ```
- Levanando el servidor local. Crear archivo json con el nombre db
  ```
    json-server db.json
  ```