import random
from types import MappingProxyType


fila = int(input("ingrese numero de filas"))
columnas = int(input("ingrese las columnas"))

matrizoriginal = []
matriscua = []

for i in range(fila):
    a = [0]*columnas
    matrizoriginal.append(a)

for i in range(fila):
    a = [6]*columnas
    matriscua.append(a)

def imprim(matrizoooo):
    for i in range(len(matrizoooo)):
        for j in range(len(matrizoooo)):
            print(""+str(i)+","+str(j)+" = "+str(matrizoooo[i][j])+" ", end='')
        print("")


imprim(matrizoriginal)
imprim(matriscua)

for i in range(len(matrizoriginal)):
    for j in range(len(matrizoriginal)):
        matrizoriginal[i][j] = random.randint(0,10)

imprim(matrizoriginal)
