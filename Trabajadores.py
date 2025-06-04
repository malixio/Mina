from conexion import *

class Trabajadores:
    @staticmethod
    def ingresar_trabajador(nombres, apellidos, cc, cargo):
        conexion = Conexion.conectar()
        cursor = conexion.cursor()
        sql = "INSERT INTO trabajador (nombres, apellidos, cc, cargo) VALUES (%s, %s, %s, %s)"
        valores = (nombres, apellidos, cc, cargo)
        cursor.execute(sql, valores)
        conexion.commit()
        cursor.close()
        conexion.close()

    @staticmethod
    def modificar_trabajador(id, nombres, apellidos, cc, cargo):
        conexion = Conexion.conectar()
        cursor = conexion.cursor()
        sql = "UPDATE trabajador SET nombres=%s, apellidos=%s, cc=%s, cargo=%s WHERE id=%s"
        valores = (nombres, apellidos, cc, cargo, id)
        cursor.execute(sql, valores)
        conexion.commit()
        cursor.close()
        conexion.close()

    @staticmethod
    def eliminar_trabajador(id):
        conexion = Conexion.conectar()
        cursor = conexion.cursor()
        sql = "DELETE FROM trabajador WHERE id=%s"
        cursor.execute(sql, (id,))
        conexion.commit()
        cursor.close()
        conexion.close()

    @staticmethod
    def obtener_todos():
        conexion = Conexion.conectar()
        cursor = conexion.cursor()
        sql = "SELECT id, nombres, apellidos, cc, cargo FROM trabajador"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        cursor.close()
        conexion.close()
        return resultados