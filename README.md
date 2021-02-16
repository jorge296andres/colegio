`pip install -r requirements.txt`

_en caso de no utilizar docker omitir este paso y cambiar los parametros de configuración en la variable DATABASES ubicada en colegio/settings_

`docker run --rm -d -p 3306:3306 --name basedatos -e MYSQL_USER=root -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=mysql mysql:latest`

`python manage.py makemigrations empleados grados roles`

`python manage.py migrate`

`python manage.py test -v 2`

`python manage.py runserver`

# Acceso Base de datos desde el CMD con Docker

`docker exec -it basedatos mysql -p`

`root`

`show databases;`

`USE mysql;`

`show tables;`
