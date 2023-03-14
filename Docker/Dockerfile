

FROM python:3.7-alpine as compile

RUN apk add gcc musl-dev mysql-client mysql-dev 

WORKDIR /app

COPY requirements.txt ./

#Flask es un framework web que se utiliza comúnmente con Python para crear aplicaciones web.
#Para utilizar Flask en esta imagen de Python instalamos Flask y sus dependencias en el contenedor.
#'pip install' instala las dependencias en el directorio "/install".
RUN pip install --prefix=/install -r requirements.txt

FROM python:3.7-alpine as final

RUN apk add mysql-dev 

#Copio desde el stage 'compile' el directorio '/install' al directorio '/usr/local' del contenedor.
COPY --from=compile /install /usr/local 

#El directorio /app será creado dentro del contenedor, y cualquier instrucción que se ejecute después de WORKDIR /app 
#se ejecutará en este directorio.
WORKDIR /app

#Copiamos tambien 'requirements.txt' para tener un registro de las dependencias utilizadas en la aplicación.
COPY Dockerfile app.py requirements.txt ./
COPY templates/ .//templates/

#Indicamos que el archivo "app.py" es el archivo principal de la aplicación Flask dentro del contenedor, y Flask 
#lo utilizará como tal para servir la aplicación.
ENV FLASK_APP=app.py
#Se especifica que la aplicación está disponible para solicitudes externas.
ENV FLASK_RUN_HOST=0.0.0.0

#Es buena práctica definir valores predeterminados tanto en la aplicación como en el Dockerfile.
ENV FLASK_ENV=development
ENV MY_USER=flaskuser
ENV MY_PWD=patodegoma
ENV MY_HOST=db01
ENV MY_DB=contador-db

CMD ["flask", "run"]