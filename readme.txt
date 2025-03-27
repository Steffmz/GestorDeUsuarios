install: pip install bcrypt
         pip install mysql-connector
         pip install mysql-connector-python

Prender : python app.py y la ruta es /test_db

Hay un error y es que en la base de datos de nosotros hay columnas que terminan en usu
por ejemplo nombreusu y hay que cambiar el nombre de las columnas a solo nombre y asi con las demas
este es la query :

ALTER TABLE usuarios 
CHANGE COLUMN idusuarios id INT(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE usuarios 
CHANGE COLUMN nombreusu nombre VARCHAR(100) NOT NULL;

ALTER TABLE usuarios 
CHANGE COLUMN passwordusu password VARCHAR(100) NOT NULL;

ALTER TABLE usuarios
ADD COLUMN apellido VARCHAR(100) NOT NULL AFTER nombre; 

ALTER TABLE usuarios
CHANGE COLUMN emailusu email VARCHAR(100) NOT NULL;