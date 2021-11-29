

import pandas
import numpy as np
import matplotlib.pyplot as plt
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

#Punto 15
fallecidos = data[data['Estado'] == 'Fallecido']
fall_dep = fallecidos.groupby('Nombre municipio').size()
fall_dep_ord = fall_dep.sort_values(ascending=False).head(10)
print("Los 10 municipios con mas fallecidos: {}".format(fall_dep_ord))

#Punto 16
rec = data[data['Recuperado'] == 'Recuperado']
rec_dep = rec.groupby('Nombre municipio').size()
rec_dep_ord = rec_dep.sort_values(ascending=False).head(10)
print("Los 10 municipios con mas Recuperados: {}".format(rec_dep_ord))

#Punto 17
agrupado = data.groupby(['Nombre departamento'])
ordenado = agrupado.size().sort_values(ascending=False)
print("las ciudades con mas casos de contagiados: {}".format(ordenado))

#Punto 18
dat = data.groupby(['Nombre departamento', 'Nombre municipio', 'Sexo'])
cantidad = dat.size()
print("la cantidad de mujeres y hombres contagiados: {}".format(cantidad))

#Punto 19
dat = data.groupby(['Nombre departamento', 'Nombre municipio', 'Sexo'])
cantidad = dat.Edad.mean()
print("la cantidad de mujeres y hombres contagiados: {}".format(cantidad))

#Punto 20
print("")
conta = data.groupby('Nombre del país').size().sort_values(ascending=False)
print("El número de contagiados por país de procedencia: {}".format(conta))

#Punto 21
print("")
fech = data.groupby('Fecha de diagnóstico').size().sort_values(ascending=False)
print("Las fechas donde se presentaron mas contagios: {}".format(fech))

#Punto 22
canti = data.groupby('Estado').size()
mor = ((canti / canti.sum()) * 100)['Fallecido']
canti = data.groupby('Recuperado').size()
Rec = ((canti / canti.sum()) * 100)['Recuperado']
print("tasa de mortalidad {}%, recuperación {}% de Colombia".format(round(mor, 2), round(Rec, 2)))


def calculoOr(a):
    return np.logical_or(a == 'Fallecido', a == 'Recuperado')
#Punto 23
datafil = data[calculoOr(data['Estado'])]
canti = datafil.groupby(['Nombre departamento', 'Estado']).size()
tasaMor = ((canti / canti.sum()) * 100)
print("tasa de mortalidad y recuperación departamento: {}".format(tasaMor))

#Punto 24
datafil = data[calculoOr(data['Estado'])]
canti = datafil.groupby(['Nombre departamento', 'Estado']).size()
tasaMor = ((canti / canti.sum()) * 100)
print("tasa de mortalidad y recuperación ciudad: {}".format(tasaMor))

#Punto 25
print("")
grupo = data.groupby(['Nombre departamento', 'Ubicación del caso']).size()
print("ciudad la cantidad de personas por atención: {}".format(grupo))

#Punto 26
print("")
dat = data.groupby(['Nombre departamento', 'Sexo'])
cantidad = dat.Edad.mean()
print("la cantidad de mujeres y hombres contagiados: {}".format(round(cantidad, 0)))

#Punto 27
print("")
contagio = data.groupby('Fecha de diagnóstico').size().cumsum()

fallecidos_total = data[data['Estado'] == 'Fallecido']
muerte = fallecidos_total.groupby('Fecha de diagnóstico').size().cumsum()

rec_total = data[data['Recuperado'] == 'Recuperado']
recuperado = rec_total.groupby('Fecha de diagnóstico').size().cumsum()

fig = plt.figure(figsize=(12, 5))
p1, p2, p3 = plt.plot(contagio.index, contagio.values, muerte.index,
                      muerte.values, recuperado.index, recuperado.values)
plt.legend(('Contagio', 'Muerte', 'Recuperado'),
           prop={'size': 10}, loc='upper right')
plt.title("Grafico de contagio, muerte y recuperación Colombia")
plt.show()
























