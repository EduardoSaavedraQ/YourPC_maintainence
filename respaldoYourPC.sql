--
-- PostgreSQL database dump
--

-- Dumped from database version 15.1
-- Dumped by pg_dump version 15.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: acciones_awp; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.acciones_awp (
    pk_num_accion_admin bigint NOT NULL,
    fk_nickname_admin character varying(20) NOT NULL,
    fecha_accion_admin date DEFAULT now() NOT NULL,
    descripcion_accion_admin text
);


ALTER TABLE public.acciones_awp OWNER TO postgres;

--
-- Name: acciones_awp_pk_num_accion_admin; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.acciones_awp_pk_num_accion_admin
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.acciones_awp_pk_num_accion_admin OWNER TO postgres;

--
-- Name: acciones_awp_pk_num_accion_admin; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.acciones_awp_pk_num_accion_admin OWNED BY public.acciones_awp.pk_num_accion_admin;


--
-- Name: acciones_usuario; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.acciones_usuario (
    pk_num_accion_usua bigint NOT NULL,
    fk_nickname_usua character varying(20) NOT NULL,
    fecha_accion_usua date DEFAULT now() NOT NULL,
    descripcion_accion_usua text
);


ALTER TABLE public.acciones_usuario OWNER TO postgres;

--
-- Name: acciones_usuario_pk_num_accion_usua; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.acciones_usuario_pk_num_accion_usua
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.acciones_usuario_pk_num_accion_usua OWNER TO postgres;

--
-- Name: acciones_usuario_pk_num_accion_usua; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.acciones_usuario_pk_num_accion_usua OWNED BY public.acciones_usuario.pk_num_accion_usua;


--
-- Name: awp; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.awp (
    pk_nickname_admin character varying(20) NOT NULL,
    correo_admin character varying(40) NOT NULL,
    contrasenia_admin character varying(15) NOT NULL,
    fecha_registro_admin date DEFAULT now() NOT NULL
);


ALTER TABLE public.awp OWNER TO postgres;

--
-- Name: awp_usuario; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.awp_usuario (
    fk_nickname_admin character varying(20) NOT NULL,
    fk_nickname_usua character varying(20) NOT NULL,
    "Tipo_de_accion" character varying(15) NOT NULL
);


ALTER TABLE public.awp_usuario OWNER TO postgres;

--
-- Name: componente; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.componente (
    pk_nombre_componente character varying(50) NOT NULL,
    descripcion_componente text NOT NULL,
    imagen bytea
);


ALTER TABLE public.componente OWNER TO postgres;

--
-- Name: componente_precio_vendedor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.componente_precio_vendedor (
    fk_nombre_componente character varying(50) NOT NULL,
    precio real NOT NULL,
    vendedor character varying(30) NOT NULL
);


ALTER TABLE public.componente_precio_vendedor OWNER TO postgres;

--
-- Name: usuario; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.usuario (
    pk_nickname character varying(20) NOT NULL,
    correo character varying(40) NOT NULL,
    contrasenia character varying(15) NOT NULL,
    fecha_registro date DEFAULT now() NOT NULL
);


ALTER TABLE public.usuario OWNER TO postgres;

--
-- Name: usuario_componente; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.usuario_componente (
    fk_nickname_usua character varying(20) NOT NULL,
    fk_nombre_componente character varying(50) NOT NULL
);


ALTER TABLE public.usuario_componente OWNER TO postgres;

--
-- Name: acciones_awp pk_num_accion_admin; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.acciones_awp ALTER COLUMN pk_num_accion_admin SET DEFAULT nextval('public.acciones_awp_pk_num_accion_admin'::regclass);


--
-- Name: acciones_usuario pk_num_accion_usua; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.acciones_usuario ALTER COLUMN pk_num_accion_usua SET DEFAULT nextval('public.acciones_usuario_pk_num_accion_usua'::regclass);


--
-- Data for Name: acciones_awp; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.acciones_awp (pk_num_accion_admin, fk_nickname_admin, fecha_accion_admin, descripcion_accion_admin) FROM stdin;
\.


--
-- Data for Name: acciones_usuario; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.acciones_usuario (pk_num_accion_usua, fk_nickname_usua, fecha_accion_usua, descripcion_accion_usua) FROM stdin;
\.


--
-- Data for Name: awp; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.awp (pk_nickname_admin, correo_admin, contrasenia_admin, fecha_registro_admin) FROM stdin;
\.


--
-- Data for Name: awp_usuario; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.awp_usuario (fk_nickname_admin, fk_nickname_usua, "Tipo_de_accion") FROM stdin;
\.


--
-- Data for Name: componente; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.componente (pk_nombre_componente, descripcion_componente, imagen) FROM stdin;
\.


--
-- Data for Name: componente_precio_vendedor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.componente_precio_vendedor (fk_nombre_componente, precio, vendedor) FROM stdin;
\.


--
-- Data for Name: usuario; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.usuario (pk_nickname, correo, contrasenia, fecha_registro) FROM stdin;
emiliano	epihua6989@gmail.com	123456789	2023-04-19
qqq	qre@gmail.com	123456789	2023-04-19
epihua	emilianodiaz739@gmail.com	123456789	2023-05-16
elkekas2000	elkekas2000@gmail.com	123456789	2023-05-15
lalonganiza	eduardo@example.com	1234567	2023-05-16
\.


--
-- Data for Name: usuario_componente; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.usuario_componente (fk_nickname_usua, fk_nombre_componente) FROM stdin;
\.


--
-- Name: acciones_awp_pk_num_accion_admin; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.acciones_awp_pk_num_accion_admin', 1, false);


--
-- Name: acciones_usuario_pk_num_accion_usua; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.acciones_usuario_pk_num_accion_usua', 1, false);


--
-- Name: acciones_awp acciones_awp_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.acciones_awp
    ADD CONSTRAINT acciones_awp_pkey PRIMARY KEY (pk_num_accion_admin);


--
-- Name: acciones_usuario acciones_usuario_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.acciones_usuario
    ADD CONSTRAINT acciones_usuario_pkey PRIMARY KEY (pk_num_accion_usua);


--
-- Name: awp awp_correo_admin_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.awp
    ADD CONSTRAINT awp_correo_admin_key UNIQUE (correo_admin);


--
-- Name: awp awp_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.awp
    ADD CONSTRAINT awp_pkey PRIMARY KEY (pk_nickname_admin);


--
-- Name: componente componente_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.componente
    ADD CONSTRAINT componente_pkey PRIMARY KEY (pk_nombre_componente);


--
-- Name: usuario usuario_correo_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_correo_key UNIQUE (correo);


--
-- Name: usuario usuario_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_pkey PRIMARY KEY (pk_nickname);


--
-- Name: acciones_awp acciones_awp_fk_nickname_admin_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.acciones_awp
    ADD CONSTRAINT acciones_awp_fk_nickname_admin_fkey FOREIGN KEY (fk_nickname_admin) REFERENCES public.awp(pk_nickname_admin);


--
-- Name: acciones_usuario acciones_usuario_fk_nickname_usua_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.acciones_usuario
    ADD CONSTRAINT acciones_usuario_fk_nickname_usua_fkey FOREIGN KEY (fk_nickname_usua) REFERENCES public.usuario(pk_nickname);


--
-- Name: awp_usuario awp_usuario_fk_nickname_admin_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.awp_usuario
    ADD CONSTRAINT awp_usuario_fk_nickname_admin_fkey FOREIGN KEY (fk_nickname_admin) REFERENCES public.awp(pk_nickname_admin);


--
-- Name: awp_usuario awp_usuario_fk_nickname_usua_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.awp_usuario
    ADD CONSTRAINT awp_usuario_fk_nickname_usua_fkey FOREIGN KEY (fk_nickname_usua) REFERENCES public.usuario(pk_nickname);


--
-- Name: componente_precio_vendedor componente_precio_vendedor_fk_nombre_componente_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.componente_precio_vendedor
    ADD CONSTRAINT componente_precio_vendedor_fk_nombre_componente_fkey FOREIGN KEY (fk_nombre_componente) REFERENCES public.componente(pk_nombre_componente);


--
-- Name: usuario_componente usuario_componente_fk_nickname_usua_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuario_componente
    ADD CONSTRAINT usuario_componente_fk_nickname_usua_fkey FOREIGN KEY (fk_nickname_usua) REFERENCES public.usuario(pk_nickname);


--
-- Name: usuario_componente usuario_componente_fk_nombre_componente_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuario_componente
    ADD CONSTRAINT usuario_componente_fk_nombre_componente_fkey FOREIGN KEY (fk_nombre_componente) REFERENCES public.componente(pk_nombre_componente);


--
-- PostgreSQL database dump complete
--

