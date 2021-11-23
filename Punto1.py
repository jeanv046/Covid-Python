

import pandas
filename = 'covid_22_noviembre.csv'
data = pandas.read_csv(filename, header=0)


print("El numero de contagios es...")
print(len(data))

#Punto 2
print("")
print("El numero de municipios afectados es {}".format(len(data["Nombre municipio"].unique())))


#Punto 3
print("")
print("Los municipios afectados son...")
print(data["Nombre municipio"].unique().tolist())

#Punto 4
print("")
print(data["Ubicación del caso"].unique().tolist())
print("El numero de personas que se encuentran en atención en casa son:")
print(len(data.loc[(data["Ubicación del caso"] == "casa") | (data["Ubicación del caso"] == "Casa") | (data["Ubicación del caso"] == "CASA")]  ))


