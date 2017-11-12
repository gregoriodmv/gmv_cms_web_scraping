"""
Script con los pasos para realizar el proceso de parseo
"""

from alimentos_scraper import *

# Se instancia el objeto para realizar web scraping a la pagina de alimentos
scraper = AlimentosScraper()

# Se inicia el proceso
ret = scraper.parseo()

# Solo si se ha terminado el proceso de parseo con exito obtenemos el fichero .csv con el dataset.
# El fichero se guaradara en el directorio actual de trabajo
if ret:
    scraper.to_csv()
