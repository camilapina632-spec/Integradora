
import conexionBD

class Bibliotecarios:
    def __init__(self, nombre, turno):
        self._nombre = nombre
        self._turno = turno

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def turno(self):
        return self._turno

    @turno.setter
    def turno(self, valor):
        self._turno = valor

    def insertar(self):
        try:
            cursor = conexionBD.cursor
            conexion = conexionBD.conexion

            sql = """INSERT INTO bibliotecarios (nombre, turno)
                     VALUES (%s, %s)"""

            cursor.execute(sql, (self.nombre, self.turno))
            conexion.commit()
            return True

        except Exception as e:
            if getattr(conexionBD, "conexion", None):
                conexionBD.conexion.rollback()
            print("Error al insertar bibliotecario:", e)
            return False

    def consultar(self):
        try:
            cursor = conexionBD.cursor
            cursor.execute("SELECT * FROM bibliotecarios")
            return cursor.fetchall()

        except Exception as e:
            print("Error al consultar bibliotecarios:", e)
            return []

    def eliminar(self, id):
        try:
            cursor = conexionBD.cursor
            conexion = conexionBD.conexion

            cursor.execute(
                "DELETE FROM bibliotecarios WHERE id = %s", (id,)
            )
            conexion.commit()
            return cursor.rowcount > 0

        except Exception as e:
            if getattr(conexionBD, "conexion", None):
                conexionBD.conexion.rollback()
            print("Error al eliminar bibliotecario:", e)
            return False

    def modificar(self, id):
        try:
            cursor = conexionBD.cursor
            conexion = conexionBD.conexion

            sql = """UPDATE bibliotecarios
                     SET nombre=%s, turno=%s WHERE id=%s"""

            cursor.execute(sql, (self.nombre, self.turno, id))
            conexion.commit()
            return cursor.rowcount >= 0

        except Exception as e:
            if getattr(conexionBD, "conexion", None):
                conexionBD.conexion.rollback()
            print("Error al modificar bibliotecario:", e)
            return False

    @classmethod
    def existe_contrasena(cls, contrasena):
        try:
            cursor = conexionBD.cursor
            sql = "SELECT 1 FROM bibliotecarios WHERE `contraseña` = %s LIMIT 1"
            cursor.execute(sql, (contrasena,))
            return cursor.fetchone() is not None
        except Exception as e:
            print("Error al verificar contraseña:", e)
            return False

    @classmethod
    def verificar_acceso(cls, nombre, contrasena):
        try:
            cursor = conexionBD.cursor
            sql = """SELECT id, nombre, apellido_paterno, apellido_materno, turno
                     FROM bibliotecarios
                     WHERE nombre = %s AND `contraseña` = %s
                     LIMIT 1"""
            cursor.execute(sql, (nombre, contrasena))
            return cursor.fetchone()
        except Exception as e:
            print("Error al validar acceso:", e)
            return None

