#pip install xlrd
#
#
#
#archi1=open("datos.txt","w") 
#archi1.write("Primer línea.\n") 
#archi1.write("Segunda línea.\n") 
#archi1.write("Tercer línea.\n")  
#archi1.close() 
import xlrd 
 
archivo = 'C:/Users/Pablo/Desktop/python/Dattos.xls'
  
wb = xlrd.open_workbook(archivo) 

hoja = wb.sheet_by_index(0) 
print(hoja.nrows) 
print(hoja.ncols) 
print(hoja.cell_value(1, 1))

nombres = hoja.row(0) 
print(nombres)

contador = 0
arxhivotxt=open("datos.txt","w") 
for i in range(hoja.nrows):
    for j in range(hoja.ncols):
        arxhivotxt.write(str(hoja.cell_value(i, j))+" ")         
        print(" "+str(hoja.cell_value(i, j))+" ", end='')
    print("\n")
    arxhivotxt.write("\n")  
    contador = contador + 1
print(contador)
arxhivotxt.close()  
# Lectura de columna
#for i in range(0,hoja.nrows):
#   print(hoja.cell_value(i,1))

ma