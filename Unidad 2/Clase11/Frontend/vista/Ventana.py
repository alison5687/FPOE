import tkinter as tk
from tkinter.messagebox import askyesno
from modelos.Hilo import Hilo
from controladores.Validaciones import Validaciones

class Interfaz:
    def mostrar_interfaz():
        def salir():
            if askyesno("Salir de la aplicación", '¿Desea salir de la aplicación?'):
                ventana.destroy()

        def guardar(self):
            
            pass

        def evento_presionar_tecla(evento):
            if Validaciones.validarLetras(modelo.hilo):
                texto_validar_hilo = ""
            else:
                texto_validar_hilo = "Sólo se permiten letras en el campo"
            labelValidacionHilo.config(text=texto_validar_hilo, fg="red")

            if Validaciones.validarNum(modelo.elasticidad):
                texto_validar_elasticidad = ""
            else:
                texto_validar_elasticidad = "Sólo se aceptan números en el campo"
            labelValidacionElasticidad.config(text=texto_validar_elasticidad, fg="red")

            if Validaciones.validarNum(modelo.suavidad):
                texto_validar_suavidad = ""
            else:
                texto_validar_suavidad = "Sólo se aceptan números en el campo"
            labelValidacionSuavidad.config(text=texto_validar_suavidad, fg="red")

            if Validaciones.validarNum(modelo.tenacidad):
                texto_validar_tenacidad = ""
            else:
                texto_validar_tenacidad = "Sólo se aceptan números en el campo"
            labelValidacionTenacidad.config(text=texto_validar_tenacidad, fg="red")

            if Validaciones.validarNum(modelo.ductilidad):
                texto_validar_ductilidad = ""
            else:
                texto_validar_ductilidad = "Sólo se aceptan números en el campo"
            labelValidacionDuctilidad.config(text=texto_validar_ductilidad, fg="red")

        # Ventana
        ventana = tk.Tk()
        ventana.geometry("500x400")
        ventana.title("Agregar Hilo")
        ventana.config(bg="lightblue")

        # Variables
        modelo = Hilo(ventana)

        # Labels
        label_titulo = tk.Label(ventana, text="Personalice su Hilo", bg="lightblue", font=("Arial", 16))
        label_titulo.place(relx=0.2, rely=0.05, relwidth=0.6)

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
        entry_hilo = tk.Entry(ventana, bg="lightcyan", textvariable=modelo.hilo, font=("Arial", 12))
        entry_hilo.bind("<KeyRelease>", evento_presionar_tecla)
        entry_hilo.place(relx=0.35, rely=0.15, relwidth=0.3)

        entry_elasticidad = tk.Entry(ventana, bg="lightcyan", textvariable=modelo.elasticidad, font=("Arial", 12))
        entry_elasticidad.bind("<KeyRelease>", evento_presionar_tecla)
        entry_elasticidad.place(relx=0.35, rely=0.25, relwidth=0.3)

        entry_suavidad = tk.Entry(ventana, bg="lightcyan", textvariable=modelo.suavidad, font=("Arial", 12))
        entry_suavidad.bind("<KeyRelease>", evento_presionar_tecla)
        entry_suavidad.place(relx=0.35, rely=0.35, relwidth=0.3)

        entry_tenacidad = tk.Entry(ventana, bg="lightcyan", textvariable=modelo.tenacidad, font=("Arial", 12))
        entry_tenacidad.bind("<KeyRelease>", evento_presionar_tecla)
        entry_tenacidad.place(relx=0.35, rely=0.45, relwidth=0.3)

        entry_ductilidad = tk.Entry(ventana, bg="lightcyan", textvariable=modelo.ductilidad, font=("Arial", 12))
        entry_ductilidad.bind("<KeyRelease>", evento_presionar_tecla)
        entry_ductilidad.place(relx=0.35, rely=0.55, relwidth=0.3)

        # Buttons
        boton_guardar = tk.Button(ventana, text="Guardar", bg="lightgreen", font=("Arial", 12), command=guardar)
        boton_guardar.place(relx=0.3, rely=0.7, relwidth=0.2)

        boton_salir = tk.Button(ventana, text="Salir", bg="salmon", font=("Arial", 12), command=salir)
        boton_salir.place(relx=0.55, rely=0.7, relwidth=0.2)

        ventana.mainloop()

