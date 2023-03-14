
<h2>WHAT'S NEW?</h2>
<h4>FLASK COUNTER MYSQL PYTHON APPLICATION</h4>

1. Uso de un solo cursor en vez de dos. 
2. Uso de un cursor ***'DictCursor'*** en lugar de un cursor normal. Esto permite recuperar los resultados de la base  
  de datos como objetos de diccionario en lugar de tuplas, lo que puede ser más fácil de trabajar. 
3. Separación del codigo html del codigo python usando un template. 
4. Valores por defecto para todas las variables de entorno. 
5. Declaración de las consultas SQL como constantes para una mejor organización y mantenibilidad. 
6. Uso de la función ***fetchone()*** en lugar de ***fetchall()*** para recuperar solo un registro en lugar de todos los registros. 
7. Gestion de excepciones y cierre de cursores en los bloques ***'try-except-finally'***. 
8. Multistage para la creación de la imagen obteniendo un tamaño de 83 MB contra los 400 MB sin multistage. 

<h2>CONFIGURABLE VARIABLES</h2>

Todas las variables en los ficheros ***'env-app'*** y ***'env-db'*** son configurables, menos las variable ***'MY_HOST'***.
Si se modifica el valor de ***'MYSQL_DATABASE'*** en el fichero ***'env-db'*** se tiene que modificar tambien ***'MY_DB'*** en ***'env-app'*** y viceversa.

<h2>TRY THE APPLICATION LOCALLY</h2>

    cd /path_to_the_repository/DockerK8s-Paolo/Docker/  
    docker compose up 
    http://localhost:5500 
    http://localhost:5500/reset 
