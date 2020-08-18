# -*- coding: utf-8 -*-
from calendar import monthrange
import sys

diaSemana = ['L', 'M', 'X', 'J', 'V', 'S', 'D']
mesNombre = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio','Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
esPagIzq = True

def imprimirPlanificadorMensual(numeroMes, numeroAno):
    if(mes < 9):
        nombreArchivo = '0' 
    else:
        nombreArchivo = ''
    nombreArchivo += str(numeroMes+1) + "_" + mesNombre[numeroMes] + "_" + 'pm1' + ".tex"

    original_stdout = sys.stdout
    with open("../Resultados/" + nombreArchivo, 'w') as f:
        sys.stdout = f
        #generarPlanificadorMensual(numeroMes, numeroAno)
        imprimePagIzq(mesNombre[numeroMes], esPagIzq)
        imprimePagDrcha(numeroMes, numeroAno, esPagIzq)
        sys.stdout = original_stdout 

def generarPlanificadorMensual(numeroMes, numeroAno):
    posicionDelDiaDeLaSemana = monthrange(numeroAno, numeroMes+1)[0]
    cantidadDiasDelMes = monthrange(numeroAno, numeroMes+1)[1]    
    for numeroDia in range(cantidadDiasDelMes):
        dia = diaSemana[posicionDelDiaDeLaSemana]
        print ( '\t\t' + dia + '_{' + str(numeroDia+1) + '}' + ' \dotfill' + "\\"+ "\\")
        if(dia == 'D'):
            print '\t\t\\hline'
        if (posicionDelDiaDeLaSemana == 6):
            posicionDelDiaDeLaSemana = -1
        posicionDelDiaDeLaSemana += 1

    print '\n\t\t\\bottomrule\n'


def imprimeCabecera(mesNombre, esPagIzq):
    if(esPagIzq):
        print '\\raggedleft{'
    else:
        print '\\raggedright{'

    print '\t\\fontsize{25}{50}\\selectfont'

    if(esPagIzq):
        print '\t\\textbf{' + mesNombre + '}\\\\'
    else:
        print '\t\\textbf{\\NextYear}'

    if(esPagIzq):
        print '}'
    else:
        print '}\\scriptsize{\\textbf{planificador mensual$_1$}}\\\\[11.3pt]' 
    
    print '\n\n'

    if(esPagIzq):
        print '\t\\textbf{\\\\Foco del mes:} \\dotfill'
    else:
        print '\t\\noindent\\dotfill'

    print '\t\\renewcommand{\\arraystretch}{1.5}\\scriptsize' 
    print '\t\t\\begin{longtabu} to \\textwidth { X[l]}'  
    print '\t\t\\centering \\small{\\textbf{TO-DO}} \\\\'
    print '\t\t\\toprule'    

def imprimeCuadroYPuntos():
    print '\t\t\\makebox{$\\square$} \\dotfill\\\\' 

def imprimeCuerpoPagIzq():
    for linea in range(25):
        imprimeCuadroYPuntos()
    print '\n\t\t\\bottomrule\n'
    print '\t\t\\\\'
    print '\t\t\\small{\\textbf{PROYECTOS}} \\\\'
    for linea in range(4):
        imprimeCuadroYPuntos()

def cierraPag():
    print '\t\\end{longtabu}\n\n'
    print '\\clearpage'

def imprimePagIzq(mesNombre, esPagIzq):
    imprimeCabecera(mesNombre, esPagIzq)
    imprimeCuerpoPagIzq()
    cierraPag()

def imprimePagDrcha(numeroMes, numeroAno, esPagIzq):
    imprimeCabecera(mesNombre[numeroMes], not esPagIzq)
    generarPlanificadorMensual(numeroMes, numeroAno)  
    cierraPag()



print("Introduzca el año que quiere generar -ej: 2020-")
ano = input()
for mes in range(12):
    imprimirPlanificadorMensual(mes, ano)

