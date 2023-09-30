from flask import Flask, render_template, url_for, request, redirect
from flask_login import LoginManager, UserMixin, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
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

@app.route('/signUp')
def signUp():
    return render_template("signUP.html",url_for=url_for)

@app.route('/logIn')
def logIn():
    return render_template("logIn.html",url_for=url_for)

@app.route('/startPage')
def startPage():
    return render_template("startPage.html",url_for=url_for)

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

        cur.execute("SELECT pk_nickname, correo FROM usuario WHERE pk_nickname = %s OR correo = %s;", (user_id, email))

        res = cur.fetchone()

        if res is None:
            hashed_pwd = generate_password_hash(pwd)
            cur.execute("INSERT INTO usuario VALUES(%s, %s, %s);", (user_id, email, hashed_pwd))
            user = User(user_id)
            login_user(user)
            return redirect(url_for('yourPCHome'))
        
        return render_template("signUp.html", repited_account=True)
    except(psycopg2.DatabaseError) as error:
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

        cur.execute(f"SELECT pk_nickname, correo, contrasenia FROM usuario WHERE correo = '{correo}';")
        res = cur.fetchone()

        if res is None or check_password_hash(res[2], pwd) is False:
            return render_template("login.html", error=True)

        id = res[0]
        user = User(id)
        login_user(user)
                
        return redirect(url_for('yourPCHome'))
        
    except(psycopg2.DatabaseError) as error:
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
    app.run(debug=True, port=5001)