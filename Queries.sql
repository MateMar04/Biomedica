DROP DATABASE IF EXISTS BIOMEDICA;

CREATE DATABASE BIOMEDICA;

USE BIOMEDICA;

CREATE TABLE SEXO
(
    ID           INT AUTO_INCREMENT PRIMARY KEY,
    NOMBRE       VARCHAR(15),
    DESCRIPCCION VARCHAR(15)
);

CREATE TABLE TELEFONO
(
    ID     INT AUTO_INCREMENT PRIMARY KEY,
    NUMERO BIGINT
);

CREATE TABLE DOMICILIO
(
    ID           INT AUTO_INCREMENT PRIMARY KEY,
    CALLE        VARCHAR(30),
    ALTURA       INT,
    N_PISO       INT,
    DEPARTAMENTO VARCHAR(15)
);

CREATE TABLE UNIDAD_DE_MEDIDA
(
    ID          INT AUTO_INCREMENT PRIMARY KEY,
    UNIDAD      VARCHAR(15),
    DESCRIPCION VARCHAR(30)
);

CREATE TABLE METODO
(
    ID           INT AUTO_INCREMENT PRIMARY KEY,
    NOMBRE       VARCHAR(30),
    DESCRIPCCION VARCHAR(30)
);

CREATE TABLE EXTRACCIONISTA
(
    ID       INT AUTO_INCREMENT PRIMARY KEY,
    NOMBRE   VARCHAR(50),
    APELLIDO VARCHAR(50)
);

CREATE TABLE ESTADO_DE_SOLICITUD
(
    ID           INT AUTO_INCREMENT PRIMARY KEY,
    NOMBRE       VARCHAR(20),
    DESCRIPCCION VARCHAR(40)
);

CREATE TABLE MEDICO
(
    ID        INT AUTO_INCREMENT PRIMARY KEY,
    MATRICULA VARCHAR(13),
    NOMBRE    VARCHAR(50),
    APELLIDO  VARCHAR(50)
);

CREATE TABLE TIPO_DE_DOCUMENTO
(
    ID          INT AUTO_INCREMENT PRIMARY KEY,
    NOMBRE      VARCHAR(15),
    DESCRIPCION VARCHAR(15)
);

CREATE TABLE ESTUDIO
(
    ID                  INT AUTO_INCREMENT PRIMARY KEY,
    NOMBRE              VARCHAR(50),
    DESCRIPCCION        VARCHAR(50),
    LIMITE_INFERIOR     INT,
    LIMITE_SUPERIOR     INT,
    ID_METODO           INT,
    ID_UNIDAD_DE_MEDIDA INT,
    CONSTRAINT `ESTUDIO->METODO` FOREIGN KEY (ID_METODO) REFERENCES METODO (ID),
    CONSTRAINT `ESTUDIO->UNIDAD_DE_MEDIDA` FOREIGN KEY (ID_UNIDAD_DE_MEDIDA) REFERENCES UNIDAD_DE_MEDIDA (ID)
);

CREATE TABLE RESULTADO
(
    ID            INT AUTO_INCREMENT PRIMARY KEY,
    VALOR_HALLADO FLOAT,
    FECHA         DATE,
    ID_ESTUDIO    INT,
    OBSERVACION   TEXT,
    CONSTRAINT `RESULTADO->ESTUDIO` FOREIGN KEY (ID_ESTUDIO) REFERENCES ESTUDIO (ID)
);

CREATE TABLE MUESTRA
(
    ID                    INT AUTO_INCREMENT PRIMARY KEY,
    DESCRIPCCION          VARCHAR(50),
    FECHA_HORA_EXTRACCION DATE,
    ID_RESULTADO          INT,
    CONSTRAINT `MUESTRA->RESULTADO` FOREIGN KEY (ID_RESULTADO) REFERENCES RESULTADO (ID)
);

CREATE TABLE PACIENTE
(
    ID                   INT PRIMARY KEY AUTO_INCREMENT,
    N_DOCUMENTO          INT,
    NOMBRE               VARCHAR(50),
    APELLIDO             VARCHAR(50),
    ID_SEXO              INT,
    ID_DOMICILIO         INT,
    ID_TELEFONO          INT,
    ID_TIPO_DE_DOCUMENTO INT,
    EMAIL                VARCHAR(100),
    CONSTRAINT `PACIENTE->SEXO` FOREIGN KEY (ID_SEXO) REFERENCES SEXO (ID),
    CONSTRAINT `PACIENTE->DOMICILIO` FOREIGN KEY (ID_DOMICILIO) REFERENCES DOMICILIO (ID),
    CONSTRAINT `PACIENTE->TELEFONO` FOREIGN KEY (ID_TELEFONO) REFERENCES TELEFONO (ID),
    CONSTRAINT `PACIENTE->TIPO_DE_DOCUMENTO` FOREIGN KEY (ID_TIPO_DE_DOCUMENTO) REFERENCES TIPO_DE_DOCUMENTO (ID)
);

CREATE TABLE SOLICITUD
(
    ID                      INT AUTO_INCREMENT PRIMARY KEY,
    RECETA                  VARCHAR(100),
    ID_PACIENTE             INT,
    ID_EXTRACCIONISTA       INT,
    ID_ESTADO               INT,
    ID_MEDICO               INT,
    FECHA_HORA_INICIO       DATETIME,
    FECHA_HORA_FINALIZACION DATETIME,
    CAP                     VARCHAR(8),
    CONSTRAINT `SOLICITUD->PACIENTE` FOREIGN KEY (ID_PACIENTE) REFERENCES PACIENTE (ID),
    CONSTRAINT `SOLICITUD->EXTRACCIONISTA` FOREIGN KEY (ID_EXTRACCIONISTA) REFERENCES EXTRACCIONISTA (ID),
    CONSTRAINT `SOLICITUD->ESTADO` FOREIGN KEY (ID_ESTADO) REFERENCES ESTADO_DE_SOLICITUD (ID),
    CONSTRAINT `SOLICITUD->MEDICO` FOREIGN KEY (ID_MEDICO) REFERENCES MEDICO (ID)
);

INSERT INTO SEXO (NOMBRE, DESCRIPCCION)
VALUES ('MASCULINO', 'HOMBRE');
INSERT INTO SEXO (NOMBRE, DESCRIPCCION)
VALUES ('FEMENINO', 'MUJER');
INSERT INTO SEXO (NOMBRE, DESCRIPCCION)
VALUES ('OTRO', 'OTRO');

INSERT INTO TELEFONO (NUMERO)
VALUES (3513497968);
INSERT INTO TELEFONO (NUMERO)
VALUES (3517544670);
INSERT INTO TELEFONO (NUMERO)
VALUES (3516791006);

INSERT INTO DOMICILIO (CALLE, ALTURA)
VALUES ('LONCOCHE', 8136);
INSERT INTO DOMICILIO (CALLE, ALTURA)
VALUES ('LONCOCHE', 8137);
INSERT INTO DOMICILIO (CALLE, ALTURA)
VALUES ('LONCOCHE', 8138);

INSERT INTO UNIDAD_DE_MEDIDA (UNIDAD, DESCRIPCION)
VALUES ('millones/mm³', 'MILLONES POR MILIMETRO CUBCIO');
INSERT INTO UNIDAD_DE_MEDIDA (UNIDAD, DESCRIPCION)
VALUES ('g/dL', 'GRAMOS POR DECILITRO');
INSERT INTO UNIDAD_DE_MEDIDA (UNIDAD, DESCRIPCION)
VALUES ('mg/dL', 'MILIGRAMO POR DECILITRO');

INSERT INTO METODO (NOMBRE, DESCRIPCCION)
VALUES ('ENZIMATICO - AUTOANALIZADOR', 'UwU');
INSERT INTO METODO (NOMBRE, DESCRIPCCION)
VALUES ('COLORIMETRICO', 'OwO');

INSERT INTO EXTRACCIONISTA (NOMBRE, APELLIDO)
VALUES ('YANINA', 'RIBONE');
INSERT INTO EXTRACCIONISTA (NOMBRE, APELLIDO)
VALUES ('LAURA', 'RIBONE');
INSERT INTO EXTRACCIONISTA (NOMBRE, APELLIDO)
VALUES ('ELISA', 'RIBONE');

INSERT INTO ESTADO_DE_SOLICITUD (NOMBRE, DESCRIPCCION)
VALUES ('EN ANALISIS', 'EL ESTUDIO ESTA SIENDO REALIZADO');
INSERT INTO ESTADO_DE_SOLICITUD (NOMBRE, DESCRIPCCION)
VALUES ('FINALIZADO', 'EL ESTUDIO HA FINALIZADO');
INSERT INTO ESTADO_DE_SOLICITUD (NOMBRE, DESCRIPCCION)
VALUES ('PENDIENTE', 'EL ESTUDIO NO HA COMENZADO');

INSERT INTO MEDICO (MATRICULA, NOMBRE, APELLIDO)
VALUES ('sDSAoj907SSDs', 'ARIEL', 'GALAVERNA');
INSERT INTO MEDICO (MATRICULA, NOMBRE, APELLIDO)
VALUES ('sDSAoDSA7SSDs', 'PAOLA', 'MONTEVERDE');
INSERT INTO MEDICO (MATRICULA, NOMBRE, APELLIDO)
VALUES ('sKLÑDSA07SSDs', 'ALVARO', 'GALAVERNA');

INSERT INTO TIPO_DE_DOCUMENTO (NOMBRE, DESCRIPCION)
VALUES ('DNI', ':)');
INSERT INTO TIPO_DE_DOCUMENTO (NOMBRE, DESCRIPCION)
VALUES ('PASAPORTE', ':|');
INSERT INTO TIPO_DE_DOCUMENTO (NOMBRE, DESCRIPCION)
VALUES ('CUIT', ':(');

INSERT INTO ESTUDIO (NOMBRE, DESCRIPCCION, LIMITE_INFERIOR, LIMITE_SUPERIOR, ID_METODO, ID_UNIDAD_DE_MEDIDA)
VALUES ('COLESTEROL L.D.L', 'A', 1, 2, 1, 3);
INSERT INTO ESTUDIO (NOMBRE, DESCRIPCCION, LIMITE_INFERIOR, LIMITE_SUPERIOR, ID_METODO, ID_UNIDAD_DE_MEDIDA)
VALUES ('COLESTEROL H.D.L', 'B', 1, 2, 1, 3);
INSERT INTO ESTUDIO (NOMBRE, DESCRIPCCION, LIMITE_INFERIOR, LIMITE_SUPERIOR, ID_METODO, ID_UNIDAD_DE_MEDIDA)
VALUES ('MAGNEISIO', 'C', 1, 2, 2, 1);

INSERT INTO RESULTADO (VALOR_HALLADO, FECHA, ID_ESTUDIO, OBSERVACION)
VALUES (0.5, '2001/01/01', 1, 'ESTAS DE RUTA');
INSERT INTO RESULTADO (VALOR_HALLADO, FECHA, ID_ESTUDIO, OBSERVACION)
VALUES (8, '2002/02/02', 2, 'TAMOS CIELO');
INSERT INTO RESULTADO (VALOR_HALLADO, FECHA, ID_ESTUDIO, OBSERVACION)
VALUES (5, '2003/03/03', 3, 'NASHE');

INSERT INTO SEXO (NOMBRE, DESCRIPCCION)
VALUES ('MASCULINO', 'HOMBRE');
INSERT INTO SEXO (NOMBRE, DESCRIPCCION)
VALUES ('FEMENINO', 'MUJER');
INSERT INTO SEXO (NOMBRE, DESCRIPCCION)
VALUES ('OTRO', 'OTRO');

INSERT INTO TELEFONO (NUMERO)
VALUES (3513497968);
INSERT INTO TELEFONO (NUMERO)
VALUES (3517544670);
INSERT INTO TELEFONO (NUMERO)
VALUES (3516791006);

INSERT INTO DOMICILIO (CALLE, ALTURA)
VALUES ('LONCOCHE', 8136);
INSERT INTO DOMICILIO (CALLE, ALTURA)
VALUES ('LONCOCHE', 8137);
INSERT INTO DOMICILIO (CALLE, ALTURA)
VALUES ('LONCOCHE', 8138);

INSERT INTO UNIDAD_DE_MEDIDA (UNIDAD, DESCRIPCION)
VALUES ('millones/mm³', 'MILLONES POR MILIMETRO CUBCIO');
INSERT INTO UNIDAD_DE_MEDIDA (UNIDAD, DESCRIPCION)
VALUES ('g/dL', 'GRAMOS POR DECILITRO');
INSERT INTO UNIDAD_DE_MEDIDA (UNIDAD, DESCRIPCION)
VALUES ('mg/dL', 'MILIGRAMO POR DECILITRO');

INSERT INTO METODO (NOMBRE, DESCRIPCCION)
VALUES ('ENZIMATICO - AUTOANALIZADOR', 'UwU');
INSERT INTO METODO (NOMBRE, DESCRIPCCION)
VALUES ('COLORIMETRICO', 'OwO');

INSERT INTO EXTRACCIONISTA (NOMBRE, APELLIDO)
VALUES ('YANINA', 'RIBONE');
INSERT INTO EXTRACCIONISTA (NOMBRE, APELLIDO)
VALUES ('LAURA', 'RIBONE');
INSERT INTO EXTRACCIONISTA (NOMBRE, APELLIDO)
VALUES ('ELISA', 'RIBONE');

INSERT INTO ESTADO_DE_SOLICITUD (NOMBRE, DESCRIPCCION)
VALUES ('EN ANALISIS', 'EL ESTUDIO ESTA SIENDO REALIZADO');
INSERT INTO ESTADO_DE_SOLICITUD (NOMBRE, DESCRIPCCION)
VALUES ('FINALIZADO', 'EL ESTUDIO HA FINALIZADO');
INSERT INTO ESTADO_DE_SOLICITUD (NOMBRE, DESCRIPCCION)
VALUES ('PENDIENTE', 'EL ESTUDIO NO HA COMENZADO');

INSERT INTO MEDICO (MATRICULA, NOMBRE, APELLIDO)
VALUES ('sDSAoj907SSDs', 'ARIEL', 'GALAVERNA');
INSERT INTO MEDICO (MATRICULA, NOMBRE, APELLIDO)
VALUES ('sDSAoDSA7SSDs', 'PAOLA', 'MONTEVERDE');
INSERT INTO MEDICO (MATRICULA, NOMBRE, APELLIDO)
VALUES ('sKLÑDSA07SSDs', 'ALVARO', 'GALAVERNA');

INSERT INTO TIPO_DE_DOCUMENTO (NOMBRE, DESCRIPCION)
VALUES ('DNI', ':)');
INSERT INTO TIPO_DE_DOCUMENTO (NOMBRE, DESCRIPCION)
VALUES ('PASAPORTE', ':|');
INSERT INTO TIPO_DE_DOCUMENTO (NOMBRE, DESCRIPCION)
VALUES ('CUIT', ':(');

INSERT INTO ESTUDIO (NOMBRE, DESCRIPCCION, LIMITE_INFERIOR, LIMITE_SUPERIOR, ID_METODO, ID_UNIDAD_DE_MEDIDA)
VALUES ('COLESTEROL L.D.L', 'A', 1, 2, 1, 3);
INSERT INTO ESTUDIO (NOMBRE, DESCRIPCCION, LIMITE_INFERIOR, LIMITE_SUPERIOR, ID_METODO, ID_UNIDAD_DE_MEDIDA)
VALUES ('COLESTEROL H.D.L', 'B', 1, 2, 1, 3);
INSERT INTO ESTUDIO (NOMBRE, DESCRIPCCION, LIMITE_INFERIOR, LIMITE_SUPERIOR, ID_METODO, ID_UNIDAD_DE_MEDIDA)
VALUES ('MAGNEISIO', 'C', 1, 2, 2, 1);

INSERT INTO RESULTADO (VALOR_HALLADO, FECHA, ID_ESTUDIO, OBSERVACION)
VALUES (0.5, '2001/01/01', 1, 'ESTAS DE RUTA');
INSERT INTO RESULTADO (VALOR_HALLADO, FECHA, ID_ESTUDIO, OBSERVACION)
VALUES (8, '2002/02/02', 2, 'TAMOS CIELO');
INSERT INTO RESULTADO (VALOR_HALLADO, FECHA, ID_ESTUDIO, OBSERVACION)
VALUES (5, '2003/03/03', 3, 'NASHE');

INSERT INTO MUESTRA (DESCRIPCCION, FECHA_HORA_EXTRACCION, ID_RESULTADO)
VALUES ('EXTRACCION DE SANGRE', '2001/01/01 10:10:10', 1);
INSERT INTO MUESTRA (DESCRIPCCION, FECHA_HORA_EXTRACCION, ID_RESULTADO)
VALUES ('EXTRACCION DE SANGRE', '2001/01/01 11:11:11', 2);
INSERT INTO MUESTRA (DESCRIPCCION, FECHA_HORA_EXTRACCION, ID_RESULTADO)
VALUES ('EXTRACCION DE SANGRE', '2011/11/11 12:12:12', 3);

INSERT INTO PACIENTE (N_DOCUMENTO, NOMBRE, APELLIDO, ID_SEXO, ID_DOMICILIO, ID_TELEFONO, ID_TIPO_DE_DOCUMENTO, EMAIL)
VALUES (45934473, 'MATEO', 'MARCHISONE', 1, 1, 1, 1, 'MATEO.MARCHISONE@GMAIL.COM');
INSERT INTO PACIENTE (N_DOCUMENTO, NOMBRE, APELLIDO, ID_SEXO, ID_DOMICILIO, ID_TELEFONO, ID_TIPO_DE_DOCUMENTO, EMAIL)
VALUES (49934479, 'BIANCA', 'MARCHISONE', 2, 1, 3, 1, 'BIANCA.MARCHISONE@GMAIL.COM');
INSERT INTO PACIENTE (N_DOCUMENTO, NOMBRE, APELLIDO, ID_SEXO, ID_DOMICILIO, ID_TELEFONO, ID_TIPO_DE_DOCUMENTO, EMAIL)
VALUES (45946465, 'PEDRO', 'MARCHISONE', 1, 3, 2, 3, 'MATEO.MARCHISONE@GMAIL.COM');

INSERT INTO SOLICITUD (RECETA, ID_PACIENTE, ID_EXTRACCIONISTA, ID_ESTADO, ID_MEDICO, FECHA_HORA_INICIO,
                       FECHA_HORA_FINALIZACION, CAP)
VALUES ('CITOLOGICO COMPLETO', 1, 1, 1, 1, '2001/01/01 10:10:10', '2001/01/01 12:10:10', 'PLE89');
INSERT INTO SOLICITUD (RECETA, ID_PACIENTE, ID_EXTRACCIONISTA, ID_ESTADO, ID_MEDICO, FECHA_HORA_INICIO,
                       FECHA_HORA_FINALIZACION, CAP)
VALUES ('CITOLOGICO COMPLETO', 2, 2, 2, 2, '2003/03/03 10:10:10', '2003/03/03 12:10:10', 'TLE89');
INSERT INTO SOLICITUD (RECETA, ID_PACIENTE, ID_EXTRACCIONISTA, ID_ESTADO, ID_MEDICO, FECHA_HORA_INICIO,
                       FECHA_HORA_FINALIZACION, CAP)
VALUES ('CITOLOGICO COMPLETO', 3, 3, 3, 3, '2001/01/01 10:10:10', '2001/01/01 12:10:10', 'MLE89');

