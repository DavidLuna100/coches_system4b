from models import coches
from tkinter import messagebox


class Controlador:
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
