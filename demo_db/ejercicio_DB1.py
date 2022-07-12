import sqlite3

def insertar_Alumnos(id, nombre, apellido):
    conn = sqlite3.connect('ejercicioDB.db',isolation_level=None)
    cursor = conn.cursor()

    query = '''INSERT INTO Alumnos (id,nombre,apellido) values (?,?,?)'''
    rows = cursor.execute(query,(id, nombre, apellido))
    filas = rows.fetchall()
    print(filas)
    cursor.close()
    conn.close()
def buscar_Alumnos(nombres):
    conn = sqlite3.connect('ejercicioDB.db')
    cursor = conn.cursor()

    query = '''select id,nombre,apellido from  Alumnos Where nombre= (?)'''
    rows = cursor.execute(query,(nombres,))
    data= rows.fetchone()
    print(data)
    cursor.close()
    conn.close()

def main():
    insertar_Alumnos(1,"Gerardo","valdez")
    insertar_Alumnos(2, "Ana", "Perez")
    insertar_Alumnos(3, "Rafael", "Ortega")
    insertar_Alumnos(4, "Santiago", "Cifuentes")
    insertar_Alumnos(5, "Gildado", "Manco")
    insertar_Alumnos(6, "Pedro", "Rodrigues")
    insertar_Alumnos(7, "Vroman", "valdez")
    insertar_Alumnos(8, "Andres", "Escobar")
    print()
    buscar_Alumnos("Pedro")

if __name__ == '__main__':
    main()
