import tkinter as tk
class Hilo():
    
    def __init__(self,ventanaPrincipal):
        self.ventanaPrincipal=ventanaPrincipal
        self.hilo=tk.StringVar(ventanaPrincipal)
        self.elasticidad=tk.StringVar(ventanaPrincipal)
        self.suavidad=tk.StringVar(ventanaPrincipal)
        self.tenacidad=tk.StringVar(ventanaPrincipal)
        self.ductilidad=tk.StringVar(ventanaPrincipal)