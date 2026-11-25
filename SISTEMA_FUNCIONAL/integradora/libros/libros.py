
import conexionBD

class Libros:
    def __init__(self, titulo, año_publicacion, autor, disponible, isbn):
        self._titulo = titulo
        self._año_publicacion = año_publicacion
        self._autor = autor
        self._disponible = disponible
        self._isbn = isbn

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, valor):
        self._titulo = valor

    @property
    def año_publicacion(self):
        return self._año_publicacion

    @año_publicacion.setter
    def año_publicacion(self, valor):
        self._año_publicacion = valor

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, valor):
        self._autor = valor

    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, valor):
        self._disponible = valor

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
            (titulo, año_publicacion, autor, disponible, isbn)
            VALUES (%s, %s, %s, %s, %s)"""

            valores = (
                self.titulo, self.año_publicacion, self.autor,
                self.disponible, self.isbn
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
            titulo=%s, año_publicacion=%s, autor=%s,
            disponible=%s, isbn=%s WHERE id=%s"""

            valores = (
                self.titulo, self.año_publicacion, self.autor,
                self.disponible, self.isbn, id
            )

            cursor.execute(sql, valores)
            conexion.commit()
            return cursor.rowcount >= 0

        except Exception as e:
            if getattr(conexionBD, "conexion", None):
                conexionBD.conexion.rollback()
            print("Error al modificar libro:", e)
            return False
