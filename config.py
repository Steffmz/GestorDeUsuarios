from flask_mysqldb import MySQL

class config:
    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = ""
    MYSQL_DB = "gestor_usuarios"
    #MYSQL_PORT = 3307

mysql = MySQL()

