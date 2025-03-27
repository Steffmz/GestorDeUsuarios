from flask import Flask
from config import mysql,config

app= Flask(__name__)
app.config.from_object(config)
mysql.init_app(app)

@app.route("/test_db")

def test_db():

    obj = mysql.connection.cursor()
    obj.execute("SELECT VERSION()")
    db_version= obj.fetchone()
    obj.close()
    return f"conexion exitosa version:{db_version[0]}"

if __name__ == "__main__":
    app.run(debug=True)
