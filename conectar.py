from config import config
import mysql.connector


def conectar():
    conexion = None
    try:
        params = config()
        print("Estableciendo conexión con la Base de Datos")
        conexion = mysql.connector.connect(**params)

        conexion.autocommit = True

        cursor = conexion.cursor()
        cursor.execute("show tables;")
        datos = cursor.fetchall()
        print(datos)
        cursor.close()

    except (Exception, mysql.connector.Error) as error:
        print(error)

    else:
        print("Conexión exitosa a la Base de Datos")

    finally:
        if conexion is not None:
            return conexion

print(conectar())