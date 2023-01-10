import xlrd 
 
archivo = 'C:/Users/Pablo/Desktop/python/Datos.xls'
  
wb = xlrd.open_workbook(archivo) 

hoja = wb.sheet_by_index(0) 
print(hoja.nrows) 
print(hoja.ncols) 
print(hoja.cell_value(1, 3))
nombres = ["Nombres"]
apellidop = ["Apellido Paterno"]
apellidom = ["Apellido Materno"]

def dividir(nombre):
    arreglonombres = nombre.split()
    print()
    nombres.append(arreglonombres[0]+" "+arreglonombres[1])
    apellidop.append(arreglonombres[2])
    apellidom.append(arreglonombres[3])

for i in range(1,hoja.nrows):
    if hoja.cell_value(i, 3).count(' ') == 3:
        #print(hoja.cell_value(i, 3))
        dividir(hoja.cell_value(i, 3))
    else:
        print("el dato es un nombre compuesto")
        print(hoja.cell_value(i, 3))



