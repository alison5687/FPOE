import tkinter as tk
from tkinter.ttk import Treeview,Scrollbar
class Todos():
    def mostrar(menu,comunicacion):
        ventana= tk.Toplevel(menu)
        ventana.title("Consultar Hilos")
        comunicacion = comunicacion
        labelTitulo= tk.Label(ventana, text="Hilos")
        labelTitulo.pack()
        
        tabla= Treeview(ventana)
        tabla["columns"]=["N°.","Hilo","Elasticidad","Suavidad","Tenacidad","Ductilidad"]
        tabla.heading("#1",text="N°.")
        tabla.heading("#2",text="Hilo")
        tabla.heading("#3",text="Elasticidad")
        tabla.heading("#4",text="Suavidad")
        tabla.heading("#5",text="Tenacidad")
        tabla.heading("#6",text="Ductilidad")

        listaHilos = comunicacion.todos()
        i=1
        for hilo in listaHilos:
            tabla.insert('','end',values=[i,hilo['hilo'],hilo['elasticidad'],hilo['suavidad'],hilo['tenacidad'],hilo['ductilidad']])
            i+=1
        
        tabla["show"]="headings"
        tabla.column("#1",width=30)
        tabla.column("#2",width=100)
        tabla.column("#3",width=200)
        tabla.column("#4",width=150)
        tabla.column("#5",width=150)
        tabla.column("#6",width=150)

        scrollbar=Scrollbar(ventana, orient="vertical",command=tabla.yview)
        tabla.config(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right",fill="y")  
        tabla.pack(fill="both",expand=True)    

        ventana.mainloop() 