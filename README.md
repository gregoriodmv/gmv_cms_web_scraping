# Dataset de Composición de Alimentos
**Gregorio de Miguel Vadillo** 

**Carlos Muñiz Solaz**

**Fecha de creación:** Octubre 2017

![Alt text](/images/logo/Food-composition.jpg?raw=true)

Repositorio generado durante la Práctica 1 de la asignatura *Tipología y ciclo de vida de los datos* del *Máster de Ciencia de Datos* de la *UOC*. En esta práctica hemos realizado *Web Scraping* sobre la **Base de Datos Española de Composición de Alimentos (BEDCA)** para generar diversos datasets que podremos explotar en prácticas posteriores.

Página oficial de BEDCA: http://www.bedca.net/

# Contexto

Las **Bases de Datos de Composición de Alimentos (BDCA)** son un conjunto de informaciones que detallan los componentes más importantes de los alimentos, así como sus valores de energia y nutrientes. Entre estos componentes, encontramos las *proteinas*, los *carbohidratos*, las *grasas*, las *vitaminas*, los *minerales* y otros componentes nutricionales importantes como la *fibra*.

Antes de la aparición de los ordenadores, la información sobre los componentes de alimentos se recogían en tablas impresas. Hoy en día, existen métodos muy avanzados para determinar esos componentes. Entre ellos podemos destacar:
* Analisis quimico de muestras llevado a cabo por laboratorios analiticos
* Calculos valores derivados de otros datos ya incluidos en la base de datos
* Estimación de valores de otras fuentes. Esto puede ser de la etiquetas de los fabricantes, de documentación cientifica o de bases de datos de otros paises

Para más información sobre las *Base de Datos de Composición de Alimentos* ver:

http://www.fao.org/3/a-y4705s.pdf

https://en.wikipedia.org/wiki/Food_composition_data

# Contenido
El data set que hemos generado contiene los siguientes campos:

* Nombre del alimento
* Campos sobre carbohidratos: fibra o carbohidratos
* Campos sobre grasas: datos sobre los distintos ácidos grasos
* Campos sobre vitaminas: A, D, E, ...
* Campos sobre minerales: hierro, calcio,  ...
* Campos proximales: alcohol, energía total, grasa total, proteina total y agua

La mayoria de los campos son valores continuos que representan valores de masa (en g, mg o ug).
Existen campos de energia expresados en kJ o kCal.
Algunos micronutrientes cuyo porcentaje en el alimento es infimo contienen la etiqueta "traza" en lugar de un valor númerico.

A la hora de analizar los datos hay que tener en cuenta que:
* Existe una gran variabilidad de la composición de los alimentos entre paises
* Existen muchos datos incompletos tanto de alimentos como de nutrientes al desconocerse su valor

Por último, es importante tener en cuenta el periodo de tiempo de los datos. Debido a los recursos, mucho de los valores no están actualizados o son muy dificiles de obtener con exactitud. También hay que tener en cuenta que los métodos para obtener los componentes van variando a lo largo de los años, con lo que es posible que los datos del dataset se queden obsoletos.




Estructura del repositorio




