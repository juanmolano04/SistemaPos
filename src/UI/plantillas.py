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
        boton_filtros = ctk.CTkButton(contenedor_filtros,height=5,width=5,fg_color=cls.BG_INPUTS,text_color=cls.TEXTO_SECUNDARIO,corner_radius=20)
        boton_filtros.grid(row=0,column=2,sticky="nsew",pady=5,padx=5)


