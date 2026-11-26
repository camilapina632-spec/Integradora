import conexionBD


class Alumnos:
    def __init__(
        self,
        nombre,
        apellido_paterno,
        apellido_materno,
        grado,
        grupo,
        turno,
    ):
        self._nombre = nombre
        self._apellido_paterno = apellido_paterno
        self._apellido_materno = apellido_materno
        self._grado = grado
        self._grupo = grupo
        self._turno = turno

    # Propiedades
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def apellido_paterno(self):
        return self._apellido_paterno

    @apellido_paterno.setter
    def apellido_paterno(self, valor):
        self._apellido_paterno = valor

    @property
    def apellido_materno(self):
        return self._apellido_materno

    @apellido_materno.setter
    def apellido_materno(self, valor):
        self._apellido_materno = valor

    @property
    def grado(self):
        return self._grado

    @grado.setter
    def grado(self, valor):
        self._grado = valor

    @property
    def grupo(self):
        return self._grupo

    @grupo.setter
    def grupo(self, valor):
        self._grupo = valor

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
            (nombre, apellido_paterno, apellido_materno, grado, grupo, turno)
            VALUES (%s, %s, %s, %s, %s, %s)"""

            valores = (
                self.nombre,
                self.apellido_paterno,
                self.apellido_materno,
                self.grado,
                self.grupo,
                self.turno,
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
            nombre = %s,
            apellido_paterno = %s,
            apellido_materno = %s,
            grado = %s,
            grupo = %s,
            turno = %s
            WHERE id = %s"""

            valores = (
                self.nombre,
                self.apellido_paterno,
                self.apellido_materno,
                self.grado,
                self.grupo,
                self.turno,
                id,
            )

            cursor.execute(sql, valores)
            conexion.commit()
            return cursor.rowcount > 0

        except Exception as e:
            if getattr(conexionBD, "conexion", None):
                conexionBD.conexion.rollback()
            print("Error al modificar alumno:", e)
            return False
