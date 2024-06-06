import re
class Validaciones():
    def __init__(self):
        pass

    def validarLetras(valor):
        patron = re.compile("^[A-Z a-zñÑáéíóú]*$")
        resultado = patron.match(valor.get()) is not None
        return resultado
    
    def validarNum(valor):
        patron = re.compile('^[0-9.]*$')
        resultado = patron.match(valor.get()) is not None
        return resultado