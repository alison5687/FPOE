import tkinter as tk
from tkinter.messagebox import askyesno
def salir():
        if askyesno("Salir de la aplicación",'¿Desea salir de la aplicación?'):
            ventana.destroy()
# Ventana
ventana=tk.Tk()
ventana.geometry("600x300")
ventana.title("Hilos")
ventana.config(bg="orchid2")
# labels
label_titulo=tk.Label(ventana,text="Adapte su Hilo.",bg="DarkOrchid1")
label_titulo.place(relx=0.4,rely=0.05,relheight=0.1,relwidth=0.2)
label_hilo=tk.Label(ventana,text="Hilo:",bg="DarkOrchid1")
label_hilo.place(relx=0.1,rely=0.2,relheight=0.1,relwidth=0.1)
label_elasticidad=tk.Label(ventana,text="Elasticidad:",bg="DarkOrchid1")
label_elasticidad.place(relx=0.1,rely=0.33,relheight=0.1,relwidth=0.1)
label_suavidad=tk.Label(ventana,text="Suavidad:",bg="DarkOrchid1")
label_suavidad.place(relx=0.1,rely=0.45,relheight=0.1,relwidth=0.1)
label_tenacidad=tk.Label(ventana,text="Tenacidad:",bg="DarkOrchid1")
label_tenacidad.place(relx=0.1,rely=0.57,relheight=0.1,relwidth=0.1)
label_ductilidad=tk.Label(ventana,text="Ductilidad:",bg="DarkOrchid1")
label_ductilidad.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.17)
# Entrys
entry_hilo=tk.Entry(ventana,bg="MediumOrchid1")
entry_hilo.place(relx=0.3,rely=0.2,relheight=0.1,relwidth=0.45)
entry_elasticidad=tk.Entry(ventana,bg="MediumOrchid1")
entry_elasticidad.place(relx=0.3,rely=0.33,relheight=0.1,relwidth=0.45)
entry_suavidad=tk.Entry(ventana,bg="MediumOrchid1")
entry_suavidad.place(relx=0.3,rely=0.45,relheight=0.1,relwidth=0.45)
entry_tenacidad=tk.Entry(ventana,bg="MediumOrchid1")
entry_tenacidad.place(relx=0.3,rely=0.57,relheight=0.1,relwidth=0.45)
entry_ductilidad=tk.Entry(ventana,bg="MediumOrchid1")
entry_ductilidad.place(relx=0.3,rely=0.7,relheight=0.1,relwidth=0.45)
# Buttoms
boton_guardar=tk.Button(ventana,text="Guardar",bg="MediumOrchid1",)
boton_guardar.place(relx=0.8,rely=0.25,relheight=0.2,relwidth=0.15)
boton_salir=tk.Button(ventana,text="Salir",bg="MediumOrchid1",command=lambda:salir())
boton_salir.place(relx=0.8,rely=0.55,relheight=0.2,relwidth=0.15)

ventana.mainloop()