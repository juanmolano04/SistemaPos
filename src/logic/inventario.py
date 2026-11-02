from database import almacenamiento as alm
from UI import plantillas as p, configuracion_colores as cls
import customtkinter as ctk

def renderizar_contenedor_producto(contenedor, texto_buscado=""):
    """
    Trae los productos filtrados de la BD y los organiza en la matriz grid.
    Se ejecuta automáticamente cada vez que el usuario escribe.
    """
    #LIMPIAR EL CONTENEDOR ANTES DE DIBUJAR
    # Eliminamos los widgets anteriores para que no se encimen los resultados
    for widget in contenedor.winfo_children():
        widget.destroy()
        
    # Reiniciar la configuración de columnas previas para evitar espacios fantasma
    for i in range(cls.COLUMNAS_MAXIMAS):
        contenedor.grid_columnconfigure(i, weight=0)

    # CONSULTA SQL FILTRADA EN TIEMPO REAL
    conexion = alm.inicializar_bd()
    cursor = conexion.cursor()
    
    # Usamos LIKE para buscar coincidencias parciales basadas en el parámetro
    termino = f"%{texto_buscado}%"
    cursor.execute("""
        SELECT id, nombre, precio, stock FROM productos 
        WHERE nombre LIKE ?
    """, (termino,))
    
    registros = cursor.fetchall()
    
    # Si no hay resultados, mostramos un mensaje en la primera celda
    if not registros:
        lbl_vacio = ctk.CTkLabel(contenedor, text="No se encontraron productos", font=("Arial", 14, "italic"))
        lbl_vacio.grid(row=0, column=0, columnspan=cls.COLUMNAS_MAXIMAS, pady=30)
        conexion.close()
        return

    # RENDERIZAR LA MATRIZ DE PRODUCTOS
    for indice, reg in enumerate(registros):
        id_prod, nombre, precio, stock = reg
        
        # Calcular la fila y la columna de la matriz usando divisiones
        fila_matriz = indice // cls.COLUMNAS_MAXIMAS
        columna_matriz = indice % cls.COLUMNAS_MAXIMAS
        
        contenedor.grid_columnconfigure(columna_matriz, weight=1)
            
        # Tu plantilla original (Asegúrate de que use .bind() internamente si es un botón-frame)
        p.plantilla_productos(contenedor, fila_matriz, columna_matriz, nombre, precio, stock)
    
    conexion.close()
    

