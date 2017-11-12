# Dataset de Composición de Alimentos
**Gregorio de Miguel Vadillo**   
**Carlos Muñiz Solaz**

**Fecha de creación:** Octubre 2017

![Alt text](/images/logo/Food-composition.jpg?raw=true)

Repositorio generado durante la Práctica 1 de la asignatura *Tipología y ciclo de vida de los datos* del *Máster de Ciencia de Datos* de la *UOC*. En esta práctica hemos realizado *Web Scraping* sobre la **Base de Datos Española de Composición de Alimentos (BEDCA)** para generar un dataset sobre la composición de los alimentos. En el repositorio se puede encontrar el código desarrollado así como el dataset generado.  

Página oficial de BEDCA: http://www.bedca.net/

# Contexto
Las **Bases de Datos de Composición de Alimentos (BDCA)** son un conjunto de informaciones que detallan los componentes más importantes de los alimentos, así como sus valores de energía y nutrientes. Entre estos componentes, encontramos las *proteínas*, los *carbohidratos*, las *grasas*, las *vitaminas*, los *minerales* y otros componentes nutricionales importantes como la *fibra*.
Para más información sobre las *Bases de Datos de Composición de Alimentos* ver:

http://www.fao.org/3/a-y4705s.pdf  
https://en.wikipedia.org/wiki/Food_composition_data

# Recogida de los datos
Antes de la aparición de los ordenadores, la información sobre los componentes de los alimentos se recogían en tablas impresas. Hoy en día, estos datos provienen de distintas fuentes y países y una vez consolidados se ponen a disposición pública a través de base de datos o páginas web.

Entre los métodos utilizados para obtener los datos encontramos:
* Análisis químico de muestras llevado a cabo por laboratorios analíticos
* Valores derivados de otros datos ya incluidos en la base de datos
* Estimación de valores de otras fuentes. Esto puede ser de la etiquetas de los fabricantes, documentación científica o bases de datos de otros países

# Contenido
El dataset inicial que hemos generado lo hemos guardado en el fichero: *alimentos_raw.csv*. Posteriormente, hemos generado otro dataset más procesado al que hemos llamado *alimentos_procesado.csv*.  
Los campos que encontramos en los datasets generados son los siguientes:

* Nombre del alimento
* Campos sobre carbohidratos: fibra o carbohidratos
* Campos sobre grasas: datos sobre los distintos ácidos grasos
* Campos sobre vitaminas: A, D, E,...
* Campos sobre minerales: hierro, calcio, ...
* Campos proximales: alcohol, energía total, grasa total, proteína total y agua

La mayoría de los campos son valores continuos que representan valores de masa (en g, mg o ug).  
Existen campos de energía expresados en kJ o kCal.  
Algunos micronutrientes cuyo porcentaje en el alimento es ínfimo se representan mediante la etiqueta "traza" en lugar de un valor numérico.

A la hora de analizar los datos hay que tener en cuenta que:
* Existe una gran variabilidad de la composición de los alimentos entre los distintos países
* Existen muchos datos incompletos tanto de alimentos como de nutrientes al desconocerse su valor

Por último, es importante tener en cuenta el *periodo de tiempo de los datos*. Debido a limitaciones en los recursos, mucho de los valores no están actualizados o son muy difíciles de obtener con exactitud. También hay que tener en cuenta que los métodos para obtener los componentes van variando a lo largo de los años, con lo que es posible que el dataset que hemos generado se quede obsoleto a lo largo de los años.

# Posibles usos del Dataset
Las aplicaciones de las *Base de Datos de Composición de Alimentos* es muy amplio. Algunos ejemplos para los que se usan estas bases de datos son la:

* Elaboración de *dietas terapéuticas*: para tratar la obesidad, diabetis, alergias e intolerancias a alimentos
* Elaboración de *dietas institucionales*: colegios, hospitales, prisiones, centros de día
* Elaboración de *dietas epidemiológicas*: estudiar el efecto de las dietas sobre la población. Por ejemplo, para perder peso, ganar musculo, ...
* Realización de estudios cuantitativos sobre la nutrición humana
* Para educar a la población sobre los alimentos y sus nutrientes
* Para elaborar las etiquetas de los productos procesados

# Estructura del repositorio
La estructura del repositorio es la siguiente:
* *src*: Directorio que contiene el código fuente en python para la creación del dataset inicial y el script en R para el procesamiento posterior
* *dataset*: Directorio con dos ficheros csv. El dataset creado mediante web scraping (*alimentos_raw.csv*) y el dataset ya procesado (*alimentos_procesado.csv*) mediante R. 
* *images*: Directorio con todas las imagenes que se visualizan en el proyecto
* *HEADER* y *CC-BY-SA-4.0*: Ficheros de licencia
* *README.md*: Este fichero

# Programas usados para la creación del repositorio
Para la realización de la práctica hemos utilizado las siguientes herramientas:
* *Python requests library*: Permite la descargas de páginas web
* *Selenium*: Permite interactuar con las páginas web. Por ejemplo, hacer click sobre un botón determinado de la página web
* *lxml*: Poporciona de herramientas para procesar el contenido obtenido de las páginas web 
* *Rstudio*: Es la herramienta que nos ha permitido realizar un procesamiento más avanzando del dataset

Para más información técnica sobre la práctica se puede visitar la wiki:  
[Wiki](../../wiki)


# Licencia
El dataset de Composición de Alimentos de Gregorio de Miguel Vadillo y Carlos Muñiz Solaz se encuentra bajo la licencia **CC-BY-SA 4.0**.  
https://creativecommons.org/licenses/by-sa/4.0/legalcode

como se explica en:  
https://creativecommons.org/licenses/  
![Alt text](/images/copyright/by-sa.png?raw=true)

Se ha elegido está licencia ya que maximiza su difusión y permitir a otros remezclar, retocar, y crear a partir de ella. Se ha preferido elegir una licencia SA BY sobre una BY para que las obras que deriven de esta se licencien bajo las mismas condiciones.

# Agradecimientos

Nos gustaría agradecer a la RedBEDCA por la elaboración de la base de datos con la composición de alimentos y la página web que nos ha permitido generar nuestro dataset.  
http://www.bedca.net/

Agradecer también a las distintas fuentes que han permitido conocer la composición de los alimentos y que han posibilitado su incorporación en la base de datos. Se puede encontrar más información sobre las distintas fuentes en el siguiente enlace:
http://www.bedca.net/bdpub/index.php








