

import pandas
filename = 'covid_22_noviembre.csv'
data = pandas.read_csv(filename, header=0)


print("El numero de contagios es...")
print(len(data))



