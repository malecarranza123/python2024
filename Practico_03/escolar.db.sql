BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `profesores` (
	`dni_id`	INTEGER,
	`nombre`	TEXT NOT NULL,
	`apellido`	TEXT NOT NULL,
	`curso`	TEXT NOT NULL,
	`estado`	TEXT NOT NULL,
	`email`	TEXT NOT NULL,
	PRIMARY KEY(`dni_id`)
);
CREATE TABLE IF NOT EXISTS `materias` (
	`id_materia`	INTEGER,
	`nombre`	TEXT NOT NULL,
	`curso`	TEXT NOT NULL,
	`descripcion`	TEXT NOT NULL,
	`horario`	TEXT NOT NULL,
	PRIMARY KEY(`id_materia`)
);
CREATE TABLE IF NOT EXISTS `estudiantes` (
	`legajo_id`	INTEGER NOT NULL,
	`dni`	INTEGER NOT NULL,
	`nombre`	TEXT NOT NULL,
	`apellido`	TEXT NOT NULL,
	`edad`	INTEGER NOT NULL,
	`fecha_nacimiento`	DATE NOT NULL,
	`curso`	TEXT NOT NULL,
	`estado`	TEXT NOT NULL,
	`email`	TEXT NOT NULL,
	PRIMARY KEY(`legajo_id`)
);
CREATE TABLE IF NOT EXISTS `calificaciones` (
	`id_estudiante`	INTEGER,
	`id_materia`	INTEGER NOT NULL,
	`nota`	FLOAT NOT NULL,
	`fecha`	DATE NOT NULL,
	PRIMARY KEY(`id_estudiante`)
);
COMMIT;
