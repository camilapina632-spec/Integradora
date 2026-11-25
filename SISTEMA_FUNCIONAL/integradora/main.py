
from alumnos import alumnos
from bibliotecarios import bibliotecarios
from libros import libros
from prestamos import prestamos

import tkinter as tk
from tkinter import ttk, messagebox


class App:

    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Sistema de Biblioteca")
        self.ventana.geometry("850x650")
        self.ventana.resizable(False, False)

        self.modelo = None
        self.campos = []
        self.nombre_tabla = ""
        self.identificador = ""
        self.entradas = {}

        self.main()

    # -----------------------------------------
    # CONFIGURACION DE LAS TABLAS
    # -----------------------------------------

    def configuracion(self, tipo):

        configuraciones = {
            "Alumnos": {
                "clase": alumnos.Alumnos,
                "campos": [
                    "nombre", "apellido1", "apellido2",
                    "gradoGrupo", "turno"
                ],
                "id": "id"
            },

            "Bibliotecarios": {
                "clase": bibliotecarios.Bibliotecarios,
                "campos": ["nombre", "turno"],
                "id": "id"
            },

            "Libros": {
                "clase": libros.Libros,
                "campos": [
                    "titulo", "año_publicacion", "autor",
                    "disponible", "isbn"
                ],
                "id": "id"
            },

            "Prestamos": {
                "clase": prestamos.Prestamos,
                "campos": [
                    "id_alumno", "id_libro", "id_bibliotecario",
                    "fechaPrestamo", "fechaRetorno",
                    "horaSalida", "horaReingreso", "observaciones"
                ],
                "id": "id_prestamo"
            }
        }

        datos = configuraciones[tipo]

        self.modelo = datos["clase"]
        self.campos = datos["campos"]
        self.nombre_tabla = tipo
        self.identificador = datos["id"]

    # -----------------------------------------
    # LIMPIAR VENTANA
    # -----------------------------------------

    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    # -----------------------------------------
    # MENU PRINCIPAL
    # -----------------------------------------

    def main(self):
        self.borrarPantalla()

        tk.Label(
            self.ventana,
            text="SISTEMA DE BIBLIOTECA",
            font=("Arial", 22, "bold")
        ).pack(pady=30)

        tk.Label(
            self.ventana,
            text="Selecciona el apartado que deseas administrar",
            font=("Arial", 12)
        ).pack(pady=10)

        opciones = [
            "Alumnos",
            "Bibliotecarios",
            "Libros",
            "Prestamos"
        ]

        for opcion in opciones:
            tk.Button(
                self.ventana,
                text=opcion,
                width=30,
                height=2,
                font=("Arial", 12),
                command=lambda tipo=opcion: self.menu_acciones(tipo)
            ).pack(pady=8)

    # -----------------------------------------
    # MENU DE ACCIONES
    # -----------------------------------------

    def menu_acciones(self, tipo):
        self.configuracion(tipo)
        self.borrarPantalla()

        tk.Label(
            self.ventana,
            text=f"MENU DE {tipo.upper()}",
            font=("Arial", 20, "bold")
        ).pack(pady=25)

        acciones = [
            ("Agregar", self.insertar_view),
            ("Eliminar", self.eliminar_view),
            ("Modificar", self.modificar_view),
            ("Consultar", self.consultar_view)
        ]

        for texto, funcion in acciones:
            tk.Button(
                self.ventana,
                text=texto,
                width=30,
                height=2,
                font=("Arial", 12),
                command=funcion
            ).pack(pady=7)

        tk.Button(
            self.ventana,
            text="Regresar al menú principal",
            width=30,
            command=self.main
        ).pack(pady=20)

    # -----------------------------------------
    # CREAR OBJETO
    # -----------------------------------------

    def crear_modelo(self, valores):
        return self.modelo(*valores)

    # -----------------------------------------
    # VISTA PARA INSERTAR
    # -----------------------------------------

    def insertar_view(self):
        self.formulario_view(
            "Agregar registro",
            self.insertar_controller
        )

    # -----------------------------------------
    # VISTA PARA MODIFICAR
    # -----------------------------------------

    def modificar_view(self):
        self.formulario_view(
            "Modificar registro",
            self.modificar_controller,
            incluir_id=True
        )

    # -----------------------------------------
    # FORMULARIO GENERAL
    # -----------------------------------------

    def formulario_view(self, titulo, funcion, incluir_id=False):
        self.borrarPantalla()

        tk.Label(
            self.ventana,
            text=titulo,
            font=("Arial", 20, "bold")
        ).pack(pady=15)

        contenedor = tk.Frame(self.ventana)
        contenedor.pack(pady=5)

        self.entradas = {}

        # Campo para el identificador
        if incluir_id:
            tk.Label(
                contenedor,
                text=self.identificador,
                font=("Arial", 11)
            ).grid(
                row=0,
                column=0,
                padx=10,
                pady=7,
                sticky="w"
            )

            entrada_id = tk.Entry(contenedor, width=35)
            entrada_id.grid(
                row=0,
                column=1,
                padx=10,
                pady=7
            )

            self.entradas[self.identificador] = entrada_id

        # Crear los campos correspondientes a cada tabla
        fila_inicial = 1 if incluir_id else 0

        for i, campo in enumerate(self.campos):

            tk.Label(
                contenedor,
                text=campo,
                font=("Arial", 11)
            ).grid(
                row=i + fila_inicial,
                column=0,
                padx=10,
                pady=7,
                sticky="w"
            )

            entrada = tk.Entry(contenedor, width=35)
            entrada.grid(
                row=i + fila_inicial,
                column=1,
                padx=10,
                pady=7
            )

            self.entradas[campo] = entrada

        tk.Button(
            self.ventana,
            text="Guardar",
            width=20,
            command=funcion
        ).pack(pady=15)

        tk.Button(
            self.ventana,
            text="Regresar",
            width=20,
            command=lambda: self.menu_acciones(self.nombre_tabla)
        ).pack(pady=5)

    # -----------------------------------------
    # CONTROLADOR PARA INSERTAR
    # -----------------------------------------

    def insertar_controller(self):

        valores = [
            self.entradas[campo].get().strip()
            for campo in self.campos
        ]

        if any(valor == "" for valor in valores):
            messagebox.showwarning(
                "Campos vacíos",
                "Debes completar todos los campos."
            )
            return

        objeto = self.crear_modelo(valores)

        if objeto.insertar():

            messagebox.showinfo(
                "Correcto",
                "El registro se agregó correctamente."
            )

            self.menu_acciones(self.nombre_tabla)

        else:

            messagebox.showerror(
                "Error",
                "No fue posible agregar el registro. Revisa los datos."
            )

    # -----------------------------------------
    # VISTA PARA ELIMINAR
    # -----------------------------------------

    def eliminar_view(self):
        self.borrarPantalla()

        tk.Label(
            self.ventana,
            text="ELIMINAR REGISTRO",
            font=("Arial", 20, "bold")
        ).pack(pady=30)

        tk.Label(
            self.ventana,
            text=f"Ingresa el {self.identificador} del registro:"
        ).pack(pady=10)

        self.entrada_id = tk.Entry(
            self.ventana,
            width=35
        )
        self.entrada_id.pack(pady=10)

        tk.Button(
            self.ventana,
            text="Eliminar",
            width=20,
            command=self.eliminar_controller
        ).pack(pady=15)

        tk.Button(
            self.ventana,
            text="Regresar",
            width=20,
            command=lambda: self.menu_acciones(self.nombre_tabla)
        ).pack(pady=5)

    # -----------------------------------------
    # CONTROLADOR PARA ELIMINAR
    # -----------------------------------------

    def eliminar_controller(self):

        id_registro = self.entrada_id.get().strip()

        if id_registro == "":
            messagebox.showwarning(
                "Campo vacío",
                "Debes ingresar un identificador."
            )
            return

        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            "¿Estás seguro de eliminar este registro?"
        )

        if not confirmar:
            return

        objeto = self.crear_modelo(
            [""] * len(self.campos)
        )

        if objeto.eliminar(id_registro):

            messagebox.showinfo(
                "Correcto",
                "El registro fue eliminado."
            )

            self.menu_acciones(self.nombre_tabla)

        else:

            messagebox.showerror(
                "Error",
                "No se encontró el registro o no pudo eliminarse."
            )

    # -----------------------------------------
    # CONTROLADOR PARA MODIFICAR
    # -----------------------------------------

    def modificar_controller(self):

        id_registro = self.entradas[
            self.identificador
        ].get().strip()

        if id_registro == "":
            messagebox.showwarning(
                "Campo vacío",
                "Debes ingresar el identificador."
            )
            return

        valores = [
            self.entradas[campo].get().strip()
            for campo in self.campos
        ]

        if any(valor == "" for valor in valores):
            messagebox.showwarning(
                "Campos vacíos",
                "Debes completar todos los campos."
            )
            return

        objeto = self.crear_modelo(valores)

        if objeto.modificar(id_registro):

            messagebox.showinfo(
                "Correcto",
                "El registro fue modificado."
            )

            self.menu_acciones(self.nombre_tabla)

        else:

            messagebox.showerror(
                "Error",
                "No fue posible modificar el registro."
            )

    # -----------------------------------------
    # VISTA PARA CONSULTAR
    # -----------------------------------------

    def consultar_view(self):
        self.borrarPantalla()

        tk.Label(
            self.ventana,
            text=f"CONSULTAR {self.nombre_tabla.upper()}",
            font=("Arial", 20, "bold")
        ).pack(pady=15)

        # Crear un objeto vacío para ejecutar consultar()
        objeto = self.crear_modelo(
            [""] * len(self.campos)
        )

        registros = objeto.consultar()

        # Crear tabla
        marco = tk.Frame(self.ventana)
        marco.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        columnas = [self.identificador] + self.campos

        tabla = ttk.Treeview(
            marco,
            columns=columnas,
            show="headings"
        )

        for columna in columnas:
            tabla.heading(
                columna,
                text=columna
            )

            tabla.column(
                columna,
                width=110,
                anchor="center"
            )

        tabla.pack(
            side="left",
            fill="both",
            expand=True
        )

        scroll = ttk.Scrollbar(
            marco,
            orient="vertical",
            command=tabla.yview
        )

        scroll.pack(
            side="right",
            fill="y"
        )

        tabla.configure(
            yscrollcommand=scroll.set
        )

        for registro in registros:
            tabla.insert(
                "",
                "end",
                values=registro
            )

        if not registros:
            messagebox.showinfo(
                "Consulta",
                "No hay registros para mostrar."
            )

        tk.Button(
            self.ventana,
            text="Regresar",
            width=20,
            command=lambda: self.menu_acciones(self.nombre_tabla)
        ).pack(pady=15)


# -----------------------------------------
# INICIAR APLICACION
# -----------------------------------------

if __name__ == "__main__":

    ventana = tk.Tk()

    aplicacion = App(ventana)

    ventana.mainloop()