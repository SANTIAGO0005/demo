import getpass
import sqlite3




def verifica_credenciales(username, password):
    conn= sqlite3.connect('miapp.db')
    cursor = conn.cursor()

    query = f'select id from user where username="{username}" and  password="{password}"'
    print('Query a ejecutar :',query)
    rows = cursor.execute(query)
    data = rows.fetchone()
    conn.commit()


    cursor.close()
    conn.close()
"""if data == None:
    return False
 return True
 """
def crear_usuario(identificador, usuario, clave):
    conn = sqlite3.connect('miapp.db',isolation_level=None)
    cursor = conn.cursor()

    query = '''INSERT INTO user (id,username,password) values (?,?,?)'''
    rows = cursor.execute(query,(identificador, usuario, clave))
    print(type(rows))

    cursor.close()
    conn.close()

def main2():
    username = input("Nombre de usuario: ")
    password = getpass.getpass("contraseña: ")

    if verifica_credenciales(username,password):
        print('login correcto')
    else:
        print('login incorrecto')

def main():
    crear_usuario(6,"gerardo","supermk")

if __name__ == '__main__':
    main()





#conn =sqlite3.connect('miapp.db')
#cursor= conn.cursor()

#rows =cursor.execute('select * from user where username="telo"')
#for row in rows:
#    print(row)
#cursor.close()
#conn.close()