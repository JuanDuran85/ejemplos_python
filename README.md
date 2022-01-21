# Python, DJango, Flask, PySide6, Tkinder

Ejemplos de programacion con Python

## Entorno Virtual para Python

- se instala el entorno virtual

    ```bash
    pip install virtualenv
    ```

- se configura el entorno virtual con el nombre

    ```bash
    python -m venv nombre_e_v
    ```

- se ejecuta el entorno virtual

    ```bash
    source entorno-virtual/Scripts/activate
    ```

- luego se selecciona el entorno virtual creado

## Instalacion de requirements
- Para instalar las librerias
    ```bash
    pip install -r requirements.txt
    ```
- Para generar el archivo de requirements
    ```bash
    pip freeze > requirements.txt
    ```

## Usando servidor local para json
- Instalacion de json-server
  ```bash
   npm install -g json-server
  ```
- Levanando el servidor local. Crear archivo json con el nombre db
  ```bash
  json-server db.json
  ```

## Creando proyectos con Django
- Iniciando el proyecto
  ```bash
  django-admin startproject nombre_proyecto
  ```
- Ejecutar ek proyecto o levantar el servicio o servidor de desarrollo
  ```bash
  python3 manage.py runserver number_port_to_run
  ```
- Crear una nueva aplicacion dentre de la eistente
  ```bash
  python3 manage.py startapp nombre_app
  ```
- Para mostrar las migraciones pendientes
  ```bash
  python3 manage.py showmigrations
  ```
- Para ejecutar las migraciones de manera automatica
  ```bash
  python3 manage.py migrate
  ```
- Para ejecutar las migraciones pendientes
  ```bash
  python3 manage.py makemigrations
  ```
- Para ejeuctar la migracion con la sentencia SQL
  ```bash
  python3 manage.py sqlmigrate nombre_app nombre_migracion
  ```
- Par crear usuarios del paqueta de admin
  ```bash
  python3 manage.py createsuperuser
  ```

## Implementando Flask
- Para levantar el servidor en modo de produccion
  ```bash
  flask run
  ```
- Para especificar el nombre del archivo de inicio, si ya es app.py se puede omitir el comando
  ```bash
  export FLASK_APP=app 
  ```
  ```cmd
  set FLASK_APP=app
  ```
  ```powershell
  $env:FLASK_APP = "app"
  ```
- Para configurar el servicio en modo de desarrollo
  ```bash
  export FLASK_ENV=development
  ```
  ```cmd
  set FLASK_ENV=development
  ```
  ```powershell
  $env:FLASK_ENV = "development"
  ```
- Generar llaves de manera segura
  ```bash
  python3 -c 'import secrets; print(secrets.token_hex())'
  ```