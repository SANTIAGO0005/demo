import sqlite3

class Nave_servicio:

    def __init__(self):
            self.conexion = sqlite3.connect('/datebase/BD_nave.db', isolation_level=None)

    def insertar_navesL(self,nombre,peso,altura,comustible,potencia,estado,capacidad_carga):

            cursor = self.conexion.cursor()
            query = '''INSERT INTO nave (nombre,peso,altura,combustible,potencia,estado) values (?,?,?,?,?,?);'''
            query2 ='''INSERT INTO nave_lanzadera (capacidad_carga,nombre_L) values (?,?)'''
            rows = cursor.execute(query, ( nombre,peso,altura,comustible,potencia,estado),query2,(capacidad_carga,nombre))
            filas = rows.fetchall()
            return filas



    def insertar_navesR(self,nombre,peso,altura,comustible,potencia,estado,capacidad_motores,objetivo_estudio):

            cursor = self.conexion.cursor()
            query = '''INSERT INTO nave (nombre,peso,altura,combustible,potencia,estado) values (?,?,?,?,?,?);'''
            query2 ='''INSERT INTO nave_robotica (cantidad_motores,nombre_R,objetivo_estudio) values (?,?,?)'''
            rows = cursor.execute(query, ( nombre,peso,altura,comustible,potencia,estado),query2,(capacidad_motores,nombre,objetivo_estudio))
            filas = rows.fetchall()
            return filas


    def insertar_navesT(self,nombre,peso,altura,comustible,potencia,estado,capacidad_personas,tipo,tarea):

            cursor = self.conexion.cursor()
            query = '''INSERT INTO nave (nombre,peso,altura,combustible,potencia,estado) values (?,?,?,?,?,?);'''
            query2 ='''INSERT INTO nave_tripulada (nombre_T,capacidad_personas,tipo,tarea) values (?,?,?)'''
            rows = cursor.execute(query, ( nombre,peso,altura,comustible,potencia,estado),query2,(nombre,capacidad_personas,tipo,tarea))
            filas = rows.fetchall()
            return filas

    def consultar_naves(self):
        pass