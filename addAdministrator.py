from werkzeug.security import generate_password_hash
from conectar import conectar

passw = "INNI2024x-7"
hashed_passwd = generate_password_hash(passw)

conn = conectar()

cur = conn.cursor()

cur.execute(f"INSERT INTO usuarios(pk_nickname, correo, contrasenia, admin) VALUES('root', 'eduardoooo89@hotmail.com', '{hashed_passwd}', 1);",)