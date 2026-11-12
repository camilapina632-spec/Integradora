-- 03_consultas.sql

-- Proyecto: ControlLibro

-- Consultas para atender los casos de uso de la biblioteca escolar.

USE ControlLibro;

-- =============================================
-- CONSULTA 1: Consultar préstamos con JOIN
-- Caso de uso: Consultar historial de préstamos.
-- Muestra alumno, libro y bibliotecario encargado.
-- =============================================

SELECT
p.id_prestamo,
CONCAT(a.nombre, ' ', a.apellido) AS alumno,
l.titulo AS libro,
CONCAT(b.nombre, ' ', b.apellido) AS bibliotecario,
p.fecha_prestamo,
p.fecha_devolucion_prevista,
p.fecha_devolucion_real
FROM prestamos p
INNER JOIN alumnos a
ON p.id_alumno = a.id_alumno
INNER JOIN libros l
ON p.id_libro = l.id_libro
INNER JOIN bibliotecarios b
ON p.id_bibliotecario = b.id_bibliotecario;

-- =============================================
-- CONSULTA 2: Alumnos con más de un préstamo
-- Caso de uso: Consultar actividad de los alumnos.
-- Utiliza GROUP BY y HAVING.
-- =============================================

SELECT
a.id_alumno,
CONCAT(a.nombre, ' ', a.apellido) AS alumno,
COUNT(p.id_prestamo) AS total_prestamos
FROM alumnos a
INNER JOIN prestamos p
ON a.id_alumno = p.id_alumno
GROUP BY
a.id_alumno,
a.nombre,
a.apellido
HAVING COUNT(p.id_prestamo) > 1;

-- =============================================
-- CONSULTA 3: Libros que nunca se han prestado
-- Caso de uso: Consultar libros sin historial de préstamos.
-- Utiliza una subconsulta.
-- =============================================

SELECT
l.id_libro,
l.titulo,
l.autor
FROM libros l
WHERE l.id_libro NOT IN (
SELECT p.id_libro
FROM prestamos p
);

-- =============================================
-- CONSULTA 4: Préstamos activos
-- Caso de uso: Consultar libros actualmente prestados.
-- =============================================

SELECT
p.id_prestamo,
l.titulo AS libro,
CONCAT(a.nombre, ' ', a.apellido) AS alumno,
p.fecha_prestamo,
p.fecha_devolucion_prevista
FROM prestamos p
INNER JOIN libros l
ON p.id_libro = l.id_libro
INNER JOIN alumnos a
ON p.id_alumno = a.id_alumno
WHERE p.fecha_devolucion_real IS NULL;

-- =============================================
-- CONSULTA 5: Crear vista del historial de préstamos
-- Caso de uso: Consultar el historial de préstamos
-- de manera sencilla.
-- =============================================

CREATE OR REPLACE VIEW vista_historial_prestamos AS
SELECT
p.id_prestamo,
l.titulo AS libro,
CONCAT(a.nombre, ' ', a.apellido) AS alumno,
CONCAT(b.nombre, ' ', b.apellido) AS bibliotecario,
p.fecha_prestamo,
p.fecha_devolucion_prevista,
p.fecha_devolucion_real
FROM prestamos p
INNER JOIN libros l
ON p.id_libro = l.id_libro
INNER JOIN alumnos a
ON p.id_alumno = a.id_alumno
INNER JOIN bibliotecarios b
ON p.id_bibliotecario = b.id_bibliotecario;

-- Consultar la vista:
SELECT * FROM vista_historial_prestamos;