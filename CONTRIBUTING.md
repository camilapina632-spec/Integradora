# Guía de contribución - ControlLibro (404 squad)

Reglas que todo el equipo sigue para que el código sea ordenado, mantenible y seguro.

## 1. Nomenclatura
- Funciones y variables: `snake_case` (ej. `registrar_prestamo`)
- Clases: `PascalCase` (ej. `Prestamo`)
- Constantes: `MAYUSCULAS` (ej. `MAX_DIAS_PRESTAMO`)
- Tablas de la base de datos: en plural y minúsculas (ej. `alumnos`)

## 2. Formato
- Indentación de 4 espacios (no tabuladores)
- Líneas de máximo 88 caracteres
- Formateador: **Black**
- Linter: **Pylint**
- Antes de cada commit se ejecuta: `black .` y `pylint src`

## 3. Funciones
- Máximo 30 líneas aproximadamente
- Una sola responsabilidad por función

## 4. Comentarios y docstrings
- Toda función pública lleva docstring con Args, Returns y Raises
- Los comentarios explican el porqué, no lo obvio

Ejemplo:

```python
def registrar_prestamo(id_libro: int, id_alumno: int) -> int:
    """Registra el préstamo de un libro a un alumno.

    Args:
        id_libro: identificador del libro (debe estar disponible).
        id_alumno: identificador del alumno registrado.

    Returns:
        El id del préstamo creado.

    Raises:
        ValueError: si el libro no está disponible o el alumno no existe.
    """
```

## 5. Estructura de carpetas
```
/src      código fuente
/docs     documentación y arquitectura
/tests    pruebas
/sql      scripts de base de datos (ej. 01_ddl.sql)
README.md
CONTRIBUTING.md
```

## 6. Control de versiones (Git)
- Ramas: `main` (estable), `develop` (integración), `feature/HU-xx` (cada historia)
- No se hace commit directo a `main`
- Commits con el formato `tipo: descripción (HU-xx)`
  - `feat: registrar préstamo (HU-03)`
  - `fix: validar fecha pasada`
  - `docs: actualizar README`
- Todo cambio entra por **pull request** y lo revisa otro integrante

## 7. Plantilla de README
Todo README incluye: nombre del proyecto, descripción, tecnologías, cómo instalar y ejecutar, estructura de carpetas e integrantes del equipo.

## 8. Definición de Terminado técnica
Una tarea está terminada cuando:
- [ ] Pasa Black y Pylint sin errores
- [ ] Tiene docstring
- [ ] Tiene al menos una prueba
- [ ] No contiene contraseñas ni credenciales en el código
- [ ] El pull request fue revisado y aprobado por otro integrante
