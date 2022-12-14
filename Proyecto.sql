PGDMP     6                	    z            Proyecto    14.5    14.5 *    $           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            %           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            &           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            '           1262    17054    Proyecto    DATABASE     n   CREATE DATABASE "Proyecto" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_United States.1252';
    DROP DATABASE "Proyecto";
                postgres    false                        2615    2200    bda    SCHEMA        CREATE SCHEMA bda;
    DROP SCHEMA bda;
                postgres    false            (           0    0 
   SCHEMA bda    COMMENT     3   COMMENT ON SCHEMA bda IS 'standard public schema';
                   postgres    false    3            ?            1259    17092    carrera_estudiante    TABLE     Y   CREATE TABLE bda.carrera_estudiante (
    idcarrera integer,
    idestudiante integer
);
 #   DROP TABLE bda.carrera_estudiante;
       bda         heap    postgres    false    3            ?            1259    17078    carreras    TABLE     c   CREATE TABLE bda.carreras (
    idcarrera integer NOT NULL,
    nombrecarrera character varying
);
    DROP TABLE bda.carreras;
       bda         heap    postgres    false    3            ?            1259    17160    carreras_idcarrera_seq    SEQUENCE     ?   ALTER TABLE bda.carreras ALTER COLUMN idcarrera ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME bda.carreras_idcarrera_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            bda          postgres    false    3    213            ?            1259    17083    curso_carrera    TABLE     O   CREATE TABLE bda.curso_carrera (
    idcurso integer,
    idcarrera integer
);
    DROP TABLE bda.curso_carrera;
       bda         heap    postgres    false    3            ?            1259    17089    curso_estudiante    TABLE     g   CREATE TABLE bda.curso_estudiante (
    idcurso integer,
    idestudiante integer,
    nota integer
);
 !   DROP TABLE bda.curso_estudiante;
       bda         heap    postgres    false    3            ?            1259    17075    curso_profesor    TABLE     Q   CREATE TABLE bda.curso_profesor (
    idcurso integer,
    idprofesor integer
);
    DROP TABLE bda.curso_profesor;
       bda         heap    postgres    false    3            ?            1259    17055    cursos    TABLE     ?   CREATE TABLE bda.cursos (
    idcurso integer NOT NULL,
    nombrecurso character varying,
    periodocurso character varying,
    horariocurso character varying,
    modalidadcurso character varying
);
    DROP TABLE bda.cursos;
       bda         heap    postgres    false    3            ?            1259    17161    cursos_idcurso_seq    SEQUENCE     ?   ALTER TABLE bda.cursos ALTER COLUMN idcurso ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME bda.cursos_idcurso_seq
    START WITH 6
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            bda          postgres    false    209    3            ?            1259    17070    profesor    TABLE     ?   CREATE TABLE bda.profesor (
    idprofesor integer NOT NULL,
    nombreprofesor character varying,
    email character varying,
    apellidos character varying,
    cedula character varying
);
    DROP TABLE bda.profesor;
       bda         heap    postgres    false    3            ?            1259    17157    profesor_idprofesor_seq    SEQUENCE     ?   ALTER TABLE bda.profesor ALTER COLUMN idprofesor ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME bda.profesor_idprofesor_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            bda          postgres    false    211    3            ?            1259    17065    student    TABLE     ?   CREATE TABLE bda.student (
    idestudiante integer NOT NULL,
    nombreestudiante character varying,
    email character varying,
    apellidos character varying,
    cedula character varying
);
    DROP TABLE bda.student;
       bda         heap    postgres    false    3            ?            1259    17158    student_idestudiante_seq    SEQUENCE     ?   ALTER TABLE bda.student ALTER COLUMN idestudiante ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME bda.student_idestudiante_seq
    START WITH 3
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            bda          postgres    false    3    210                      0    17092    carrera_estudiante 
   TABLE DATA           B   COPY bda.carrera_estudiante (idcarrera, idestudiante) FROM stdin;
    bda          postgres    false    216   ,/                 0    17078    carreras 
   TABLE DATA           9   COPY bda.carreras (idcarrera, nombrecarrera) FROM stdin;
    bda          postgres    false    213   Q/                 0    17083    curso_carrera 
   TABLE DATA           8   COPY bda.curso_carrera (idcurso, idcarrera) FROM stdin;
    bda          postgres    false    214   ?/                 0    17089    curso_estudiante 
   TABLE DATA           D   COPY bda.curso_estudiante (idcurso, idestudiante, nota) FROM stdin;
    bda          postgres    false    215   ?/                 0    17075    curso_profesor 
   TABLE DATA           :   COPY bda.curso_profesor (idcurso, idprofesor) FROM stdin;
    bda          postgres    false    212   ?/                 0    17055    cursos 
   TABLE DATA           _   COPY bda.cursos (idcurso, nombrecurso, periodocurso, horariocurso, modalidadcurso) FROM stdin;
    bda          postgres    false    209   +0                 0    17070    profesor 
   TABLE DATA           U   COPY bda.profesor (idprofesor, nombreprofesor, email, apellidos, cedula) FROM stdin;
    bda          postgres    false    211   ?0                 0    17065    student 
   TABLE DATA           X   COPY bda.student (idestudiante, nombreestudiante, email, apellidos, cedula) FROM stdin;
    bda          postgres    false    210   41       )           0    0    carreras_idcarrera_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('bda.carreras_idcarrera_seq', 3, true);
          bda          postgres    false    219            *           0    0    cursos_idcurso_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('bda.cursos_idcurso_seq', 7, true);
          bda          postgres    false    220            +           0    0    profesor_idprofesor_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('bda.profesor_idprofesor_seq', 2, true);
          bda          postgres    false    217            ,           0    0    student_idestudiante_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('bda.student_idestudiante_seq', 3, true);
          bda          postgres    false    218            ?           2606    17102    carreras idcarreras_pk 
   CONSTRAINT     X   ALTER TABLE ONLY bda.carreras
    ADD CONSTRAINT idcarreras_pk PRIMARY KEY (idcarrera);
 =   ALTER TABLE ONLY bda.carreras DROP CONSTRAINT idcarreras_pk;
       bda            postgres    false    213            |           2606    17096    cursos idcursos_pk 
   CONSTRAINT     R   ALTER TABLE ONLY bda.cursos
    ADD CONSTRAINT idcursos_pk PRIMARY KEY (idcurso);
 9   ALTER TABLE ONLY bda.cursos DROP CONSTRAINT idcursos_pk;
       bda            postgres    false    209            ~           2606    17098    student idestudiante_pk 
   CONSTRAINT     \   ALTER TABLE ONLY bda.student
    ADD CONSTRAINT idestudiante_pk PRIMARY KEY (idestudiante);
 >   ALTER TABLE ONLY bda.student DROP CONSTRAINT idestudiante_pk;
       bda            postgres    false    210            ?           2606    17100    profesor idprofesor_pk 
   CONSTRAINT     Y   ALTER TABLE ONLY bda.profesor
    ADD CONSTRAINT idprofesor_pk PRIMARY KEY (idprofesor);
 =   ALTER TABLE ONLY bda.profesor DROP CONSTRAINT idprofesor_pk;
       bda            postgres    false    211            ?           2606    17148 0   carrera_estudiante fk_carreraestudiante_carreras    FK CONSTRAINT     ?   ALTER TABLE ONLY bda.carrera_estudiante
    ADD CONSTRAINT fk_carreraestudiante_carreras FOREIGN KEY (idcarrera) REFERENCES bda.carreras(idcarrera);
 W   ALTER TABLE ONLY bda.carrera_estudiante DROP CONSTRAINT fk_carreraestudiante_carreras;
       bda          postgres    false    213    216    3202            ?           2606    17143 /   carrera_estudiante fk_carreraestudiante_student    FK CONSTRAINT     ?   ALTER TABLE ONLY bda.carrera_estudiante
    ADD CONSTRAINT fk_carreraestudiante_student FOREIGN KEY (idestudiante) REFERENCES bda.student(idestudiante);
 V   ALTER TABLE ONLY bda.carrera_estudiante DROP CONSTRAINT fk_carreraestudiante_student;
       bda          postgres    false    216    3198    210            ?           2606    17103     curso_profesor fk_curso_profesor    FK CONSTRAINT        ALTER TABLE ONLY bda.curso_profesor
    ADD CONSTRAINT fk_curso_profesor FOREIGN KEY (idcurso) REFERENCES bda.cursos(idcurso);
 G   ALTER TABLE ONLY bda.curso_profesor DROP CONSTRAINT fk_curso_profesor;
       bda          postgres    false    212    209    3196            ?           2606    17128 %   curso_carrera fk_cursocarrera_carrera    FK CONSTRAINT     ?   ALTER TABLE ONLY bda.curso_carrera
    ADD CONSTRAINT fk_cursocarrera_carrera FOREIGN KEY (idcarrera) REFERENCES bda.carreras(idcarrera);
 L   ALTER TABLE ONLY bda.curso_carrera DROP CONSTRAINT fk_cursocarrera_carrera;
       bda          postgres    false    214    213    3202            ?           2606    17123 $   curso_carrera fk_cursocarrera_cursos    FK CONSTRAINT     ?   ALTER TABLE ONLY bda.curso_carrera
    ADD CONSTRAINT fk_cursocarrera_cursos FOREIGN KEY (idcurso) REFERENCES bda.cursos(idcurso);
 K   ALTER TABLE ONLY bda.curso_carrera DROP CONSTRAINT fk_cursocarrera_cursos;
       bda          postgres    false    214    3196    209            ?           2606    17133 *   curso_estudiante fk_cursoestudiante_cursos    FK CONSTRAINT     ?   ALTER TABLE ONLY bda.curso_estudiante
    ADD CONSTRAINT fk_cursoestudiante_cursos FOREIGN KEY (idcurso) REFERENCES bda.cursos(idcurso);
 Q   ALTER TABLE ONLY bda.curso_estudiante DROP CONSTRAINT fk_cursoestudiante_cursos;
       bda          postgres    false    209    3196    215            ?           2606    17138 +   curso_estudiante fk_cursoestudiante_student    FK CONSTRAINT     ?   ALTER TABLE ONLY bda.curso_estudiante
    ADD CONSTRAINT fk_cursoestudiante_student FOREIGN KEY (idestudiante) REFERENCES bda.student(idestudiante);
 R   ALTER TABLE ONLY bda.curso_estudiante DROP CONSTRAINT fk_cursoestudiante_student;
       bda          postgres    false    3198    215    210            ?           2606    17108 (   curso_profesor fk_cursoprofesor_profesor    FK CONSTRAINT     ?   ALTER TABLE ONLY bda.curso_profesor
    ADD CONSTRAINT fk_cursoprofesor_profesor FOREIGN KEY (idprofesor) REFERENCES bda.profesor(idprofesor);
 O   ALTER TABLE ONLY bda.curso_profesor DROP CONSTRAINT fk_cursoprofesor_profesor;
       bda          postgres    false    212    211    3200                  x?3?4?2?4?????? ??         &   x?3???2??MMN?2???K)-.)?L??????? t??         3   x?ȱ  ??;?2??/?k?Fi?X8??Μ9sVиS?C??         %   x?3?4??0?2?P&ʔӐ??BB?=... ?'6            x?3?4?2bCNC.c 6?=... (         ?   x?m?A
?@E??)zaڪ{???M?	6?NJ&??S??$?????(s˒k? Iǉa??????t?`B3?_NV??i,G????E?޽??y???rI?>WKwX&L?⥂P?B????V??s?N??E0         b   x?m˱
?  ???cB-0?Z??֖?2J㔠?????4<Qʞ?3?Pj|?8???敥???+????R?B7l?_$?Ŀ?~FY甩-?">~?&{         _   x?3????K,?H???JJ,*J?+I-v??+K????K???t??r??q?g?&rfe??%楤V?(???????rf?f?q?(?x? -(?     