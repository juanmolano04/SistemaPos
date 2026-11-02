import customtkinter as ctk
from UI import configuracion_colores as cls


def buscar_filtrar(contenedor_padre):
        contenedor_filtros = ctk.CTkFrame(contenedor_padre,fg_color=cls.BG_PRINCIPAL, height=40)
        contenedor_filtros.pack(side="top", fill="both", padx=10 ,pady= 10)
        contenedor_filtros.grid_rowconfigure(0,weight=1)
        contenedor_filtros.grid_columnconfigure(0,weight=3)
        contenedor_filtros.grid_columnconfigure(1,weight=3)
        contenedor_filtros.grid_columnconfigure(2,weight=0,minsize=5)
        
        #Entrada del buscador
        entrada_buscador = ctk.CTkEntry(contenedor_filtros,placeholder_text="Buscar",fg_color=cls.BG_INPUTS,text_color=cls.TEXTO_SECUNDARIO,corner_radius=20)
        entrada_buscador.grid(row=0,column=0,sticky="nsew",pady=5,padx=5)
        
        #Selector de categoria (Filtro)
        selector_categorias = ctk.CTkOptionMenu(contenedor_filtros,fg_color=cls.BG_INPUTS,text_color=cls.TEXTO_SECUNDARIO,corner_radius=20,values=["Categoria"],button_color=cls.BG_INPUTS)
        selector_categorias.grid(row=0,column=1,sticky="nsew",pady=5,padx=5)
    
        #Boton para filtros    
        boton_filtros = ctk.CTkButton(contenedor_filtros,width=10,fg_color=cls.BG_INPUTS,text_color=cls.TEXTO_SECUNDARIO,corner_radius=20,text="F")
        boton_filtros.grid(row=0,column=2,pady=5,padx=5)


def plantilla_productos(contenedor,fila,columna,nombre,precio,stock):
        contenedor_producto = ctk.CTkFrame(contenedor,fg_color=cls.BG_PANEL)
        contenedor_producto.grid(row=fila,column=columna,pady=5,padx=5)
        
        
        contenedor_imgproducto = ctk.CTkFrame(contenedor_producto,fg_color="blue")
        contenedor_imgproducto.pack()
        
        texto_nombrep = ctk.CTkLabel(contenedor_producto,text=nombre)
        texto_nombrep.pack()
        
        texto_stock = ctk.CTkLabel(contenedor_producto,text=stock)
        texto_stock.pack()
        
        texto_precio = ctk.CTkLabel(contenedor_producto,text=precio)
        texto_precio.pack()
        
        