import customtkinter as ctk
from UI import menu as m

#Cargar datos e iniciando Sistema Pos
def main(app):
    print("Iniciando app")#referencia de inicio
    m.principal_interfaz(app)
    print("App Finalizada")#referencia de fin
    
if __name__ == "__main__":
    Spos = ctk.CTk()
    main(Spos)
    