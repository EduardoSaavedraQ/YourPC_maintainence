from flask import Flask, render_template, url_for, request, redirect, make_response, jsonify
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import mysql.connector
from conectar import conectar
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import numpy as np

app = Flask(__name__)
app.secret_key = 'una clave secreta muy segura'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'logIn'

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


@app.route('/<int:admin>/')
@app.route('/')
def yourPCHome(admin=None):
    admin_value = admin if admin is not None else False

    response = make_response(render_template("yourPCHome.html", admin=admin_value))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'

    return response

def get_graph():
    x = np.array([1, 2, 3, 4])
    y = np.array([10, 15, 13, 17])
    # Generar un gráfico con Matplotlib
    #plt.bar(x, y)
    plt.plot(x, y)
    plt.title('Ejemplo de Gráfico')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.xticks(rotation=-90)

    # Guardar el gráfico en un objeto BytesIO
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Convertir la imagen a base64
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()

    return 'data:image/png;base64,{}'.format(graph_url)

@app.route('/showGraphic')
def  showGraphicPage():
    graph_url = get_graph()
    return render_template('showGraph.html', graph_url=graph_url)

@app.route('/signUp')
def signUp():
    return render_template("signUp.html",url_for=url_for)

@app.route('/logIn')
def logIn():
    return render_template("logIn.html",url_for=url_for)

@app.route('/startPage')
def startPage():
    return render_template("startPage.html",url_for=url_for)

@app.route('/notebook/<int:admin>')
@login_required
def notebookPage(admin=None):
    admin_value = admin if admin is not None else False

    response = make_response(render_template("notebook.html", admin=admin_value))
    response = make_response(render_template("notebook.html", admin=admin_value))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'

    return response

@app.route('/addPCPage/<int:admin>')
@app.route('/addPCPage')
@login_required
def addPCPage():
    response = make_response(render_template("addPC.html"))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'

    return response

@app.route('/searchPCPage/<int:admin>')
@app.route('/searchPCPage')
@login_required
def searchPCPage(admin=None):
    admin_value = admin if admin is not None else False

    response = make_response(render_template('searchPC.html', admin=admin_value))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    
    return response

@app.route('/createAdminUser')
@login_required
def createAdminUserPage():
    response = make_response(render_template("createAdminUser.html", url_for=url_for))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'

    return response

@app.route('/selectPCPage')
@login_required
def selectPCPage():
    response = make_response(render_template("selectPC.html"))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'

    return response

@app.route('/modifyPCPage/<string:id>')
@login_required
def modifyPCPage(id):
    try:
        conn = conectar()
        cur = conn.cursor()

        print(id)

        sql = f"SELECT pk_nombre, precio, proposito, descripcion, imagen_filename FROM pc WHERE pk_nombre = '{id}'"
        print("llega")
        
        cur.execute(sql)

        res = cur.fetchone()

        res = list(res)

        response = make_response(render_template("modifyPC.html", pc=res))
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'

        return response
    
    except(mysql.connector.Error):
        return "No se ha podido cargar la PC"

    finally:
        if cur is not None:
            cur.close()
            conn.close()

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

@app.route('/addNewAdmin', methods=['POST'])
@login_required
def addNewAdmin():

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
            cur.execute(f"INSERT INTO usuarios(pk_nickname, correo, contrasenia, admin) VALUES('{user_id}', '{email}', '{hashed_pwd}', 1);")
            
            return redirect(url_for('yourPCHome', admin=1))

        return render_template("createAdminUser.html", repited_account=True)
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
        user = User(id)
        login_user(user)
        
        return redirect(url_for('yourPCHome', admin=res[3]))

    except(mysql.connector.Error) as error:
        print(error)

    finally:
        if cur is not None:
            cur.close()
            conn.close()

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')

@app.route('/uploadPC/<string:admin_id>', methods=['POST'])
@login_required
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

        return redirect(url_for("yourPCHome", admin=1))
    except(mysql.connector.DatabaseError) as error:
        print(error)
        return "Error en la inserción de los datos"
    finally:
        if cur is not None:
            cur.close()
            conn.close()

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

@app.route('/searchPC/<int:admin>', methods=['POST'])
def searchPC(admin=None):
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
            return render_template('searchPC.html', no_results = True, admin=admin)

        from porpousesDic import porpousesDic

        for r in resultados:
            print(r)
            r[4] = porpousesDic[r[4]]
        
        return render_template('searchPC.html', results = resultados, admin=admin)

    except(mysql.connector.DatabaseError) as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
            conn.close()

@app.route('/addPCToNotebook', methods=['POST'])
def addPCToNotebook():
    pcName = request.json['pcName']

    try:
        conn = conectar()
        cur = conn.cursor()

        sqlSearching = f"SELECT * FROM usuarios_pcs WHERE fk_id_usuario = '{current_user.id}' AND fk_id_pc = '{pcName}';"
        cur.execute(sqlSearching)

        res = cur.fetchone()

        if res is not None:
            raise Exception("PC ya añadida a la libreta")

        sqlInsertion = f"INSERT INTO usuarios_pcs VALUES ('{current_user.id}', '{pcName}');"

        cur.execute(sqlInsertion)

        return jsonify(None)
    
    except(mysql.connector.Error, Exception) as error:
        print(error)
    
    finally:
        if cur is not None:
            cur.close()
            conn.close()

@app.route('/selectPCPage/getPCMatches', methods=['POST'])
def getPCMatches():
    if request.method == 'POST':
        print(request.json)
        id = request.json['input']
        print(id)

        try:
            conn = conectar()
            cur = conn.cursor()

            sql = f"SELECT pk_nombre, imagen_filename, descripcion, precio, proposito FROM pc WHERE pk_nombre LIKE '{id}%';"

            cur.execute(sql)

            res = cur.fetchall()
            res = [list(tupl) for tupl in res]

            print(res)

            return jsonify(res)
        
        except(mysql.connector.DatabaseError) as error:
            print(error)
        
        finally:
            if cur is not None:
                cur.close()
                conn.close()

@app.route('/updatePC/<string:id>', methods=['POST'])
def savePCChanges(id):
    newPCName = request.form['PC Name']
    newPrice = request.form['Price']
    newPurpose = request.form['Purpose']
    newDescription = request.form['Description']
    newImage = None
    newFilename = ''

    if 'Image' in request.files:
        newImage = request.files['Image']
        newFilename = secure_filename(newImage.filename)

    try:
        conn = conectar()
        cur = conn.cursor()

        currentImageRes = None

        if newFilename != '':
            sqlCurrentImage = f"SELECT imagen_filename FROM pc WHERE pk_nombre = '{id}';"
            cur.execute(sqlCurrentImage)
            currentImageRes = cur.fetchone()[0]
        
        sqlUpdate = f"UPDATE pc SET pk_nombre = '{newPCName}', precio = {newPrice}, descripcion = '{newDescription}', proposito = {newPurpose}" 

        if newFilename != '':
            sqlUpdate += f", imagen_filename = '{newFilename}'"
        
        sqlUpdate += f" WHERE pk_nombre = '{id}';"
        print(sqlUpdate)

        cur.execute(sqlUpdate)

        if newFilename != '':
            currentFilename = f'static/uploads/{currentImageRes}'
            os.remove(currentFilename)

            newImage.save('static/uploads/' + newFilename)

        return redirect(url_for('modifyPCPage', id=newPCName))

    except(mysql.connector.DatabaseError) as error:
        print(error)

    finally:
        if cur is not None:
            cur.close()
            conn.close()

@app.route('/modifyPC/getPC', methods=['POST'])
def getPC():
    if request.method == 'POST':
        pcID = request.json['input']

        try:
            conn = conectar()
            cur = conn.cursor()

            sql = f"SELECT pk_nombre FROM pc WHERE pk_nombre = '{pcID}';"

            cur.execute(sql)

            res = cur.fetchone()

            if res is None:
                return jsonify(None)
            
            res = list(res)
            print(res)

            return jsonify(res)
        
        except(mysql.connector.DatabaseError) as error:
            print(error)
        
        finally:
            if cur is not None:
                cur.close()
                conn.close()

@app.route('/deletePC', methods=['POST'])
def deletePC():
    pcName = request.json['id']

    try:
        conn = conectar()
        cur = conn.cursor()

        sqlGetPCImageFilename = f"SELECT imagen_filename FROM pc WHERE pk_nombre = '{pcName}'"

        cur.execute(sqlGetPCImageFilename)

        filename = cur.fetchone()[0]

        sqlDeletion = f"DELETE FROM pc WHERE pk_nombre = '{pcName}'"

        cur.execute(sqlDeletion)
        os.remove(f'static/uploads/{filename}')

        return redirect(url_for('selectPCPage'))
    
    except(mysql.connector.Error) as error:
        print(error)
        return jsonify(None)
    
    finally:
        if cur is not None:
            cur.close()
            conn.close()

@app.route('/notebook/getNoteBook')
def getNoteBook():
    try:
        conn = conectar()
        cur = conn.cursor()

        sqlPCsUser = f"SELECT fk_id_pc FROM usuarios_pcs WHERE fk_id_usuario = '{current_user.id}'"

        sqlGetPCMatches = f"SELECT pk_nombre, imagen_filename, descripcion, precio, proposito FROM pc WHERE pk_nombre IN ({sqlPCsUser});"

        cur.execute(sqlGetPCMatches)

        res = cur.fetchall()

        if len(res) == 0:
            res = None

        return jsonify(res)

    except(mysql.connector.Error) as error:
        print(error)
    
    finally:
        if cur is not None:
            cur.close()
            conn.close()

@app.route('/notebook/deletePCFromNotebook', methods=['POST'])
def deletePCFromNotebook():
    pcName = request.json['pcId']

    try:
        conn = conectar()
        cur = conn.cursor()

        sql = f"DELETE FROM usuarios_pcs WHERE fk_id_usuario = '{current_user.id}' AND fk_id_pc = '{pcName}';"

        cur.execute(sql)

        return jsonify(None)
    
    except(mysql.connector.Error) as error:
        print(error)
    
    finally:
        if cur is not None:
            cur.close()
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)