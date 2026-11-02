import sqlite3

# 1. Configuración de la Base de Datos de prueba
def inicializar_bd():
    conexion = sqlite3.connect(":memory:")  # Usa 'tu_base_datos.db' para persistir datos
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    """)
    datos = [
        ("Laptop ASUS", 899.99, 10),
        ("Mouse Logitech", 25.50, 50),
        ("Teclado Mecánico", 75.00, 22),
        ("Monitor 4K", 349.99, 8),
        ("desourante",349.99,8)
    ]
    cursor.executemany("INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)", datos)
    conexion.commit()
    return conexion