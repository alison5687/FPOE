import re
class Validaciones():
    def __init__(self):
        pass

    def letras(self,valor):
        patron = re.compile("^[A-Za-zñÑáéíóú]*$")
        resultado = patron.match(valor.get()) is not None
        return resultado
    
    def num(self,valor):
        patron = re.compile('^[0-9.]*$')
        resultado = patron.match(valor.get()) is not None
        return resultado