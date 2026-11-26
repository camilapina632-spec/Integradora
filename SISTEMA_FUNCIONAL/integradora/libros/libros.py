import conexionBD


class Libros:
    def __init__(self, titulo, autor, anio_publicacion, isbn):
        self._titulo = titulo
        self._autor = autor
        self._anio_publicacion = anio_publicacion
        self._isbn = isbn

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, valor):
        self._titulo = valor

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, valor):
        self._autor = valor

    @property
    def anio_publicacion(self):
        return self._anio_publicacion

    @anio_publicacion.setter
    def anio_publicacion(self, valor):
        self._anio_publicacion = valor

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, valor):
        self._isbn = valor

    def insertar(self):
        try:
            cursor = conexionBD.cursor
            conexion = conexionBD.conexion

            sql = """INSERT INTO libros
            (titulo, autor, anio_publicacion, ISBN)
            VALUES (%s, %s, %s, %s)"""

            valores = (
                self.titulo,
                self.autor,
                self.anio_publicacion,
                self.isbn,
            )

            cursor.execute(sql, valores)
            conexion.commit()
            return True

        except Exception as e:
            if getattr(conexionBD, "conexion", None):
                conexionBD.conexion.rollback()
            print("Error al insertar libro:", e)
            return False

    def consultar(self):
        try:
            cursor = conexionBD.cursor
            cursor.execute("SELECT * FROM libros")
            return cursor.fetchall()

        except Exception as e:
            print("Error al consultar libros:", e)
            return []

    def eliminar(self, id):
        try:
            cursor = conexionBD.cursor
            conexion = conexionBD.conexion

            cursor.execute("DELETE FROM libros WHERE id = %s", (id,))
            conexion.commit()
            return cursor.rowcount > 0

        except Exception as e:
            if getattr(conexionBD, "conexion", None):
                conexionBD.conexion.rollback()
            print("Error al eliminar libro:", e)
            return False

    def modificar(self, id):
        try:
            cursor = conexionBD.cursor
            conexion = conexionBD.conexion

            sql = """UPDATE libros SET
            titulo = %s,
            autor = %s,
            anio_publicacion = %s,
            ISBN = %s
            WHERE id = %s"""

            valores = (
                self.titulo,
                self.autor,
                self.anio_publicacion,
                self.isbn,
                id,
            )

            cursor.execute(sql, valores)
            conexion.commit()
            return cursor.rowcount > 0

        except Exception as e:
            if getattr(conexionBD, "conexion", None):
                conexionBD.conexion.rollback()
            print("Error al modificar libro:", e)
            return False
