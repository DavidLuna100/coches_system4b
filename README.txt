Sistema de Gestión de Coches (CRUD) - Python + Tkinter + MySQL
Estructura MVC

main.py                      -> Arranque de la aplicación (clase App)
conexionBD.py                -> Conexión a la base de datos bd_coches
bd.sql                       -> Script para crear la base de datos y la tabla
models/coches.py             -> Modelo: clase Coches y consultas SQL
views/vistas.py              -> Vistas: ventanas, menú y formularios (Tkinter)
controllers/controlador.py   -> Controlador: lógica entre vistas y modelo

Requisitos:
- Python 3
- pip install mysql-connector-python
- MySQL en 127.0.0.1 (usuario root, sin contraseña)

Ejecución:
1. Ejecutar bd.sql en MySQL
2. python main.py
