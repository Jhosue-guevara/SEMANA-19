sistema pqeueño de inventario usando django 

Entorno Virtual
Instalación de librerías necesarias dentro del entorno virtual

pip install -r requirements.txt
Restaurar la Base de Datos
Asegúrate de tener PostgreSQL instalado en tu máquina.
Crea una nueva base de datos en PostgreSQL.
Desde la terminal, ejecuta el siguiente comando para restaurar la base de datos:
psql -U tu_usuario -h localhost -d nombre_de_tu_base_de_datos < Database/dump.sql
Realiza la conexión a la bd utilizando PostreSql, modificando el string de conexión que se encuentra en el archivo de “settings.py”
Uso
Corre la aplicación

python manage.py runserver
Puede ingresar a las paginas creando un superusuario o creando una cuenta en "registro/"

Desarrolladores

Edwin Alexander Villalta Ortiz SMSS022022
Cindy Johana Valencia Flores SMSS042422
Angel Josue Guevara Portillo SMSS015622
