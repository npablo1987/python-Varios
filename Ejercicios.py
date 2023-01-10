from reportlab.platypus import (SimpleDocTemplate, Spacer,Table)
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
import os

fila = int(input("ingrese numero de filas: "))
columnas = int(input("ingrese las columnas: "))

aumentovariable = int(input("ingrese variable aumento: "))

matrizoriginal = []
matrizoriginald = []

for i in range(fila):
    a = [0]*columnas
    matrizoriginal.append(a)

for i in range(fila):
    a = [0]*columnas
    matrizoriginald.append(a)


def imprim(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            print(""+str(i)+","+str(j)+" = "+str(matriz[i][j])+"   ", end='')
        print("")

def completarasedente(matriz, fila, num, colum):    
    asedente = 1
    numa= num
    numd = num
    nums = num
    if fila == 0 : 
        asedente = 1
        for j in range(len(matriz)):
            matriz[fila][j] = asedente
            asedente = asedente + numa
    elif fila % 2 == 0:
        asedente = 1
        for j in range(len(matriz)):
            matriz[fila][j] = asedente
            asedente = asedente + numd
    else:
        total = num * colum -1
        for j in range(len(matriz)):
             matriz[fila][j] = total
             total = total - nums

  
for i in range(len(matrizoriginald)):
    completarasedente(matrizoriginald, i, aumentovariable,columnas)
        
imprim(matrizoriginald) 


doc = SimpleDocTemplate("prueba.pdf", pagesize = A4)
story = []

datos = matrizoriginald

tabla = Table(data = datos,
              style = [
                      ('GRID',(0,0),(-1,-1), 0.5, colors.grey),
                      ('BOX',(0,0),(-1,-1),1,colors.black),
                      ('BACKGROUND',(0,0), (-1,0), colors.white),
                      ]
             )
story.append(tabla)
story.append(Spacer(0,15))
doc.build(story)
os.system("prueba.pdf")