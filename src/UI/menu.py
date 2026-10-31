import customtkinter as ctk

#Definiendo colores




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
    