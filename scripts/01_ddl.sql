Script DDL - ControlLibro

CREATE DATABASE IF NOT EXISTS ControlLibro;
USE ControlLibro;

-- =========================================
-- TABLA: LIBROS
-- =========================================

CREATE TABLE IF NOT EXISTS libros (
    id_libro INT AUTO_INCREMENT PRIMARY KEY,
    codigo_inventario VARCHAR(30) NOT NULL UNIQUE,
    titulo VARCHAR(150) NOT NULL,
    autor VARCHAR(120) NOT NULL,
    isbn VARCHAR(20),
    anio_publicacion INT,

    CONSTRAINT chk_anio_libro
        CHECK (anio_publicacion IS NULL OR anio_publicacion >= 1000)
) ENGINE=InnoDB;


-- =========================================
-- TABLA: ALUMNOS
-- =========================================

CREATE TABLE IF NOT EXISTS alumnos (
    id_alumno INT AUTO_INCREMENT PRIMARY KEY,
    matricula VARCHAR(30) NOT NULL UNIQUE,
    nombre VARCHAR(80) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    grado INT NOT NULL,
    grupo VARCHAR(10) NOT NULL,

    CONSTRAINT chk_grado
        CHECK (grado BETWEEN 1 AND 3)
) ENGINE=InnoDB;


-- =========================================
-- TABLA: BIBLIOTECARIOS
-- =========================================

CREATE TABLE IF NOT EXISTS bibliotecarios (
    id_bibliotecario INT AUTO_INCREMENT PRIMARY KEY,
    numero_empleado VARCHAR(30) NOT NULL UNIQUE,
    nombre VARCHAR(80) NOT NULL,
    apellido VARCHAR(100) NOT NULL
) ENGINE=InnoDB;


-- =========================================
-- TABLA: PRESTAMOS
-- =========================================

CREATE TABLE IF NOT EXISTS prestamos (
    id_prestamo INT AUTO_INCREMENT PRIMARY KEY,

    id_libro INT NOT NULL,
    id_alumno INT NOT NULL,
    id_bibliotecario INT NOT NULL,

    fecha_prestamo DATE NOT NULL,
    fecha_devolucion_prevista DATE NOT NULL,
    fecha_devolucion_real DATE DEFAULT NULL,

    CONSTRAINT fk_prestamo_libro
        FOREIGN KEY (id_libro)
        REFERENCES libros(id_libro)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,

    CONSTRAINT fk_prestamo_alumno
        FOREIGN KEY (id_alumno)
        REFERENCES alumnos(id_alumno)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,

    CONSTRAINT fk_prestamo_bibliotecario
        FOREIGN KEY (id_bibliotecario)
        REFERENCES bibliotecarios(id_bibliotecario)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,

    CONSTRAINT chk_fecha_prevista
        CHECK (fecha_devolucion_prevista >= fecha_prestamo),

    CONSTRAINT chk_fecha_real
        CHECK (
            fecha_devolucion_real IS NULL
            OR fecha_devolucion_real >= fecha_prestamo
        ),

    INDEX idx_prestamo_libro (id_libro),
    INDEX idx_prestamo_alumno (id_alumno),
    INDEX idx_prestamo_bibliotecario (id_bibliotecario),
    INDEX idx_prestamo_fecha (fecha_devolucion_prevista)
) ENGINE=InnoDB;