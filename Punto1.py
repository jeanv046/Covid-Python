

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

#Punto 5
print("")
print(data["Recuperado"].unique().tolist())
print("Número de personas que se encuentran recuperados: ")
print(len(data.loc[(data["Recuperado"] == "Recuperado")]))

#Punto 6
print("")
print(data["Estado"].unique().tolist())
print("Número de personas que ha fallecido: ")
print(len(data.loc[(data["Estado"] == "Fallecido")]))

#punto 7
print("")
print(data["Tipo de contagio"].unique().tolist())
print(data.loc[(data["Tipo de contagio"] == "Importado")])

#punto 8
print("")
print("El numero de departamentos afectados es {}".format(len(data["Nombre departamento"].unique())))

#Punto 9
print("")
print("Los departamentos afectados son...")
print(data["Nombre departamento"].unique().tolist())

#Punto 10
print("")
orden_casos = data.groupby('Ubicación del caso').size().sort_values(ascending=False)
print("El Odenamiento queda asi: {}".format(orden_casos))

#Punto 11
print("")
datos_agrupados = data.groupby('Nombre departamento')
dep_cont = datos_agrupados.size().sort_values(ascending=False).head(10)
print("Los 10 departamentos mas Casos de contagio: {}".format(dep_cont))

#Punto 12
fallecidos = data[data['Estado'] == 'Fallecido']
fall_dep = fallecidos.groupby('Nombre departamento').size()
fall_dep_ord = fall_dep.sort_values(ascending=False).head(10)
print("Los 10 departamentos con mas fallecidos: {}".format(fall_dep_ord))

#Punto 13
rec = data[data['Recuperado'] == 'Recuperado']
rec_dep = rec.groupby('Nombre departamento').size()
rec_dep_ord = rec_dep.sort_values(ascending=False).head(10)
print("Los 10 departamentos con mas Recuperados: {}".format(rec_dep_ord))

#Punto 14
datos_agrupados = data.groupby('Nombre municipio')
dep_cont = datos_agrupados.size().sort_values(ascending=False).head(10)
print("Los 10 municipios mas afectados: {}".format(dep_cont))


























