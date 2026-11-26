from coches import coches
from tkinter import Tk,Label,Entry,Button,messagebox,StringVar,Menu,LabelFrame,ttk


class App:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Gestión de Coches")
        self.ventana.geometry("600x700")
        self.ventana.resizable(0,0)
        self.main()

    # .... Vistas o Views del Sistema ....
    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def barraMenu(self):
        #Menu de Opciones
        menuBar=Menu(self.ventana)
        self.ventana.config(menu=menuBar)

        menuPrincipal=Menu(menuBar,tearoff=False)
        menuBar.add_cascade(label="Principal",menu=menuPrincipal)
        menuPrincipal.add_command(label="Menu Principal",command=self.main)
        menuPrincipal.add_command(label="Menu Acciones",command=self.menu_acciones)
        menuPrincipal.add_separator()
        menuPrincipal.add_command(label="Salir",command=self.ventana.quit)

        accionesMenu=Menu(menuBar,tearoff=False)
        menuBar.add_cascade(label="Acciones",menu=accionesMenu)
        accionesMenu.add_command(label="Agregar",command=self.insertar_coche_view)
        accionesMenu.add_command(label="Borrar",command=self.eliminar_coche_view)
        accionesMenu.add_command(label="Modificar",command=self.modificar_coche_view)
        accionesMenu.add_command(label="Mostrar",command=self.consultar_coche_view)
        accionesMenu.add_separator()
        accionesMenu.add_command(label="Regresar",command=self.main)

    def main(self):
        self.borrarPantalla()
        self.barraMenu()
        Label(self.ventana,text="::: MENU PRINCIPAL :::").pack(pady=20)
        Button(self.ventana,text="1.- Coches",command=self.menu_acciones).pack(pady=10)
        Button(self.ventana,text="2.- Salir",command=self.ventana.quit).pack(pady=10)

    def menu_acciones(self):
        self.borrarPantalla()
        self.barraMenu()
        tipo="Coche"
        Label(self.ventana,text=f"...::: Menu de {tipo} :::...").pack(pady=10)
        Button(self.ventana,text="1.- Agregar",command=self.insertar_coche_view).pack(pady=10)
        Button(self.ventana,text="2.- Borrar",command=self.eliminar_coche_view).pack(pady=10)
        Button(self.ventana,text="3.- Modificar",command=self.modificar_coche_view).pack(pady=10)
        Button(self.ventana,text="4.- Mostrar",command=self.consultar_coche_view).pack(pady=10)
        Button(self.ventana,text="5.- Regresar",command=self.main).pack(pady=10)

    def insertar_coche_view(self):
        self.borrarPantalla()
        self.barraMenu()
        Label(self.ventana,text="...Ingresar los datos del Coche").pack(pady=10)

        self.frame1=LabelFrame(self.ventana,text="Datos del coche")
        self.frame1.pack(pady=10,padx=20)

        Label(self.frame1,text="Marca: ").grid(row=0,column=0,pady=5,padx=10)
        self.marca=Entry(self.frame1)
        self.marca.focus()
        self.marca.grid(row=0,column=1,pady=5,padx=10)

        Label(self.frame1,text="Color: ").grid(row=1,column=0,pady=5,padx=10)
        self.color=Entry(self.frame1)
        self.color.grid(row=1,column=1,pady=5,padx=10)

        Label(self.frame1,text="Modelo: ").grid(row=2,column=0,pady=5,padx=10)
        self.modelo=Entry(self.frame1)
        self.modelo.grid(row=2,column=1,pady=5,padx=10)

        Label(self.frame1,text="Velocidad: ").grid(row=3,column=0,pady=5,padx=10)
        self.velocidad=Entry(self.frame1)
        self.velocidad.grid(row=3,column=1,pady=5,padx=10)

        Label(self.frame1,text="Potencia: ").grid(row=4,column=0,pady=5,padx=10)
        self.potencia=Entry(self.frame1)
        self.potencia.grid(row=4,column=1,pady=5,padx=10)

        Label(self.frame1,text="# de Asientos: ").grid(row=5,column=0,pady=5,padx=10)
        self.asientos=Entry(self.frame1)
        self.asientos.grid(row=5,column=1,pady=5,padx=10)

        Button(self.ventana,text=":: Agregar ::",command=self.insertar_coche_controller).pack(pady=5)
        Button(self.ventana,text=":: Regresar ::",command=self.menu_acciones).pack(pady=5)

    def eliminar_coche_view(self):
        self.borrarPantalla()
        self.barraMenu()
        Label(self.ventana,text="...Ingresar el ID del coche a eliminar").pack(pady=10)

        self.frame1=LabelFrame(self.ventana,text="Eliminar coche")
        self.frame1.pack(pady=10,padx=20)

        Label(self.frame1,text="ID: ").grid(row=0,column=0,pady=5,padx=10)
        self.id=Entry(self.frame1)
        self.id.focus()
        self.id.grid(row=0,column=1,pady=5,padx=10)

        self.btn_buscar=Button(self.frame1,text="Buscar",command=lambda:self.buscar_controller("eliminar"))
        self.btn_buscar.grid(row=1,column=0,columnspan=2,pady=5)

        self.btn_eliminar=Button(self.frame1,text=":: Eliminar ::",state="disabled",command=self.eliminar_coche_controller)
        self.btn_eliminar.grid(row=2,column=0,columnspan=2,pady=5)

        Button(self.ventana,text=":: Regresar ::",command=self.menu_acciones).pack(pady=5)

    def consultar_coche_view(self):
        self.borrarPantalla()
        self.barraMenu()
        Label(self.ventana,text="..:: Consultar Coches ::..").pack(pady=10)

        columnas=("ID","Marca","Color","Modelo","Velocidad","Potencia","Asientos")
        self.tabla=ttk.Treeview(self.ventana,columns=columnas,show="headings",height=15)
        for col in columnas:
            self.tabla.heading(col,text=col)
            self.tabla.column(col,width=75,anchor="center")
        self.tabla.pack(pady=10,padx=10)

        self.consultar_coche_controller(self.tabla)

        Button(self.ventana,text=":: Regresar ::",command=self.menu_acciones).pack(pady=5)

    def modificar_coche_view(self):
        self.borrarPantalla()
        self.barraMenu()
        Label(self.ventana,text="...Ingresar el ID del coche a modificar").pack(pady=10)

        self.frame1=LabelFrame(self.ventana,text="Buscar coche")
        self.frame1.pack(pady=10,padx=20)

        Label(self.frame1,text="ID: ").grid(row=0,column=0,pady=5,padx=10)
        self.id=Entry(self.frame1)
        self.id.focus()
        self.id.grid(row=0,column=1,pady=5,padx=10)

        self.btn_buscar=Button(self.frame1,text="Buscar",command=lambda:self.buscar_controller("modificar"))
        self.btn_buscar.grid(row=1,column=0,columnspan=2,pady=5)

        # Variables asociadas a los campos
        self.var_marca=StringVar()
        self.var_color=StringVar()
        self.var_modelo=StringVar()
        self.var_velocidad=StringVar()
        self.var_potencia=StringVar()
        self.var_asientos=StringVar()

        self.frame2=LabelFrame(self.ventana,text="Datos del coche")
        self.frame2.pack(pady=10,padx=20)

        Label(self.frame2,text="Marca: ").grid(row=0,column=0,pady=5,padx=10)
        self.marca=Entry(self.frame2,textvariable=self.var_marca)
        self.marca.grid(row=0,column=1,pady=5,padx=10)

        Label(self.frame2,text="Color: ").grid(row=1,column=0,pady=5,padx=10)
        self.color=Entry(self.frame2,textvariable=self.var_color)
        self.color.grid(row=1,column=1,pady=5,padx=10)

        Label(self.frame2,text="Modelo: ").grid(row=2,column=0,pady=5,padx=10)
        self.modelo=Entry(self.frame2,textvariable=self.var_modelo)
        self.modelo.grid(row=2,column=1,pady=5,padx=10)

        Label(self.frame2,text="Velocidad: ").grid(row=3,column=0,pady=5,padx=10)
        self.velocidad=Entry(self.frame2,textvariable=self.var_velocidad)
        self.velocidad.grid(row=3,column=1,pady=5,padx=10)

        Label(self.frame2,text="Potencia: ").grid(row=4,column=0,pady=5,padx=10)
        self.potencia=Entry(self.frame2,textvariable=self.var_potencia)
        self.potencia.grid(row=4,column=1,pady=5,padx=10)

        Label(self.frame2,text="# de Asientos: ").grid(row=5,column=0,pady=5,padx=10)
        self.asientos=Entry(self.frame2,textvariable=self.var_asientos)
        self.asientos.grid(row=5,column=1,pady=5,padx=10)

        self.btn_modificar=Button(self.ventana,text=":: Modificar ::",state="disabled",command=self.modificar_coche_controller)
        self.btn_modificar.pack(pady=5)

        Button(self.ventana,text=":: Regresar ::",command=self.menu_acciones).pack(pady=5)

    # .... Controlador o Controller del Sistema ....
    def respuesta_sql(self,respuesta):
        if respuesta:
            messagebox.showinfo(title=":: Exitoso ::",message="...¡Accion Realizada con Exito!...")
        else:
            messagebox.showerror(title=":: Verifique por favor ::",message="...¡Esta Accion no pudo realizarse en este momento!...")

    def confirmacion_eliminar(self):
        return messagebox.askyesno(title=":: Confirmar ::",message="¿Deseas eliminar este coche?")

    def cambiar_estado_btn(self,estado,tipo_accion):
        if estado:
            nuevo_estado="normal"
        else:
            nuevo_estado="disabled"
        if tipo_accion=="eliminar":
            self.btn_eliminar.config(state=nuevo_estado)
        elif tipo_accion=="modificar":
            self.btn_modificar.config(state=nuevo_estado)

    def insertar_coche_controller(self):
        coches1=coches.Coches(self.marca.get(),self.color.get(),self.modelo.get(),self.velocidad.get(),self.potencia.get(),self.asientos.get())
        respuesta=coches1.insertar()
        self.respuesta_sql(respuesta)
        del coches1
        if respuesta:
            self.insertar_coche_view()

    def eliminar_coche_controller(self):
        id=self.id.get()
        resp=self.confirmacion_eliminar()
        if resp==True:
            respuesta=coches.Coches.eliminar(id)
            self.respuesta_sql(respuesta)
            if respuesta:
                self.eliminar_coche_view()

    def consultar_coche_controller(self,tabla):
        registros=coches.Coches.consultar()
        if len(registros)>0:
            for fila in registros:
                tabla.insert("","end",values=fila)
        else:
            messagebox.showinfo(title=":: Consulta ::",message="¡No se encontro informacion en la BD!...")

    def modificar_coche_controller(self):
        id=self.id.get()
        coches1=coches.Coches(self.marca.get(),self.color.get(),self.modelo.get(),self.velocidad.get(),self.potencia.get(),self.asientos.get())
        respuesta=coches1.actualizar(id)
        self.respuesta_sql(respuesta)
        del coches1
        if respuesta:
            self.modificar_coche_view()

    def buscar_controller(self,tipo_accion):
        id=self.id.get()
        coche1=coches.Coches.buscar(id)
        if len(coche1)>0:
            messagebox.showinfo(title="...¡ Registro Encontrado !...",message=f"...¡El registro fue encontrado con exito, puedes {tipo_accion}!...")
            self.cambiar_estado_btn(True,tipo_accion)
            if tipo_accion=="modificar":
                self.var_marca.set(coche1[0][1])
                self.var_color.set(coche1[0][2])
                self.var_modelo.set(coche1[0][3])
                self.var_velocidad.set(coche1[0][4])
                self.var_potencia.set(coche1[0][5])
                self.var_asientos.set(coche1[0][6])
        else:
            messagebox.showerror(title="...¡ Verifica por favor !...",message=f"...¡El registro no fue encontrado, no es posible {tipo_accion}!...")
            self.cambiar_estado_btn(False,tipo_accion)


if __name__=="__main__":
    ventana=Tk()
    app=App(ventana)
    ventana.mainloop()