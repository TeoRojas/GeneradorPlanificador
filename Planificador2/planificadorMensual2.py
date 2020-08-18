# -*- coding: utf-8 -*-
from funcionesgeneracion import *


mesNombre = ['0', 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio','Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']


print("Introduzca el año que quiere generar -ej: 2020-")
ano = input()


for mes in range(1,13):
    if(mes < 10):
        nombreArchivo = '0' 
    else:
        nombreArchivo = ''
    nombreArchivo += str(mes) + "_" + mesNombre[mes] + "_" + 'pm2' + ".tex"

    original_stdout = sys.stdout
    with open("../Resultados/" + nombreArchivo, 'w') as f:
        sys.stdout = f
        
        matriz = generaMatrizMensual(mes, ano)
        imprimePaginaIzq(matriz, mes)
        imprimePaginaDch(matriz, mes)

        sys.stdout = original_stdout 
