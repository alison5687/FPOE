import tkinter as tk
from tkinter.messagebox import askyesno

class Consultar():
    def mostrari(menu,modelo,validacion,comunicacion):
        
        def consultar():
            hilo=comunicacion.consultar(entryID.get())
            if hilo is not None and isinstance(hilo, dict) and 'hilo' in hilo:
                
                entryHilo.config(state="normal")
                entryHilo.delete(0, tk.END)
                entryHilo.insert(0, hilo['hilo'])
                entryHilo.config(state="disabled")
            else:
                labelValidacionID.config(text="No se encontro hilo.")

        def presionar(evento):
            if(entryID).get()=="":
                texto_validar_id="No se permite espacio en blanco"
                boton_consultar_id.config(state="disabled")
            elif validacion.num(entryID):
                texto_validar_id=""
                boton_consultar_id.config(state="normal")
            else:
                texto_validar_id="Solo se permiten números."
            labelValidacionID.config(text=texto_validar_id)
    
        def salir():
            if askyesno("Salir de la aplicacion",'¿Desea salir de la aplicaion?'):
                ventana.destroy()
        
        ventana= tk.Toplevel(menu)
        ventana.geometry("500x500")
        ventana.title("Consultar ID")
        ventana.config(bg="DarkOrchid1")

        modelo= modelo
        validacion= validacion
        comunicacion= comunicacion

        labelTitulo= tk.Label(ventana, text="Consultar Hilo",bg="DarkOrchid1")
        labelTitulo.place(relx=0.4,rely=0.1,relheight=0.1,relwidth=0.2)
        
        labelID= tk.Label(ventana, text="ID",bg="DarkOrchid1")
        labelID.place(relx=0.2,rely=0.35,relheight=0.1,relwidth=0.1)

        labelHilo=tk.Label(ventana, text="Hilo",bg="DarkOrchid1")
        labelHilo.place(relx=0.2,rely=0.55,relheight=0.1,relwidth=0.1)

        labelValidacionID=tk.Label(ventana, text="",bg="DarkOrchid1")
        labelValidacionID.place(relx=0.4,rely=0.45, relheight=0.1, relwidth=0.2)

        entryID= tk.Entry(ventana,bg="DarkOrchid2")
        entryID.bind("<KeyRelease>",presionar)
        entryID.place(relx=0.4,rely=0.35,relheight=0.1,relwidth=0.2)

        entryHilo= tk.Entry(ventana, state="disabled")
        entryHilo.place(relx=0.4, rely=0.55, relheight=0.1, relwidth=0.2)

        boton_consultar_id= tk.Button(ventana, text="Consultar ID", command=lambda:consultar())
        boton_consultar_id.place(relx=0.2, rely=0.8, relheight=0.1, relwidth=0.2)
        boton_consultar_id.config(state="disabled")

        boton_salir= tk.Button(ventana, text="Salir",bg="DarkOrchid2", command=lambda:salir())
        boton_salir.place(relx=0.55, rely=0.8, relheight=0.1, relwidth=0.2)

        ventana.mainloop()