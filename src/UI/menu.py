import customtkinter as ctk

#Definiendo colores
BG_PRINCIPAL = "#1F1D2B"      # Fondo oscuro de la zona izquierda
BG_PANEL = "#252836"          # Fondo de las tarjetas de productos y panel derecho del ticket
BG_INPUTS = "#2D303E"         # Cajas de texto, buscador, selectores y casillas vacías

COLOR_COBRAR = "#34C759"      # Verde vibrante para el botón principal de cobrar
COLOR_ELIMINAR = "#FF6B6B"    # Rojo salmón para los iconos de basura o botón cancelar

TEXTO_TITULO = "#FFFFFF"      # Blanco puro para textos principales, precios y botones
TEXTO_SECUNDARIO = "#808191"  # Gris opaco para subtítulos, etiquetas y líneas divisorias



#Menu de inicio 
def principal_interfaz(Spos):
    Spos.title("Sistema Pos") #Titulo de la ventana principal
    Spos.geometry("827x627")#tamaño de la ventana principal
    inicio(Spos) #llamando a Inicio
    Spos.mainloop() #mainloop
    

# diseño de interfaz de inicio
def inicio(app):
    #contenedor de inicio
    contenedor_principal = ctk.CTkFrame(app,fg_color=BG_PRINCIPAL)
    contenedor_principal.pack(fill="both",expand=True)
    #tamaños de grid del contenedor principal
    contenedor_principal.grid_columnconfigure(0, weight=3) #celda grande horizontal
    contenedor_principal.grid_columnconfigure(1, weight=1) #pequeño horizontal
    contenedor_principal.grid_rowconfigure(0, weight=1)  #una sola fila
    
    #contenedor de buscador y productos
    contenedor_categorias = ctk.CTkFrame(contenedor_principal,fg_color=BG_PRINCIPAL)
    contenedor_categorias.grid(row=0,column=0,sticky="nsew", pady=20,padx=10)
    
    #contenedor factura
    contenedor_factura = ctk.CTkFrame(contenedor_principal,fg_color=BG_PANEL,border_color=TEXTO_SECUNDARIO,border_width=2,corner_radius=20)
    contenedor_factura.grid(row=0,column=1,sticky="nsew", pady=20,padx=10)
    
    #contenerdo buscador y filtros
    contenedor_filtros = ctk.CTkFrame(contenedor_categorias,fg_color=BG_PRINCIPAL, height=40)
    contenedor_filtros.pack(side="top", fill="both", padx=10 ,pady= 10)
    contenedor_filtros.grid_rowconfigure(0,weight=1)
    contenedor_filtros.grid_columnconfigure(0,weight=3)
    contenedor_filtros.grid_columnconfigure(1,weight=3)
    contenedor_filtros.grid_columnconfigure(2,weight=0,minsize=5)
    
    #contenedor productos 
    contenedor_productos = ctk.CTkScrollableFrame(contenedor_categorias,fg_color=BG_PRINCIPAL,scrollbar_button_color=BG_INPUTS, scrollbar_button_hover_color=BG_PANEL,orientation="vertical")       # Color de la barra que se mueve
    contenedor_productos.pack(side="top",fill="both",expand =True, padx=10 ,pady= 10)
    
    entrada_buscador = ctk.CTkEntry(contenedor_filtros,placeholder_text="Buscar",fg_color=BG_INPUTS,text_color=TEXTO_SECUNDARIO,corner_radius=20)
    entrada_buscador.grid(row=0,column=0,sticky="nsew",pady=5,padx=5)
    
    selector_categorias = ctk.CTkOptionMenu(contenedor_filtros,fg_color=BG_INPUTS,text_color=TEXTO_SECUNDARIO,corner_radius=20,values=["Categoria"],button_color=BG_INPUTS)
    selector_categorias.grid(row=0,column=1,sticky="nsew",pady=5,padx=5)
    
    boton_filtros = ctk.CTkButton(contenedor_filtros,height=5,width=5,fg_color=BG_INPUTS,text_color=TEXTO_SECUNDARIO,corner_radius=20)
    boton_filtros.grid(row=0,column=2,sticky="nsew",pady=5,padx=5)
    
    
    