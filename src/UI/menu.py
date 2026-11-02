import customtkinter as ctk
from UI import plantillas as p, configuracion_colores as cls
from logic import inventario as inv

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
    buscador = p.buscar_filtrar(contenedor_categorias)
    
    
    #eventos del buscador
    def al_escribir(event):
        """Espera a que el usuario deje de escribir por 200ms antes de recargar la interfaz."""
        if cls.timer_id is not None:
            app.after_cancel(cls.timer_id)
        
        cls.timer_id = app.after(200, ejecutar_filtro_matriz)
    
    def ejecutar_filtro_matriz():
        """Captura el texto actual de la barra y actualiza el contenedor grid."""
        texto = buscador.get()
        # Pasamos el contenedor global donde se pintan tus productos
        inv.renderizar_contenedor_producto(contenedor_productos, texto)
    
    buscador.bind("<KeyRelease>", al_escribir)
    
    
    
    #contenedor productos 
    contenedor_productos = ctk.CTkScrollableFrame(contenedor_categorias,fg_color=cls.BG_PRINCIPAL,scrollbar_button_color=cls.BG_INPUTS, scrollbar_button_hover_color=cls.BG_PANEL,orientation="vertical")       # Color de la barra que se mueve
    contenedor_productos.pack(side="top",fill="both",expand =True, padx=10 ,pady= 10)
    
    inv.renderizar_contenedor_producto(contenedor_productos)
    
    
    
    
    
    
    
    