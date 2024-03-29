from flask import Flask, render_template, url_for, request, redirect
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
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

@app.route('/uploadPC/<string:admin_id>', methods=['POST'])
def uploadPC(admin_id):
    nombrePC = request.form['Nombre']
    descripcionPC = request.form['Descripcion']
    precioPC = round(float(request.form['Precio']), 2)
    propositoPC = int(request.form['Proposito'])
    imagenPC = request.files['Imagen']
    filename = secure_filename(imagenPC.filename)
    imagenPC.save('static/uploads/' + filename)

    try:
        conn = conectar()
        cur = conn.cursor()

        cur.execute(f"INSERT INTO pc(pk_nombre, fk_id_admin, descripcion, precio, proposito, imagen_filename) VALUES('{nombrePC}', '{admin_id}', '{descripcionPC}', {precioPC}, {propositoPC}, '{filename}');")

        return render_template("yourPCHome.html", admin=True)
    except(mysql.connector.DatabaseError) as error:
        print(error)
        return "Error en la inserción de los datos"
    finally:
        if cur is not None:
            cur.close()
            conn.close()

@app.route('/searchPCPage')
def searchPCPage():
    return render_template('searchPC.html')

def makeTuplePorpousesForSQL(list_of_pourposes):
    items = len(list_of_pourposes)
    cont = 1
    tuplestring = "("

    for item in list_of_pourposes:

        tuplestring += str(item)

        if cont < items:
            tuplestring += ", "
            cont += 1

    tuplestring += ")"

    return tuplestring

@app.route('/searchPC', methods=['POST'])
def searchPC():
    #Obtiene el rango de precios
    rango_precio = request.form['rango_precio']

    #Crea un alista para guardar los valores que representan propósitos de las PC
    propositos = []

    #Obtiene los valores de los checkbox y los añade a la lista
    propositos.append(request.form.get('Oficina'))
    propositos.append(request.form.get('Programacion'))
    propositos.append(request.form.get('Gaming'))
    propositos.append(request.form.get('Diseño'))

    #Elimina los valores nulos de la lista
    propositos = filter(lambda item: item!=None,propositos)

    #Convierte los valores de la lista en enteros
    propositos = list(map(int, propositos))

    try:
        conn = conectar()
        cur = conn.cursor()
        #Prepara consula de SQL
        sql_statement = "SELECT pk_nombre, imagen_filename, descripcion, precio, proposito FROM pc"
        sql_precio = f"(precio {rango_precio})"
        sql_propositos = f"(proposito IN {makeTuplePorpousesForSQL(propositos)})"
        
        #Verifica si existen condiciones para la consulta
        if rango_precio != "0" or len(propositos) != 0:
            sql_statement += " WHERE "

            #Determina si los resultados se deben encontrar dentro de un rango de precios
            if rango_precio != "0":
                sql_statement += sql_precio

            #Determina si hay dos condiciones a cumplir
            if rango_precio != "0" and len(propositos) != 0:
                sql_statement += " AND "

            #Determina si los resultados deben encontrarse dentro de ciertos propósitos
            if len(propositos) != 0:
                sql_statement += sql_propositos

        #Ejecuta la consulta y obtiene los resultados
        print(sql_statement)
        cur.execute(sql_statement)
        resultados = cur.fetchall()
        resultados = [list(tupla) for tupla in resultados]
        cantidad = len(resultados)

        print("La cantidad de resultados es:", cantidad)

        if cantidad == 0:
            return render_template('searchPC.html', no_results = True)

        from porpousesDic import porpousesDic

        for r in resultados:
            print(r)
            r[4] = porpousesDic[r[4]]
        
        return render_template('searchPC.html', results = resultados)

    except(mysql.connector.DatabaseError) as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)