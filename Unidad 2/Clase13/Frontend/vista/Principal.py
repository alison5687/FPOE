import tkinter as tk
from controladores.Validaciones import Validaciones
from controladores.Comunicacion import Comunicacion
from modelos.Hilo import Hilo
from .Guardar import Interfaz
from .Consultar import Consultar
from .Todos import Todos
from .Actualizar import Actualizar

class Principal():

        

    def __init__(self):
        def guardar():
            guardar=Interfaz.mostrar_interfaz(ventana, hilo,validacion,comunicacion)

        def consultar():
            consultar= Consultar.mostrari(ventana,hilo,validacion,comunicacion)
    
        def todos():
            todos= Todos.mostrar(ventana,comunicacion)

        def actualizar():
            actualizar= Actualizar.mostrar_interfaz(ventana,hilo,validacion,comunicacion)
        
        
        
        ventana = tk.Tk()
        ventana.geometry("500x500")
        ventana.title("Menú Principal")

        hilo= Hilo(ventana)
        validacion= Validaciones()
        comunicacion= Comunicacion(ventana)

        boton_guardar=tk.Button(ventana, text="Guardar",bg="DarkOrchid1", command=lambda:guardar())
        boton_guardar.place(relx=0.35, rely=0.2,relheight=0.1, relwidth=0.35)

        boton_consultar=tk.Button(ventana, text="Consultar Hilo",bg="DarkOrchid1", command=lambda:consultar())
        boton_consultar.place(relx=0.35, rely=0.4,relheight=0.1, relwidth=0.35)


        boton_consultar_todos=tk.Button(ventana, text="Consultar todos los hilos",bg="DarkOrchid1", command=lambda:todos())
        boton_consultar_todos.place(relx=0.35, rely=0.6,relheight=0.1, relwidth=0.35)

        boton_actualizar=tk.Button(ventana, text="Actualizar un hilo", bg="DarkOrchid3", command=lambda:actualizar())
        boton_actualizar.place(relx=0.35, rely=0.8, relheight=0.1, relwidth=0.35)




        ventana.mainloop()
