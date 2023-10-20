CREATE TABLE public.estado_archivos (
	id serial4 NOT NULL,
	nombre_archivo varchar NOT NULL,
	nuevo_archivo varchar NOT NULL,
	estado varchar NOT NULL,
	extension_original varchar NULL,
	extension_nueva varchar NULL,
	fecha_carga timestamp NULL,
	fecha_procesamiento timestamp NULL,
	CONSTRAINT estado_archivos_pk PRIMARY KEY (id),
	CONSTRAINT estado_archivos_un UNIQUE (id)
);