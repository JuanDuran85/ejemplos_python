# Python, DJango, Flask, PySide6, Tkinder, FastApi, Tornado, PySimpleGui

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

    ```bash window
    source entorno-virtual/Scripts/activate
    ```
    ```bash linux
    source entorno-virtual/bin/activate
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
- Para observar todos los paquetes instalados con pip
  ```bash
    pip list
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

## Servidor local con python
- Iniciar un servidor local con python desde la terminal
  ```bash
    python -m http.server 8000
  ```

## Generar documentacion por la terminar
- Utilizando pydoc
  ```bash
   pydoc ruta_archivo.py
  ```
- Para generar un HTML con pydoc
  ```bash
   pydoc -w ruta_archivo.py
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
- Para crear la carpeta de migraciones
  ```bash
  flask db init
  ```
- Para crear los archivos que representaran el modelo para ser migrado a la base de datos
  ```bash
  flask db migrate
  ```
- Para guardar los cambios en la base de datos una vez creado los archivos de migracion
  ```bash
  flask db upgrade
  ```
- Comando para verificar que todo este actualizado con respecto a las migraciones
  ```bash
  flask db stamp head
  ```

## Implementando FastAPI
- Para levantar el servidor
  ```bash
    uvicorn nombre_archivo:app --reload --port=8080
  ```

## Generando Ejecutable con pyinstaller
- Para generar el ejecutable
  ```bash
  pyinstaller --onefile --windowed --icon=icon.ico nombre_archivo.py
  ```
  En el caso de Mac o linux no usar --windowed

## Sentencias SQL
- Para obtener el nombre de la base de datos
  ```SQL
  select current_database();
  ```
- Para obtener la fecha y/o del sistema
  ```SQL
  select now()
  select timeofday()
  select current_time
  select current_date
  ```
- Para extraer un dia/mes/año de una fecha timestamp en una columna
  ```SQL
  select extract(day from timestamp)
  select extract(month from timestamp)
  select extract(quarter from timestamp)
  select age(timestamp)
  ```
- Para extraer la fecha o la hora del timestamp comviertiendo a caracter
  ```SQL
  select to_char(current_timestamp, 'HH:MM:SS')
  select to_char(current_timestamp, 'DD:MM:YYYY')
  ```
- Funciones para trabajar con caracteres
  ```SQL
  select length("NOMBRE") as "longitug" from abc # longitud de un campo
  ```
  ```SQL
  select lower("NOMBRE") from abc # convertir a minusculas
  ```
  ```SQL
  select left("NOMBRE",3) from abc # extrae los tres primeros caracteres de un campo
  ```
  ```SQL
  select "NOMBRE" || ' ' || "APELLIDO1" as "nombre_completo" from esquema."PERSONAS" # para concatenar dos campos
  ```
  ```SQL
  select char_length("nombre:columna"::varchar) as longitud from "nombre_tabla" # permite contar la cantidad de caracteres en un string
  ```
- Actualizar y retornar valor inmediatamente
  ```SQL
  update "nombre_tabla" set "nombre_columna" = 'valor' where "columna_x" = 'valor_x' returning "columna_y", "columna_x"
  ```
- Modificar propiedades de la table con alter
  ```SQL
  alter table "nombre_tabla" rename column "nombre_columna" to "nuevo_nombre" # modificar el nombre de una columna
  ```
  ```SQL
  alter table "nombre_tabla" alter column "nombre_columna" drop/set not null # modificar propiedad de una columna
  ```
  ```SQL
  alter table "nombre_tabla" drop column "nombre_columna" # eliminar columna
  ```
- Para eliminar una columna
  ```SQL
  alter table "nombre_tabla" drop column "nombre_columna"
  ```
- Para eliminar una tabla
  ```SQL
  drop table "nombre_tabla"
  ```
- Para eliminar una base de datos
  ```SQL
  drop database "nombre_base_datos"
  ```
- Se puede implementar case para una columna
  ```SQL
  select "columna_x", case when "columna_x" = 'valor_x' then 'valor' when "columna_x" = "valor_y" then "valor" else 'valor_z' end as "nuevo_nombre" from "nombre_tabla"
  ```
