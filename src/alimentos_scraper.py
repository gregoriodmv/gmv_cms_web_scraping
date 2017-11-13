# -*- coding: latin-1 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from alimento import *
import time
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import lxml.html


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


"""
Clase AlimentosScraper

Clase que contiene la informacion y las rutinas necesarias para realizar el proceso de parseo de la web de alimentos.

Formada por los siguientes atributos:
* url: Contiene la url base a partir de la cual se iniciar el proceso de web scraping
* alimentos: Lista con objetos Alimento donde se van guardando los alimentos parseados
* inicio_parseo: Indica el numero de fila desde la que se inicia el proceso de parseo. Permite reanudar el proceso de
parseo en el ultimo elemento en caso de que el proceso se interrumpa.
"""

class AlimentosScraper(object):

    ELEMENTO_INICIAL = 2        # Constante que indica el primer alimento de la tabla
    ELEMENTO_FINAL = 950        # Constante que indica el ultimo alimento de la tabla

    def __init__(self, alimentos = list()):
        self.url = 'http://www.bedca.net/bdpub/index.php'
        self.alimentos = alimentos
        self.inicio_parseo = self.ELEMENTO_INICIAL

    def start_browser(self):
        self.browser = webdriver.Firefox()

    def close_browser(self):
        self.browser.quit()

    def ir_a_url(self, url):
        self.browser.get(url)

    def parsea_info_alimento(self):
        """
        Rutina que obtiene los componentes de un alimento y sus valores desde la pagina que describe el alimento.

        La informacion del alimento esta dispuesta en forma de tabla. Cada fila de la tabla representa un componente
        del alimento y las columnas de la fila contienen el nombre, unidad y valor de ese componente para el alimento.

        Se recorren las filas de la tabla. Para cada fila se obtienen sus columnas. Solo nos vamos a fijar en las
        columnas que contiene informacion de nutrientes, por lo que el resto se saltan. Si la fila representa un
        componente, se obtiene su nombre, su unidad y su valor, y se crea un diccionario de la forma

        { "nombre" : 'nombre_componente' , "unidad": 'valor_unidad', "valor" : 'valor'}

        que representa al componente.

        :return:       Lista con los diccionarios que representan los componentes del alimento
        """
        lista_componentes = []

        try:

            root = lxml.html.fromstring(self.browser.page_source)
            for row in root.xpath("//table[3]//tr"):
                cells = row.xpath(".//td")
                if cells:
                    # Filtramos aquellas filas que no tiene informacion de un nutriente.
                    if cells[0].text_content() not in ["Proximales", "Hidratos de Carbono", "Grasas", "Vitaminas", "Minerales"]:
                        lista_componentes.append({"nombre": cells[0].text_content(),
                                                      "unidad": cells[2].text_content(),
                                                      "valor": cells[1].text_content()})

        except Exception as ex:
            print "Error: " + str(ex)

        return lista_componentes

    def to_csv(self, nombre_fichero="alimentos.csv"):
        """
        Rutina que vuelca la informacion parseada de la pagina en un archivo .csv para crear el dataset.

        Se abre el fichero con permisos de escritura. La primera fila del fichero sera la cabecera, que indica el
        nombre de los atributos del dataset. Estara formada por el nombre del alimento seguido del nombre de cada
        componente del alimento.

        A continuacion se itera sobre los alimentos obtenidos durante el proceso de parseo. Para cada alimento se
        obtiene su nombre y la lista con los valores asociados a cada uno de sus componentes. Se concatenan en una
        sola lista y se escribe en el fichero .csv a modo de iobservacion.

        :param nombre_fichero: Nombre del fichero .csv de salida con el dataset. Por defecto es 'alimentos.csv'
        :return:
        """

        try:
            alimento_muestra = self.alimentos[0]

            # Se crea un documento .csv para escribir y se obtiene un objeto para escribir en el fichero
            csvfile = open(nombre_fichero, "wb")
            print "Abriendo fichero {0}...".format(nombre_fichero)
            csvwriter = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_ALL)

            # Se crea la cabecera del dataset. Esta formada por el nombre del alimento y sus componentes
            nombre_atributos = ["Nombre"]               # El primer atributo sera el nombre del alimento
            for atributo in alimento_muestra.componentes:
                cadena = atributo["nombre"] + " (" + atributo["unidad"] + ")"
                nombre_atributos.append(cadena)

            # Se escribe la cabecera
            csvwriter.writerow([unicode(celda).encode("utf-8") for celda in nombre_atributos])

            # Para cada alimento de los parseados, se forma una lista con su nombre y los valores de sus componententes y
            # se escribe en el fichero .csv
            for indice, alimento in enumerate(self.alimentos):
                registro = [alimento.nombre]
                registro.extend(alimento.get_valores())
                csvwriter.writerow([unicode(celda).encode("utf-8") for celda in registro])
        except UnicodeEncodeError as ex:
            print ex
        except IndexError as ex:
            print "Error en la creacion del dataset. No hay ningun alimento registrado"

        # Se cierra el fichero al finalizar el proceso
        if csvfile:
            print "Cerrando fichero {0}...".format(nombre_fichero)
            csvfile.close()


    def parseo(self, show_time = False):
        """
        Rutina que realiza todo el proceso de parseo:
        1. Crea una instancia del navegador
        2. Accede a la url base a partir de la cual se inicia el proceso de parseo
        3. Navega por los botones hasta llegar a la pagina que contiene una lista con los alimentos a obtener
        4. Accede a cada alimento, parsea su informacion y lo guarda en un objeto de tipo Alimento
        5. Una vez terminado el proceso se cierra la instancia del navegador

        :param show_time    Indica si se mide el tiempo de parseo de cada elemento y tiempo de parseo total.
                            Por defecto es False

        :return:        True si el proceso ha terminado bien
                        False en caso de que hubiera algun problema durante el proceso de parseo
        """

        # Si el parametro show_time es True, se arranca un timer para medir el tiempo de la tarea de parseo
        if show_time:
            inicio_proceso = time.time()

        # 1. Se inicia el navegador
        self.start_browser()

        # 2. y se accede a la url a prasear
        self.ir_a_url(self.url)

        # 3. Navegacion por los botones
        # 3.1. Se obtiene el boton "Consulta" ...
        button = self.browser.find_element_by_css_selector('div.link:nth-child(4) > a:nth-child(1)')
        if not button:
            print "El boton 'Consulta' no existe. Se cancela el proceso"
            return False

        # ... y se hace click sobre el
        button.click()

        # 3.2. Se obtiene el boton "Lista alfabetica"
        button = self.browser.find_element_by_css_selector('#Alfabetica')
        if not button:
            print "El boton 'Lista alfabetica' no existe. Se cancela el proceso"
            return False

        # ... y se hace click sobre el
        button.click()

        # 3.3. Se obtiene el boton "Todos"
        button = self.browser.find_element_by_css_selector('#alphabet > p:nth-child(1) > a:nth-child(1)')
        if not button:
            print "Error al obtener el boton Todos"
            return False

        # ... y se hace click sobre el
        button.click()

        time.sleep(1)

        # 4. Se accede al primer elemento de la lista pinchando en el nombre del alimento.
        # Se parsea la informacion de la pagina y se encapsula en un objeto Alimento. Finalmente se pincha en
        # "Listado anterior" para volver a la lista y repetir el proceso con el siguiente elemento hasta llegar al
        # final de la lista.
        for fila in range(self.inicio_parseo, self.ELEMENTO_FINAL + 1):
            try:
                # En cada iteracion se guarda el incice del elemento que se esta parseando, para que en caso de fallo
                # se pueda repetir el proceso desde el elemento que fallo
                self.inicio_parseo = fila

                # 4.1 Se obtiene el link a la pagina de informacion del elemento y se accede ella
                # elemento = self.browser.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div[2]/table/tbody/tr[{0}]/td[2]/a".format(fila))

                elemento = WebDriverWait(self.browser, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/div[2]/table/tbody/tr[{0}]/td[2]/a".format(fila))))

                nombre = elemento.text
                print "Obteniendo informacion de: " + nombre
                elemento.click()            # Se accede al elemento
                time.sleep(0.1)

                # Se inicia el tiempo de parseo del alimento
                # if show_time:
                #     inicio_alimento = time.time()

                # 4.2 Se obtiene una lista con los componentes de dicho alimento
                componentes = self.parsea_info_alimento()

                # if show_time:
                #     final_alimento = time.time()
                #     print "Tiempo de parseo de " + nombre + ": %d segundos" % (final_alimento - inicio_alimento)

                # 4.3. Se encapsula la informacion obtenida en un objeto de tipo Alimentos
                self.alimentos.append(Alimento(nombre, componentes))

                # 4.4. Se pincha en el boton "Lista anterior" para poder repetir el proceso con los siguientes alimentos
                volver = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='Todos']")))

                # volver = self.browser.find_element_by_xpath("//*[@id='Todos']")
                volver.click()

                time.sleep(0.1)

            except NoSuchElementException as ex:
                print "Elemento %d no encontrado" % fila
                print ex

        # Se obtiene la marca de tiempo tras el parseo y se calcula la diferencia respecto al inicio
        if show_time:
            final_proceso = time.time()
            print "Tiempo total de parseo: %d segundos" % (final_proceso - inicio_proceso)


        # 5. Se cierra la instancia al navegador
        self.close_browser()
        return True