CREATE TABLE public.estado_archivos (
	id serial4 NOT NULL,
	nombre_archivo varchar NOT NULL,
	nuevo_archivo varchar NOT NULL,
	estado varchar NOT NULL,
	extension_original varchar NULL,
	extension_nueva varchar NULL,
	fecha_carga timestamp NULL,
	fecha_procesamiento timestamp NULL,
	CONSTRAINT estado_archivos_pk PRIMARY KEY (id)
);

CREATE TABLE public.users (
    id bigserial NOT NULL,
    username varchar NOT NULL,
    email varchar NOT NULL,
    password varchar NOT NULL,
    CONSTRAINT users_pk PRIMARY KEY (id),
	CONSTRAINT users_user_un UNIQUE (username),
	CONSTRAINT users_email_un UNIQUE (email)

)