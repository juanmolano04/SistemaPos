import customtkinter as ctk
from UI import plantillas as p, configuracion_colores as cls
from database import almacenamiento as alm

#Menu de inicio 
def principal_interfaz(Spos):
    Spos.title("Sistema Pos") #Titulo de la ventana principal
    Spos.after(0, lambda: Spos.state("zoomed"))
    inicio(Spos) #llamando a Inicio
    Spos.mainloop() #mainloop
    

# diseño de interfaz de inicio
def inicio(app):
    #contenedor de inicio
    contenedor_principal = ctk.CTkFrame(app,fg_color=cls.BG_PRINCIPAL)
    contenedor_principal.pack(fill="both",expand=True)
    #tamaños de grid del contenedor principal
    contenedor_principal.grid_columnconfigure(0, weight=3) #celda grande horizontal
    contenedor_principal.grid_columnconfigure(1, weight=1) #pequeño horizontal
    contenedor_principal.grid_rowconfigure(0, weight=1)  #una sola fila
    
    #contenedor de buscador y productos
    contenedor_categorias = ctk.CTkFrame(contenedor_principal,fg_color=cls.BG_PRINCIPAL)
    contenedor_categorias.grid(row=0,column=0,sticky="nsew", pady=20,padx=10)
    
    #contenedor factura
    contenedor_factura = ctk.CTkFrame(contenedor_principal,fg_color=cls.BG_PANEL,border_color=cls.TEXTO_SECUNDARIO,border_width=2,corner_radius=20)
    contenedor_factura.grid(row=0,column=1,sticky="nsew", pady=20,padx=10)
    
    #se llama a buscar y filtrar para tener el controlador 
    p.buscar_filtrar(contenedor_categorias)
    
    #contenedor productos 
    contenedor_productos = ctk.CTkScrollableFrame(contenedor_categorias,fg_color=cls.BG_PRINCIPAL,scrollbar_button_color=cls.BG_INPUTS, scrollbar_button_hover_color=cls.BG_PANEL,orientation="vertical")       # Color de la barra que se mueve
    contenedor_productos.pack(side="top",fill="both",expand =True, padx=10 ,pady= 10)
    
    conexion = alm.inicializar_bd()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, precio, stock FROM productos")
    registros = cursor.fetchall()
    

    for indice, reg in enumerate(registros):
        id_prod, nombre, precio, stock = reg
        
        # Calcular la fila y la columna de la matriz usando divisiones
        fila_matriz = indice // cls.COLUMNAS_MAXIMAS
        columna_matriz = indice % cls.COLUMNAS_MAXIMAS
        
        contenedor_productos.grid_columnconfigure(columna_matriz,weight=1)
            
        p.plantilla_productos(contenedor_productos, fila_matriz,columna_matriz, nombre, precio, stock)
    
    
    conexion.close()
    
    