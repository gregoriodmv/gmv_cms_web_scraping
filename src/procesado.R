##############################
# Descripción: Este script procesa el fichero alimentos_raw.csv 
#
# Autores: Gregorio de Miguel Vadillo
#          Carlos Muñiz Solaz
#############################

# Cargamos el fichero
options(OutDec= ",")
alimentos <- read.csv2(file.choose(), header = TRUE, encoding = "UTF-8")

# Actualizamos el nombre de columnas
colnames (alimentos) <- c("Nombre", "Alcohol (g)", "Energía total (kCal)", "Grasa total (g)","Proteina total (g)","Agua (g)", "Fibra total (g)", 
  "Carbohidratos (g)", "A.G docosahexaenóico(g)", "A.G monoinsaturados (g)","A.G poliinsaturados (g)", "A.G saturados.totales.(mg)", 
  "A.G 12.0", "A.G 14.0(mg)", "A.G 16.0(mg)", "A.G 18.0(mg)", "A.G 18.1 n-9 (mg)", "Colesterol(mg)", "A.G 18.2 (mg)", "A.G 18.3 (mg)", 
  "A.G 20.4 n-6", "A.G 20.5", "Vitamina A (mg)", "Vitamina D (mg)", "Vitamina E (mg)", "Folato total(mg)",  "Equivalentes de niacina(mg)", 
  "Riboflavina (mg)",  "Tiamina (mg)", "Vitamina B12 (mg)", "Vitamina B6 (mg)",  "Vitamina C (mg)", "Calcio(mg)",  
  "Hierro total(mg)", "Potasio(mg)", "Magnesio (mg)", "Sodio(mg)", "Fósforo (mg)", "Ioduro (mg)", "Selenio total (mg)", "Zinc (mg)")  

# Usamos solo las kCal para las energias
alimentos$"Energía total (kCal)" <- as.character (alimentos$"Energía total (kCal)")
alimentos$"Energía total (kCal)"[alimentos$"Energía total (kCal)" == ""] <- "?(?)"
alimentos$"Energía total (kCal)"[alimentos$"Energía total (kCal)" == "-"] <- "?(?)"
alimentos$"Energía total (kCal)" <- gsub("[\\(\\)]", "", regmatches(alimentos$"Energía total (kCal)", gregexpr("\\(.*?\\)", alimentos$"Energía total (kCal)")))
alimentos$"Energía total (kCal)"[alimentos$"Energía total (kCal)" == "?"] <- "NA"

# Subtituimos los valores desconocidos por NA
alimentos <- as.data.frame(lapply(alimentos, function(y) gsub("traza", "0.0000000001", y)))
alimentos <- as.data.frame(lapply(alimentos, function(y) gsub("-", "NA", y)))
is.na(alimentos) <- alimentos == ""

# Cambiamos el delimitador numerico por commas
alimentos <- as.data.frame(lapply(alimentos, function(y) as.character(y)))
alimentos <- as.data.frame(lapply(alimentos, function(y) gsub("\\.", "\\,", y)))

# Generamos el fichero ya procesado
write.csv2 (alimentos, "alimentos_procesado.csv")
