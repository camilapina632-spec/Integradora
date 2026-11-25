
import conexionBD

class Prestamos:
    def __init__(self, id_alumno, id_libro, id_bibliotecario,
                 fechaPrestamo, fechaRetorno, horaSalida,
                 horaReingreso, observaciones):

        self._id_alumno = id_alumno
        self._id_libro = id_libro
        self._id_bibliotecario = id_bibliotecario
        self._fechaPrestamo = fechaPrestamo
        self._fechaRetorno = fechaRetorno
        self._horaSalida = horaSalida
        self._horaReingreso = horaReingreso
        self._observaciones = observaciones

    @property
    def id_alumno(self):
        return self._id_alumno

    @id_alumno.setter
    def id_alumno(self, valor):
        self._id_alumno = valor

    @property
    def id_libro(self):
        return self._id_libro

    @id_libro.setter
    def id_libro(self, valor):
        self._id_libro = valor

    @property
    def id_bibliotecario(self):
        return self._id_bibliotecario

    @id_bibliotecario.setter
    def id_bibliotecario(self, valor):
        self._id_bibliotecario = valor

    @property
    def fechaPrestamo(self):
        return self._fechaPrestamo

    @fechaPrestamo.setter
    def fechaPrestamo(self, valor):
        self._fechaPrestamo = valor

    @property
    def fechaRetorno(self):
        return self._fechaRetorno

    @fechaRetorno.setter
    def fechaRetorno(self, valor):
        self._fechaRetorno = valor

    @property
    def horaSalida(self):
        return self._horaSalida

    @horaSalida.setter
    def horaSalida(self, valor):
        self._horaSalida = valor

    @property
    def horaReingreso(self):
        return self._horaReingreso

    @horaReingreso.setter
    def horaReingreso(self, valor):
        self._horaReingreso = valor

    @property
    def observaciones(self):
        return self._observaciones

    @observaciones.setter
    def observaciones(self, valor):
        self._observaciones = valor

    def insertar(self):
        try:
            cursor = conexionBD.cursor
            conexion = conexionBD.conexion

            sql = """INSERT INTO prestamos
            (id_alumno, id_libro, id_bibliotecario, fechaPrestamo,
             fechaRetorno, horaSalida, horaReingreso, observaciones)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""

            valores = (
                self.id_alumno, self.id_libro, self.id_bibliotecario,
                self.fechaPrestamo, self.fechaRetorno, self.horaSalida,
                self.horaReingreso, self.observaciones
            )

            cursor.execute(sql, valores)
            conexion.commit()
            return True

        except Exception as e:
            if getattr(conexionBD, "conexion", None):
                conexionBD.conexion.rollback()
            print("Error al insertar préstamo:", e)
            return False

    def consultar(self):
        try:
            cursor = conexionBD.cursor
            cursor.execute("SELECT * FROM prestamos")
            return cursor.fetchall()

        except Exception as e:
            print("Error al consultar préstamos:", e)
            return []

    def eliminar(self, id_prestamo):
        try:
            cursor = conexionBD.cursor
            conexion = conexionBD.conexion

            cursor.execute(
                "DELETE FROM prestamos WHERE id_prestamo = %s",
                (id_prestamo,)
            )
            conexion.commit()
            return cursor.rowcount > 0

        except Exception as e:
            if getattr(conexionBD, "conexion", None):
                conexionBD.conexion.rollback()
            print("Error al eliminar préstamo:", e)
            return False

    def modificar(self, id_prestamo):
        try:
            cursor = conexionBD.cursor
            conexion = conexionBD.conexion

            sql = """UPDATE prestamos SET
            id_alumno=%s, id_libro=%s, id_bibliotecario=%s,
            fechaPrestamo=%s, fechaRetorno=%s, horaSalida=%s,
            horaReingreso=%s, observaciones=%s
            WHERE id_prestamo=%s"""

            valores = (
                self.id_alumno, self.id_libro, self.id_bibliotecario,
                self.fechaPrestamo, self.fechaRetorno, self.horaSalida,
                self.horaReingreso, self.observaciones, id_prestamo
            )

            cursor.execute(sql, valores)
            conexion.commit()
            return cursor.rowcount >= 0

        except Exception as e:
            if getattr(conexionBD, "conexion", None):
                conexionBD.conexion.rollback()
            print("Error al modificar préstamo:", e)
            return False
