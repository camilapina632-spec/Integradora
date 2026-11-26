import conexionBD


class Prestamos:
    def __init__(self, alumno, libro, fecha_prestamo, fecha_retorno):
        self._alumno = alumno
        self._libro = libro
        self._fecha_prestamo = fecha_prestamo
        self._fecha_retorno = fecha_retorno

    @property
    def alumno(self):
        return self._alumno

    @alumno.setter
    def alumno(self, valor):
        self._alumno = valor

    @property
    def libro(self):
        return self._libro

    @libro.setter
    def libro(self, valor):
        self._libro = valor

    @property
    def fecha_prestamo(self):
        return self._fecha_prestamo

    @fecha_prestamo.setter
    def fecha_prestamo(self, valor):
        self._fecha_prestamo = valor

    @property
    def fecha_retorno(self):
        return self._fecha_retorno

    @fecha_retorno.setter
    def fecha_retorno(self, valor):
        self._fecha_retorno = valor

    @staticmethod
    def _existe_referencia(tabla, id_valor):
        cursor = conexionBD.cursor
        cursor.execute(f"SELECT 1 FROM {tabla} WHERE id = %s LIMIT 1", (id_valor,))
        return cursor.fetchone() is not None

    def insertar(self):
        try:
            cursor = conexionBD.cursor
            conexion = conexionBD.conexion

            if not self._existe_referencia("alumnos", self.alumno):
                print(f"Error: el alumno con id={self.alumno} no existe.")
                return False

            if not self._existe_referencia("libros", self.libro):
                print(f"Error: el libro con id={self.libro} no existe.")
                return False

            sql = """INSERT INTO prestamos
            (Alumno, Libro, fecha_prestamo, fecha_retorno)
            VALUES (%s, %s, %s, %s)"""

            valores = (
                self.alumno,
                self.libro,
                self.fecha_prestamo,
                self.fecha_retorno,
            )

            cursor.execute(sql, valores)
            conexion.commit()
            return True

        except Exception as e:
            if getattr(conexionBD, "conexion", None):
                conexionBD.conexion.rollback()
            print("Error al insertar préstamo (llave foránea o BD):", e)
            return False

    def consultar(self):
        try:
            cursor = conexionBD.cursor
            sql = """SELECT p.id, p.Alumno, p.Libro, p.fecha_prestamo, p.fecha_retorno,
                      a.nombre AS nombre_alumno, l.autor AS autor_libro
               FROM prestamos p
               INNER JOIN alumnos a ON p.Alumno = a.id
               INNER JOIN libros l ON p.Libro = l.id"""
            cursor.execute(sql)
            return cursor.fetchall()

        except Exception as e:
            print("Error al consultar préstamos:", e)
            return []

    def eliminar(self, id_prestamo):
        try:
            cursor = conexionBD.cursor
            conexion = conexionBD.conexion

            cursor.execute(
                "DELETE FROM prestamos WHERE id = %s",
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

            if not self._existe_referencia("alumnos", self.alumno):
                print(f"Error: el alumno con id={self.alumno} no existe.")
                return False

            if not self._existe_referencia("libros", self.libro):
                print(f"Error: el libro con id={self.libro} no existe.")
                return False

            sql = """UPDATE prestamos SET
            Alumno = %s,
            Libro = %s,
            fecha_prestamo = %s,
            fecha_retorno = %s
            WHERE id = %s"""

            valores = (
                self.alumno,
                self.libro,
                self.fecha_prestamo,
                self.fecha_retorno,
                id_prestamo,
            )

            cursor.execute(sql, valores)
            conexion.commit()
            return cursor.rowcount > 0

        except Exception as e:
            if getattr(conexionBD, "conexion", None):
                conexionBD.conexion.rollback()
            print("Error al modificar préstamo (llave foránea o BD):", e)
            return False
