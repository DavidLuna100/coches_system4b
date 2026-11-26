from tkinter import Tk
from views.vistas import Vistas
from controllers.controlador import Controlador

class App(Vistas,Controlador):
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Gestión de Coches")
        self.ventana.geometry("600x700")
        self.ventana.resizable(0,0)
        self.main()

if __name__=="__main__":
    ventana=Tk()
    app=App(ventana)
    ventana.mainloop()
