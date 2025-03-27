from flask import Flask
from config import mysql,config
import bcrypt

class Usuario:

    def __init__(self,mysql):
        self.mysql = mysql
        pass

    @staticmethod 
    def agregarusuario(nombre,apellido,email,password):
        #generar hash contraseña
        conencriptada = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt()).decode('utf-8')

        #llamar la conexion
        con = mysql.connection.cursor()
        con.execute("INSERT INTO usuarios(nombre,apellido,email,password)VALUES(%s, %s, %s, %s)",
                    (nombre,apellido,email,conencriptada))
        mysql.connection.commit()
        con.close()