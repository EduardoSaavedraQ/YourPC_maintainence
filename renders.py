from flask import Flask, render_template, url_for, request, redirect
from flask_login import LoginManager, UserMixin, login_user, logout_user
import psycopg2
from conectar import conectar

app = Flask(__name__)
app.secret_key = 'una clave secreta muy segura'
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)



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


""" @app.route("/LogIn", methods=['POST'])
def LogIn():
    correo = request.form.get("email")
    contrasenia = request.form.get("pwd")

    no_match = "El correo y/o la contraseña son incorrectos"
    retorno = "startPage.html"

    try:
        conn = conectar()
        cur = conn.cursor()
        print(correo)
        print(contrasenia)
        cur.execute(
            "SELECT correo, contrasenia FROM usuario WHERE correo = '%s' AND contrasenia = '%s';",(correo, contrasenia))
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

 """

""" @app.route('/LogIn', methods=['POST'])
def LogIn():
    correo = request.form.get("email")
    contrasenia = request.form.get("pwd")

    no_match = "El correo y/o la contraseña son incorrectos"

    try:
        conn = conectar()
        cur = conn.cursor()

        cur.execute(f"SELECT * FROM usuario WHERE correo = '{correo}';")
        res = cur.fetchone()

        if res is None:
            raise Exception(no_match)

        print(res)
        id = res[0]
        user = User(id)
        login_user(user)
                
        return redirect(url_for('yourPCHome'))
        #return render_template('yourPCHome.html', url_for=url_for)
        
    except(psycopg2.DatabaseError, Exception) as error:
        if error is no_match:
            p = 1
    
    finally:
        cur.close()
        conn.close() """

@app.route("/LogIn", methods=['POST'])
def LogIn():
    correo = request.form.get("email")

    no_match = "El correo y/o la contraseña son incorrectos"

    try:
        conn = conectar()
        cur = conn.cursor()

        cur.execute(f"SELECT * FROM usuario WHERE correo = '{correo}';")
        res = cur.fetchone()

        if res is None:
            raise Exception(no_match)

        id = res[0]
        user = User(id)
        login_user(user)
                
        return redirect(url_for('yourPCHome'))
        #return render_template('yourPCHome.html', url_for=url_for)
        
    except(psycopg2.DatabaseError, Exception) as error:
        if error is no_match:
            p = 1
    
    finally:
        cur.close()
        conn.close()

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('yourPCHome'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)