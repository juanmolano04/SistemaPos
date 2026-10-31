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
    Spos.geometry("500x500") #tamaño de la ventana principal
    inicio(Spos) #llamando a Inicio
    Spos.mainloop() #mainloop
    

# diseño de interfaz de inicio
def inicio(app):
    #contenedor de inicio
    contenedor_principal = ctk.CTkFrame(app,fg_color="gray")
    contenedor_principal.grid(row = 0, column = 0)
    