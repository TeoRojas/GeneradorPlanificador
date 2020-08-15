# -*- coding: utf-8 -*-
from calendar import monthrange
import sys

diaSemana = ['L', 'M', 'X', 'J', 'V', 'S', 'D']
mesNombre = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio','Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']


def imprimirPlanificadorMensual(numeroMes, numeroAno):
    nombreArchivo = str(numeroMes) + "_" + mesNombre[numeroMes-1] + "_" + str(numeroAno) + ".txt"
    original_stdout = sys.stdout
    with open("resultados/" + nombreArchivo, 'w') as f:
        sys.stdout = f
        print mesNombre[numeroMes-1] + " de " + str(numeroAno)
        print "--------------------------------------\n\n\n"
        generarPlanificadorMensual(numeroMes, numeroAno)
        sys.stdout = original_stdout 

def generarPlanificadorMensual(numeroMes, numeroAno):
    posicionDelDiaDeLaSemana = monthrange(numeroAno, numeroMes)[0]
    cantidadDiasDelMes = monthrange(numeroAno, numeroMes)[1]    
    for numeroDia in range(cantidadDiasDelMes):
        dia = diaSemana[posicionDelDiaDeLaSemana]
        print ( '\t\t' + dia + '_{' + str(numeroDia+1) + '}' + ' \dotfill' + "\\"+ "\\")
        if(dia == 'D'):
            print '\t\t\hline'
        if (posicionDelDiaDeLaSemana == 6):
            posicionDelDiaDeLaSemana = -1
        posicionDelDiaDeLaSemana += 1


print("Introduzca el año que quiere generar -ej: 2020-")
ano = input()
for mes in range(1,13):
    imprimirPlanificadorMensual(mes, ano)
                                      