import tkinter as tk
from tkinter.messagebox import askyesno, showerror, showinfo
import requests

class Actualizar():
    def mostrar_interfaz(menu,modelo,validacion,comunicacion):
        def buscar():
            entry_id.config(state="disabled")
            entry_hilo.config(state="normal")
            entry_elasticidad.config(state="normal")
            entry_suavidad.config(state="normal")
            entry_tenacidad.config(state="normal")
            entry_ductilidad.config(state="normal")
            id = entry_id.get()
            datos = comunicacion.buscar(id)
            if datos:
                entry_hilo.delete(0,tk.END)
                entry_hilo.insert(0,datos['hilo'])
                entry_elasticidad.insert(0,datos['elasticidad'])
                entry_suavidad.insert(0,datos['suavidad'])
                entry_tenacidad.insert(0,datos['tenacidad'])
                entry_ductilidad.insert(0,datos['ductilidad'])
                boton_actualizar.config(state="normal")
            else:
                showerror("Error", "Hilo no encontrado.")
        def actualizar():
            id = entry_id.get()
            hilo = entry_hilo.get()
            elasticidad = entry_elasticidad.get()
            suavidad = entry_suavidad.get()
            tenacidad = entry_tenacidad.get()
            ductilidad = entry_ductilidad.get()

            print(f"ID: {id}")
            print(f"Hilo: {hilo}")
            print(f"Elasticidad: {elasticidad}")
            print(f"Suavidad: {suavidad}")
            print(f"Tenacidad: {tenacidad}")
            print(f"Ductilidad: {ductilidad}")

            
            try:
                resultado = comunicacion.actualizar(id, hilo, elasticidad, suavidad, tenacidad, ductilidad)
                if resultado:
                    showinfo("Éxito", "Hilo actualizado exitosamente.")
                else:
                    showerror("Error", "Error al actualizar el hilo.")
            except requests.exceptions.HTTPError as err:
                showerror("Error", f"Error HTTP: {err}")
            except Exception as e:
                showerror("Error", f"Error inesperado: {e}")

        def limpiar():
            entry_id.delete(0, tk.END)
            entry_hilo.delete(0, tk.END)
            entry_elasticidad.delete(0, tk.END)
            entry_suavidad.delete(0, tk.END)
            entry_tenacidad.delete(0, tk.END)
            entry_ductilidad.delete(0, tk.END)
            boton_actualizar.config(state=tk.DISABLED)
            labelValidacionHilo.config(text="No puede estar el campo vacío")
            labelValidacionID.config(text="No puede estar el campo vacío")

        def salir():
                if askyesno("Salir de la aplicación", '¿Desea salir de la aplicación?'):
                    ventana.destroy()
        
        def presionar(evento):
            if validacion.num(entry_id):
                texto_validacion_id=""
                boton_actualizar.config(state="normal")
            else:
                texto_validacion_id = "Sólo se permiten números en el campo"
            labelValidacionID.config(text=texto_validacion_id)
            if validacion.letras(modelo.hilo):
                texto_validar_hilo = ""
            else:
                texto_validar_hilo = "Sólo se permiten letras en el campo"
            labelValidacionHilo.config(text=texto_validar_hilo, fg="red")

            if validacion.num(modelo.elasticidad):
                texto_validar_elasticidad = ""
            else:
                texto_validar_elasticidad = "Sólo se aceptan números en el campo"
            labelValidacionElasticidad.config(text=texto_validar_elasticidad, fg="red")

            if validacion.num(modelo.suavidad):
                texto_validar_suavidad = ""
            else:
                texto_validar_suavidad = "Sólo se aceptan números en el campo"
            labelValidacionSuavidad.config(text=texto_validar_suavidad, fg="red")

            if validacion.num(modelo.tenacidad):
                texto_validar_tenacidad = ""
            else:
                texto_validar_tenacidad = "Sólo se aceptan números en el campo"
            labelValidacionTenacidad.config(text=texto_validar_tenacidad, fg="red")

            if validacion.num(modelo.ductilidad):
                texto_validar_ductilidad = ""
            else:
                texto_validar_ductilidad = "Sólo se aceptan números en el campo"
            labelValidacionDuctilidad.config(text=texto_validar_ductilidad, fg="red")

        modelo = modelo
        validacion = validacion
        comunicacion = comunicacion
        ventana = tk.Toplevel(menu)
        ventana.geometry("500x400")
        ventana.title("Agregar Hilo")
        ventana.config(bg="lightblue")
        
        # Labels

        label_id = tk.Label(ventana,text="ID;",bg="DarkOrchid1",font=("Arial",12))
        label_id.place(relx=0.1,rely=0.05)

        label_hilo = tk.Label(ventana, text="Hilo:", bg="lightblue", font=("Arial", 12))
        label_hilo.place(relx=0.1, rely=0.15)

        label_elasticidad = tk.Label(ventana, text="Elasticidad:", bg="lightblue", font=("Arial", 12))
        label_elasticidad.place(relx=0.1, rely=0.25)

        label_suavidad = tk.Label(ventana, text="Suavidad:", bg="lightblue", font=("Arial", 12))
        label_suavidad.place(relx=0.1, rely=0.35)

        label_tenacidad = tk.Label(ventana, text="Tenacidad:", bg="lightblue", font=("Arial", 12))
        label_tenacidad.place(relx=0.1, rely=0.45)

        label_ductilidad = tk.Label(ventana, text="Ductilidad:", bg="lightblue", font=("Arial", 12))
        label_ductilidad.place(relx=0.1, rely=0.55)

        labelValidacionID= tk.Label(ventana, text="", bg="DarkOrchid1",fg="red")
        labelValidacionID.place(relx=0.7, rely=0.05, relheight=0.05, relwidth=0.25)

        labelValidacionHilo = tk.Label(ventana, text="", bg="lightblue",font=("Arial",12))
        labelValidacionHilo.place(relx=0.7, rely=0.15,relheight=0.05,relwidth=0.25)

        labelValidacionElasticidad = tk.Label(ventana, text="", bg="lightblue",font=("Arial",12))
        labelValidacionElasticidad.place(relx=0.7, rely=0.25,relheight=0.05,relwidth=0.25)

        labelValidacionSuavidad = tk.Label(ventana, text="", bg="lightblue",font=("Arial",12))
        labelValidacionSuavidad.place(relx=0.7, rely=0.35,relheight=0.05,relwidth=0.25)

        labelValidacionTenacidad = tk.Label(ventana, text="", bg="lightblue",font=("Arial",12))
        labelValidacionTenacidad.place(relx=0.7, rely=0.45,relheight=0.05,relwidth=0.25)

        labelValidacionDuctilidad = tk.Label(ventana, text="", bg="lightblue",font=("Arial",12))
        labelValidacionDuctilidad.place(relx=0.7, rely=0.55)

        # Entrys
        entry_id = tk.Entry(ventana,bg="DarkOrchid3",font=("Arial",12))
        entry_id.bind("<KeyRelease>", presionar)
        entry_id.bind("<Return>", lambda event: entry_hilo.focus())
        entry_id.place(relx=0.35,rely=0.05,relwidth=0.3)

        entry_hilo = tk.Entry(ventana, bg="DarkOrchid3", textvariable=modelo.hilo, font=("Arial", 12))
        entry_hilo.bind("<KeyRelease>", presionar)
        entry_hilo.bind("<Return>", lambda event: entry_elasticidad.focus())
        entry_hilo.place(relx=0.35, rely=0.15, relwidth=0.3)
        entry_hilo.config(state="disabled")

        entry_elasticidad = tk.Entry(ventana, bg="DarkOrchid3", textvariable=modelo.elasticidad, font=("Arial", 12))
        entry_elasticidad.bind("<KeyRelease>", presionar)
        entry_elasticidad.bind("<Return>", lambda event: entry_suavidad.focus())
        entry_elasticidad.place(relx=0.35, rely=0.25, relwidth=0.3)
        entry_elasticidad.config(state="disabled")

        entry_suavidad = tk.Entry(ventana, bg="DarkOrchid3", textvariable=modelo.suavidad, font=("Arial", 12))
        entry_suavidad.bind("<KeyRelease>", presionar)
        entry_suavidad.bind("<Return>", lambda event: entry_tenacidad.focus())
        entry_suavidad.place(relx=0.35, rely=0.35, relwidth=0.3)
        entry_suavidad.config(state="disabled")

        entry_tenacidad = tk.Entry(ventana, bg="DarkOrchid3", textvariable=modelo.tenacidad, font=("Arial", 12))
        entry_tenacidad.bind("<KeyRelease>", presionar)
        entry_tenacidad.bind("<Return>", lambda event: entry_ductilidad.focus())
        entry_tenacidad.place(relx=0.35, rely=0.45, relwidth=0.3)
        entry_tenacidad.config(state="disabled")

        entry_ductilidad = tk.Entry(ventana, bg="DarkOrchid3", textvariable=modelo.ductilidad, font=("Arial", 12))
        entry_ductilidad.bind("<KeyRelease>", presionar)
        entry_ductilidad.place(relx=0.35, rely=0.55, relwidth=0.3)
        entry_ductilidad.config(state="disabled")

        # Buttons
        boton_buscar = tk.Button(ventana, text="Buscar", bg="DarkOrchid2",font=("Arial",12), command=buscar)
        boton_buscar.place(relx=0.05, rely=0.7, relwidth=0.15)

        boton_actualizar = tk.Button(ventana, text="Actualizar", bg="DarkOrchid2", command=actualizar)
        boton_actualizar.config(state=tk.DISABLED)
        boton_actualizar.place(relx=0.3, rely=0.7, relwidth=0.15)

        boton_limpiar = tk.Button(ventana, text="Limpiar", bg="lemon chiffon",font=("Arial",12), command=limpiar)
        boton_limpiar.place(relx=0.55, rely=0.7, relwidth=0.15)

        boton_salir = tk.Button(ventana, text="Salir", bg="salmon", font=("Arial", 12), command=salir)
        boton_salir.place(relx=0.8, rely=0.7, relwidth=0.15)

        ventana.mainloop()
