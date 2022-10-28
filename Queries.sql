DROP DATABASE IF EXISTS BIOMEDICA;

CREATE DATABASE BIOMEDICA;

USE BIOMEDICA;

CREATE TABLE SEXO
(
    ID           INT AUTO_INCREMENT PRIMARY KEY,
    DESCRIPCCION CHAR(1)
);

CREATE TABLE TELEFONO
(
    ID     INT AUTO_INCREMENT PRIMARY KEY,
    NUMERO BIGINT
);

CREATE TABLE DOMICILIO
(
    ID     INT AUTO_INCREMENT PRIMARY KEY,
    CALLE  VARCHAR(30),
    ALTURA INT
);