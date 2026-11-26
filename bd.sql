-- Base de datos del sistema de Coches (ejecutar en MySQL / phpMyAdmin)
CREATE DATABASE IF NOT EXISTS bd_coches;
USE bd_coches;

CREATE TABLE IF NOT EXISTS coches (
    id INT AUTO_INCREMENT PRIMARY KEY,
    marca VARCHAR(50) NOT NULL,
    color VARCHAR(50) NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    velocidad INT NOT NULL,
    potencia INT NOT NULL,
    asientos INT NOT NULL
);
