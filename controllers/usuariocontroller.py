from flask import render_template, request, redirect, url_for
from models.usuario import Usuario

class Usuariocontroller:
    def __init__(self,mysql):
        self.mysql = mysql

        #recibir lo que viene de la lista agregar usuario.html
    def agregar_usuario(self):
        if request.method == "POST":
            nombre = request.form["txtnombre"]
            apellido = request.form["txtapellido"]
            email = request.form["txtemail"]
            password = request.form["txtpassword"]

            #llamar el modelo para agregar el usuario

            Usuario.agregarusuario(nombre,apellido,email,password)

            return redirect(url_for("formulario_registro"))
    #muestra el formulario
    def formulario_registro(self):
            return render_template("agregar_usuario.html")