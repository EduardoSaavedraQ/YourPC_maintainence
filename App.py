from flask import Flask, render_template, url_for, request, redirect
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
from conectar import conectar

app = Flask(__name__)
app.secret_key = 'una clave secreta muy segura'
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, id, is_admin=False):
        self.id = id
        self.is_admin = is_admin

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)



@app.route('/')
def yourPCHome():
    return render_template("yourPCHome.html")

@app.route('/signUp')
def signUp():
    return render_template("signUp.html",url_for=url_for)

@app.route('/logIn')
def logIn():
    return render_template("logIn.html",url_for=url_for)

@app.route('/startPage')
def startPage():
    return render_template("startPage.html",url_for=url_for)

@app.route('/addPCPage')
def addPCPage():
    return render_template("addPC.html", url_for=url_for)

@app.route('/createAdminUser')
def createAdminUserPage():
    return render_template("createAdminUser.html", url_for=url_for)

@app.route('/SignUp', methods=['POST'])
def SignUp():

    user_id = request.form['nombre']
    email = request.form['correo']
    pwd = request.form['pwd']
    length_pwd = len(pwd)

    #Comprueba la longitud de la contraseña
    if length_pwd < 5 or len(pwd) > 15:
        return render_template("signUp.html", error_pwd=True)
    # Verifica si el usuario o el correo ya existen en la base de datos
    try:
        conn = conectar()
        cur = conn.cursor()

        cur.execute("SELECT pk_nickname, correo FROM usuarios WHERE UPPER(pk_nickname) = %s OR UPPER(correo) = %s;", (user_id.upper(), email.upper()))

        res = cur.fetchone()

        if res is None:
            hashed_pwd = generate_password_hash(pwd) #Default method="pbkdf2:sha1", alternativa method="pbkdf2:sha512"
            cur.execute(f"INSERT INTO usuarios(pk_nickname, correo, contrasenia) VALUES('{user_id}', '{email}', '{hashed_pwd}');")
            user = User(user_id)
            login_user(user)
            return redirect(url_for('yourPCHome'))

        return render_template("signUp.html", repited_account=True)
    except(mysql.connector.Error) as error:
        print(error)

    finally:
        if cur is not None:
            cur.close()
            conn.close()

@app.route("/LogIn", methods=['POST'])
def LogIn():
    correo = request.form['email']
    pwd = request.form['pwd']

    try:
        conn = conectar()
        cur = conn.cursor()

        cur.execute(f"SELECT pk_nickname, correo, contrasenia, admin FROM usuarios WHERE correo = '{correo}';")
        res = cur.fetchone()

        if res is None or check_password_hash(res[2], pwd) is False:
            return render_template("logIn.html", error=True)

        id = res[0]
        user = User(id, bool(res[3]))
        login_user(user)
        return render_template("yourPCHome.html")

    except(mysql.connector.Error) as error:
        print(error)

    finally:
        if cur is not None:
            cur.close()
            conn.close()

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('yourPCHome'))

if __name__ == '__main__':
    app.run(debug=True)