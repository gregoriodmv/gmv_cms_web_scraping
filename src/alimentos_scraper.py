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

class AlimentosScraper(object):

    def __init__(self, alimentos = list()):
        self.url = 'http://www.bedca.net/bdpub/index.php'
        self.alimentos = alimentos
        self.inicio_parseo = 2

    # TODO Hacerlo para otros navegadores
    def start_browser(self):
        self.browser = webdriver.Firefox()

    def close_browser(self):
        self.browser.quit()

    def ir_a_url(self, url):
        self.browser.get(url)

    def parsea_info_alimento(self):
        """
        Rutina que parsea la informacion de la pagina de un alimento

        La informacion del alimento esta dispuesta en forma de tabla. Cada componente de la tabla es una fila de la
        tabla. Asi, se recorren las filas y se va extrayendo la informacion de cada componente.

        :return:       Lista con los componentes de un alimento y los valores de cada componentes
        """
        lista_componentes = []

        # for num_fila in range(2, 46):
        #     try:
        #
        #         print "Analizando fila %d" % (num_fila)
        #
        #         # nombre = self.browser.find_element_by_xpath(
        #         #     "/html/body/div[1]/div/div[3]/div[2]/div[2]/table[3]/tbody[{0}]/tr/td[1]/b".format(num_fila))
        #         # valor = self.browser.find_element_by_xpath(
        #         #     "/html/body/div[1]/div/div[3]/div[2]/div[2]/table[3]/tbody[{0}]/tr/td[2]".format(num_fila))
        #         # unidad = self.browser.find_element_by_xpath(
        #         #     "/html/body/div[1]/div/div[3]/div[2]/div[2]/table[3]/tbody[{0}]/tr/td[3]".format(num_fila))
        #
        #         # Introduzco la espera en el nombre esperando que pete en la unidad o en el valor
        #         # nombre = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/div[2]/table[3]/tbody[{0}]/tr/td[1]/b".format(num_fila))))
        #         # valor = self.browser.find_element_by_xpath(
        #         #     "/html/body/div[1]/div/div[3]/div[2]/div[2]/table[3]/tbody[{0}]/tr/td[2]".format(num_fila))
        #         # unidad = self.browser.find_element_by_xpath(
        #         #     "/html/body/div[1]/div/div[3]/div[2]/div[2]/table[3]/tbody[{0}]/tr/td[3]".format(num_fila))
        #
        #         tabla = self.browser.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div[2]/table[3]")
        #         tableRows = tabla.find_elements_by_tag_name("tr")
        #
        #         for fila in tableRows:
        #             for columna in fila.find_elements_by_tag_name("td"):
        #                 print columna.get_attribute('textContent')
        #
        #
        #         # print "Nombre: " + nombre.get_attribute('textContent') + " Valor: " + valor.get_attribute('textContent')
        #         #
        #         # lista_componentes.append({"nombre": nombre.text, "unidad": unidad.text, "valor": valor.text})
        #
        #     except Exception as ex:
        #         print "Error: " + str(ex)


        try:

            # # tabla = WebDriverWait(self.browser, 1).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/div[2]/table[3]")))
            # tabla = self.browser.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div[2]/table[3]")
            # tableRows = tabla.find_elements_by_tag_name("tr")
            #
            # for fila in tableRows:
            #     columnas = fila.find_elements_by_tag_name("td")
            #     # if columnas:
            #     #     if columnas[0].get_attribute('textContent') not in ["Proximales", "Hidratos de Carbono", "Grasas", "Vitaminas", "Minerales"]:
            #     #         # lista_componentes.append({"nombre": columnas[0].get_attribute('textContent'),
            #     #         #                           "unidad": columnas[2].get_attribute('textContent'),
            #     #         #                           "valor": columnas[1].get_attribute('textContent')})
            #     #
            #     #         lista_componentes.append({"nombre": columnas[0].text,
            #     #                                   "unidad": columnas[2].text,
            #     #                                   "valor": columnas[1].text})

            root = lxml.html.fromstring(self.browser.page_source)
            for row in root.xpath("//table[3]//tr"):
                cells = row.xpath(".//td")
                if cells:
                    if cells[0].text_content() not in ["Proximales", "Hidratos de Carbono", "Grasas", "Vitaminas", "Minerales"]:
                        lista_componentes.append({"nombre": cells[0].text_content(),
                                                      "unidad": cells[2].text_content(),
                                                      "valor": cells[1].text_content()})

        except Exception as ex:
            print "Error: " + str(ex)

        return lista_componentes


    def to_csv(self, nombre_fichero="alimentos.csv"):
        """
        Rutina que vuelca la informacion parseada de la pagina en un archivo .csv para dar lugar al dataset
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

        # Si el fichero esta abierto, se cierra al finalizar la rutina
        if csvfile:
            print "Cerrando fichero {0}...".format(nombre_fichero)
            csvfile.close()


    def parseo(self, show_time = False):
        """
        Rutina que realiza todo el proceso de parseo:
        1. Crea una instancia del navegador
        2. Accede a la url base
        3. Navega por los botones hasta llegar a la pagina que contiene una lista con los alimentos a obtener
        4. Accede a cada alimento, parsea su informacion y lo guarda en un objeto de tipo Alimento

        :param show_time    Indica si se mide el tiempo del proceso de parseo. Por defecto es False
        :return:
        """

        # Si el parametro show_time es True, se arranca un timer para medir el tiempo de la tarea de parseo
        if show_time:
            inicio_proceso = time.time()

        # 1. Se inicia el navegador
        self.start_browser()

        # Se hace que el navegador vaya a la url que queremos parsear
        self.ir_a_url(self.url)

        # 3. Navegacion por los botones
        # 3.1. Hacemos click en el boton "Consulta"
        button = self.browser.find_element_by_css_selector('div.link:nth-child(4) > a:nth-child(1)')
        if not button:
            print "El boton 'Consulta' no existe. Se cancela el proceso"
            return False

        button.click()

        # 3.2. Hacemos click en el boton "Lista alfabetica"
        button = self.browser.find_element_by_css_selector('#Alfabetica')
        if not button:
            print "El boton 'Lista alfabetica' no existe. Se cancela el proceso"
            return False

        button.click()


        # 3.3. Hacemos click en el boton "Todos"
        button = self.browser.find_element_by_css_selector('#alphabet > p:nth-child(1) > a:nth-child(1)')
        if not button:
            print "Error al obtener el boton Todos"
            return False

        button.click()
        time.sleep(1)

        # 4. Se accede al primer elemento de la lista pinchando en el nombre del alimento.
        # Se parsea la informacion de la pagina y se encapsula en un objeto Alimento. Finalmente se pincha en
        # "Listado anterior" para volver a la lista y repetir el proceso con el siguiente elemento hasta llegar al
        # final de la lista.
        for i in range(self.inicio_parseo,950):
            try:
                # En cada iteracion se guarda el incice del elemento que se esta parseando, para que en caso de fallo
                # se pueda repetir el proceso desde el elemento que fallo
                self.inicio_parseo = i

                # 4.1 Se obtiene el link a la pagina de informacion del elemento y se accede ella
                elemento = self.browser.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div[2]/table/tbody/tr[{0}]/td[2]/a".format(i))
                nombre = elemento.text
                print "Obteniendo informacion de: " + nombre
                elemento.click()            # Se accede al elemento
                time.sleep(0.1)

                # Se inicia el tiempo de parseo del alimento
                if show_time:
                    inicio_alimento = time.time()

                # 4.2 Se obtiene una lista con los componentes de dicho alimento
                componentes = self.parsea_info_alimento()

                if show_time:
                    final_alimento = time.time()
                    print "Tiempo de parseo de " + nombre + ": %d segundos" % (final_alimento - inicio_alimento)

                # 4.3. Se encapsula la informacion obtenida en un objeto de tipo Alimentos
                self.alimentos.append(Alimento(nombre, componentes))

                # 4.4. Se pincha en el boton "Lista anterior" para poder repetir el proceso con los siguientes alimentos
                volver = self.browser.find_element_by_xpath("//*[@id='Todos']")
                volver.click()

                time.sleep(0.1)

            except NoSuchElementException as ex:
                print "Elemento %d no encontrado" % i
                print ex

        # Se obtiene la marca de tiempo tras el parseo y se calcula la diferencia respecto al inicio
        if show_time:
            final_proceso = time.time()
            print "Tiempo total de parseo: %d segundos" % (final_proceso - inicio_proceso)

