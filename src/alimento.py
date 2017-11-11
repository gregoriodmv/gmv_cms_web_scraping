"""
Clase que representa la informacion de un alimento
Esta formado por un nombre y un diccionario que relaciona cada componente con su unidad y su valor
de la siguiente forma { nombre : { "unidad": 'valor', "valor" : 'valor'}
"""
# TODO La unidad es siempre la misma para cada componente, lo que varia entre un alimento y otro es el valor de
# ese atributo

class Alimento(object):

    def __init__(self, nombre="", componentes=list()):
        self.nombre = nombre
        self.componentes = componentes

    def get_atributos(self):
        return [atributo["nombre"] for atributo in self.componentes]

    def get_valores(self):
        return [atributo["valor"] for atributo in self.componentes]

    def get_valor(self, nombre_atributo):
        for atributo in self.componentes:
            if atributo["nombre"] == nombre_atributo:
                return atributo["valor"]
