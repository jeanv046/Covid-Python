

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

