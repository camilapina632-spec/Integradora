
import conexionBD

class Alumnos:
    def __init__(self, nombre, apellido1, apellido2, gradoGrupo, turno):
        self._nombre = nombre
        self._apellido1 = apellido1
        self._apellido2 = apellido2
        self._gradoGrupo = gradoGrupo
        self._turno = turno

    # Propiedades
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def apellido1(self):
        return self._apellido1

    @apellido1.setter
    def apellido1(self, valor):
        self._apellido1 = valor

    @property
    def apellido2(self):
        return self._apellido2

    @apellido2.setter
    def apellido2(self, valor):
        self._apellido2 = valor

    @property
    def gradoGrupo(self):
        return self._gradoGrupo

    @gradoGrupo.setter
    def gradoGrupo(self, valor):
        self._gradoGrupo = valor

    @property
    def turno(self):
        return self._turno

    @turno.setter
    def turno(self, valor):
        self._turno = valor

    # INSERTAR
    def insertar(self):
        try:
            cursor = conexionBD.cursor
            conexion = conexionBD.conexion

            sql = """INSERT INTO alumnos
            (nombre, apellido1, apellido2, gradoGrupo, turno)
            VALUES (%s, %s, %s, %s, %s)"""

            valores = (
                self.nombre, self.apellido1, self.apellido2,
                self.gradoGrupo, self.turno
            )

            cursor.execute(sql, valores)
            conexion.commit()
            return True

        except Exception as e:
            if getattr(conexionBD, "conexion", None):
                conexionBD.conexion.rollback()
            print("Error al insertar alumno:", e)
            return False

    # CONSULTAR
    def consultar(self):
        try:
            cursor = conexionBD.cursor
            cursor.execute("SELECT * FROM alumnos")
            return cursor.fetchall()

        except Exception as e:
            print("Error al consultar alumnos:", e)
            return []

    # ELIMINAR
    def eliminar(self, id):
        try:
            cursor = conexionBD.cursor
            conexion = conexionBD.conexion

            cursor.execute("DELETE FROM alumnos WHERE id = %s", (id,))
            conexion.commit()
            return cursor.rowcount > 0

        except Exception as e:
            if getattr(conexionBD, "conexion", None):
                conexionBD.conexion.rollback()
            print("Error al eliminar alumno:", e)
            return False

    # MODIFICAR
    def modificar(self, id):
        try:
            cursor = conexionBD.cursor
            conexion = conexionBD.conexion

            sql = """UPDATE alumnos SET
            nombre=%s, apellido1=%s, apellido2=%s,
            gradoGrupo=%s, turno=%s WHERE id=%s"""

            valores = (
                self.nombre, self.apellido1, self.apellido2,
                self.gradoGrupo, self.turno, id
            )

            cursor.execute(sql, valores)
            conexion.commit()
            return cursor.rowcount >= 0

        except Exception as e:
            if getattr(conexionBD, "conexion", None):
                conexionBD.conexion.rollback()
            print("Error al modificar alumno:", e)
            return False
