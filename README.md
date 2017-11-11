# Dataset de Composición de Alimentos
**Gregorio de Miguel Vadillo** 

**Carlos Muñiz Solaz**

**Fecha de creación:** Octubre 2017

![Alt text](/images/logo/Food-composition.jpg?raw=true)

Repositorio generado durante la Práctica 1 de la asignatura *Tipología y ciclo de vida de los datos* del *Máster de Ciencia de Datos* de la *UOC*. En esta práctica hemos realizado *Web Scraping* sobre la **Base de Datos Española de Composición de Alimentos (BEDCA)** para generar un dataset sobre la composición de los alimentos. En el repositorio se puede encontrar el código desarrollado así como el dataset generado. 
Página oficial de BEDCA: http://www.bedca.net/

# Contexto
Las **Bases de Datos de Composición de Alimentos (BDCA)** son un conjunto de informaciones que detallan los componentes más importantes de los alimentos, así como sus valores de energía y nutrientes. Entre estos componentes, encontramos las *proteínas*, los *carbohidratos*, las *grasas*, las *vitaminas*, los *minerales* y otros componentes nutricionales importantes como la *fibra*.

Antes de la aparición de los ordenadores, la información sobre los componentes de alimentos se recogía en tablas impresas. Hoy en día, existen métodos muy avanzados para determinar esos componentes. Entre ellos podemos destacar:
* Análisis químico de muestras llevado a cabo por laboratorios analíticos
* Cálculos valores derivados de otros datos ya incluidos en la base de datos
* Estimación de valores de otras fuentes. Esto puede ser de la etiquetas de los fabricantes, de documentación científica o de bases de datos de otros países

Para más información sobre las *Bases de Datos de Composición de Alimentos* ver:

http://www.fao.org/3/a-y4705s.pdf

https://en.wikipedia.org/wiki/Food_composition_data

# Contenido
El dataset que hemos generado contiene el siguiente fichero:
alimentos.csv
Cuyos campos son:

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

Por último, es importante tener en cuenta el periodo de tiempo de los datos. Debido a los recursos, mucho de los valores no están actualizados o son muy difíciles de obtener con exactitud. También hay que tener en cuenta que los métodos para obtener los componentes van variando a lo largo de los años, con lo que es posible que los datos del dataset se queden obsoletos.

# Posibles usos del Dataset

Las aplicaciones de las *Base de Datos de Composición de Alimentos* es muy amplio. Algunos ejemplos para los que se usan estas bases de datos son la:

* Elaboración de *dietas terapéuticas*: para tratar la obesidad, diabetis, alergias e intolerancias a alimentos
* Elaboración de *dietas institucionales*: colegios, hospitales, prisiones, centros de día
* Elaboración de *dietas epidemiológicas*: estudiar el efecto de las dietas sobre la población. Por ejemplo, para perder peso, ganar musculo, ...
* Realización de estudios cuantitativos sobre la nutrición humana
* Para educar a la población sobre los alimentos y sus nutrientes
* Para elaborar las etiquetas de los productos procesados

# Estructura del repositorio

# Licencia
El dataset de Composición de Alimentos de Gregorio de Miguel Vadillo y Carlos Muñiz Solaz se encuentra bajo la licencia **CC-BY-SA 4.0**.

https://creativecommons.org/licenses/by-sa/4.0/legalcode

como se explica en:

https://creativecommons.org/licenses/

![Alt text](/images/copyright/by-sa.png?raw=true)

# Agradecimientos

Nos gustaría agradecer a la RedBEDCA por la elaboración de la base de datos con la composición de alimentos y la página web que nos ha permitido generar nuestro dataset.

http://www.bedca.net/
https://www.bedca.net/bdpub/UsoBD.pdf

Agradecer también a las distintas fuentes que han permitido conocer la composición de los alimentos y que ha permitido su incorporación en la base de datos. Se puede encontrar más información sobre las distintas fuentes en el siguiente enlace:

http://www.bedca.net/bdpub/index.php








