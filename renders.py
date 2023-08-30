from flask import Flask, render_template, url_for,request
import psycopg2
from conectar import conectar

app = Flask(__name__)


@app.route('/')
def yourPCHome():
    return render_template("yourPCHome.html", url_for=url_for)

@app.route('/formulario')
def formulario():
    return render_template("formulario.html",url_for=url_for)

@app.route('/logIn')
def logIn():
    return render_template("logIn.html",url_for=url_for)

@app.route('/startPage')
def startPage():
    return render_template("startPage.html",url_for=url_for)

@app.route('/SignIn', methods=['POST'])
def SignIn():
    nombreUsua = request.form['nombre']
    correoUsua = request.form['correo']
    contrasenia = request.form['contrasenia']

    conn = conectar()
    cur = conn.cursor()
    cur.execute("INSERT INTO usuario VALUES (%s, %s, %s);",(nombreUsua,correoUsua,contrasenia))

    return render_template("startPage.html")


@app.route("/LogIn", methods=['POST'])
def LogIn():
    correo = request.form.get("correo")
    contrasenia = request.form.get("contrasenia")

    no_match = "El correo y/o la contraseña son incorrectos"
    retorno = "startPage.html"

    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute(
            "SELECT correo, contrasenia FROM usuario WHERE correo = %s AND contrasenia = %s;",(correo, contrasenia))
        r = cur.fetchall()
        if len(r) == 0:
            raise Exception(no_match)
        
        retorno="startPage.html"

    except (psycopg2.DatabaseError, Exception) as error:
        if str(error) == no_match:
            retorno = "logIn.html"
        print(error)
    finally:
        cur.close()
        conn.close()
        return render_template(retorno)


if __name__ == '__main__':
    app.run(debug=True)
