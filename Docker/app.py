
from flask import Flask, render_template
from flask_mysqldb import MySQL
import os

#Creamos una instancia de la clase Flask.
app = Flask(__name__, template_folder='/app/templates')

#Los argumentos de "app.config" son variables por defecto del CLI de MYSQL.
#Cuando se importa la librearia "flask_mysqldb" esas 4 variables vienen con valores por defecto.
#Por ejemplo, el valor por defecto de MYSQL_HOST es "localhost". Si lo dejasemos asi podriamos conectar la aplicacion
#flask a la aplicacion MYSQL solo si ambas estuvieran en el mismo contenedor/maquina. 
#Aqui cada aplicacion corre en un contenedor distinto dentro de la misma red, entonces sobrescribimos el valor por
#defecto con "db01". En general cada contenedor tiene su propia dirección IP y su propia configuración de red. 
#Nuestros contenedores estan en la misma red por lo que la conexion se realiza a través de una conexión por socket y
#hay resolucion de nombres. Eso significa que la aplicación Python resolverá el nombre "db01" a una dirección IP.
#TCP 3306 es el puerto utilizado por defecto para la conexión al servidor de MySQL. Una conexión TCP se utiliza cuando 
#los contenedores están en redes separadas.
#Con 'os.environ.get' recuperamos el valor de las variables de entorno. Si estan establecidas el método devuelve sus
#valores, si no devuelve los valores predeterminados que se pasan como segundos argumentos.
app.config['MYSQL_USER'] = os.environ.get('MY_USER', 'flaskuser')
app.config['MYSQL_PASSWORD'] = os.environ.get('MY_PWD', 'patodegoma')
app.config['MYSQL_HOST'] = os.environ.get('MY_HOST', 'db01')
app.config['MYSQL_DB'] = os.environ.get('MY_DB', 'contador-db')
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

#Crea una instancia de la clase MySQL y la asocia con la aplicación Flask 'app'. La clase MySQL toma la instancia 
#de la aplicación Flask como argumento y la utiliza para configurar la conexión a la base de datos. La instancia mysql
#se puede utilizar para ejecutar consultas SQL y recuperar resultados de la base de datos.
mysql = MySQL(app)

UPDATE_COUNTER_QUERY = "UPDATE tabla_contador SET contador = contador + 1;"
SELECT_COUNTER_QUERY = "SELECT contador FROM tabla_contador;"
RESET_COUNTER_QUERY = "UPDATE tabla_contador SET contador = 0;"

@app.route('/reset')
def initialize():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute(RESET_COUNTER_QUERY)
        mysql.connection.commit()
    except Exception as e:
        return f"Error while resetting the counter: {e}"
    finally:
        cursor.close()
        
    message = "Counter reset to 0"
    return render_template('index.html', message=message)


@app.route('/')
def count():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute(UPDATE_COUNTER_QUERY)
        mysql.connection.commit()
        cursor.execute(SELECT_COUNTER_QUERY)
        result = cursor.fetchone()
    except Exception as e:
        return f"Error while fetching the counter: {e}"
    finally:
        cursor.close()

    message = "The number of visitors to this page is: " + str(result['contador'])
    return render_template('index.html', message=message)
