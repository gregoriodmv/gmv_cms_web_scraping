"""
Clase Alimento

Clase que representa un alimento. Cada alimento se modela con un nombre y un conjunto de componentes que representan sus
caracteristicas nutricionales. De esta forma, la clase tiene los siguientes 2 atributos:
* nombre: Especifica el nombre del alimento. Por ejemplo, "Aceite de oliva"

* componentes: Una lista donde cada elemento es un diccionario con la informacion de cada componente del alimento con el
siguiente formato:
{ "nombre" : 'nombre_componente' , "unidad": 'valor_unidad', "valor" : 'valor'}

Por ejemplo:
{nombre : "carbohidratos", unidad : "g", valor: 50 }
"""

class Alimento(object):

    def __init__(self, nombre="", componentes=list()):
        self.nombre = nombre
        self.componentes = componentes

    def get_atributos(self):
        """
        Rutina que devuelve una lista con los nombres de los componentes
        :return:    Lista con los valores de sus componentes
        """
        return [atributo["nombre"] for atributo in self.componentes]

    def get_valores(self):
        """
        Rutina que devuelve una lista con los valores de los componentes
        :return:    Lista con los valores de sus componentes
        """
        return [atributo["valor"] for atributo in self.componentes]

    def get_valor(self, nombre_atributo):
        for atributo in self.componentes:
            if atributo["nombre"] == nombre_atributo:
                return atributo["valor"]
