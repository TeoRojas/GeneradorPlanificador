# -*- coding: utf-8 -*-
import numpy as np

def copiarDesde():
    print "%%%%%%%%%%%%% COPIAR DESDE AQUÍ %%%%%%%%%%%%%%%%%%%"

def copiarHasta():
    print "%%%%%%%%%%%%% COPIAR HASTA AQUÍ %%%%%%%%%%%%%%%%%%%"
    
def imprimeMesCabeceraIzqd(mesEnTexto, nSemanas):
    print "\\clearpage"
    print "{\\raggedleft"
    print "\t\\fontsize{25}{50}\\selectfont"
    print "\t\\textbf{"+ mesEnTexto +"}\\\\"
    print "}\n\n"
    if(nSemanas == 4):
        print "\t\\renewcommand{\\arraystretch}{1.25}\\scriptsize"
        print "\t\\begin{longtabu} to \\textwidth { X[l] X[l]}"
        print "\t\t\\centering \\textbf{Semana1} &  \\centering\\textbf{Semana2}  \\\\"
    else:
        print "\t\\renewcommand{\\arraystretch}{1.24}\\scriptsize"
        print "\t\\begin{longtabu} to \\textwidth { X[l] X[l] X[l]}"
        print "\t\t\\centering \\textbf{Semana1} &  \\centering\\textbf{Semana2}  &   \centering\\textbf{Semana3}  \\\\"
        
    print "\t\t\\toprule"


def cierraPagina():
    print '\t\t\\bottomrule'
    print '\t\\end{longtabu}'
    print '\\clearpage'


def imprimeMesCabeceraDch(nSemanas):
    print "%Página siguiente"
    print "{\\raggedright"
    print "\t\\fontsize{25}{50}\\selectfont"
    print "\t\\textbf{\\NextYear}"
    print "}\\scriptsize{\\textbf{planificador mensual$_2$}}\n\n"
    if(nSemanas <= 5):
        print "\t\\renewcommand{\\arraystretch}{1.39}\\scriptsize"
        print "\t\\begin{longtabu} to \\textwidth { X[l] X[l]}"
        print "\t\t\\centering \\textbf{Semana4} &  \\centering\\textbf{Semana5}  \\\\"
    else:
        print "\t\\renewcommand{\\arraystretch}{1.24}\\scriptsize"
        print "\t\\begin{longtabu} to \\textwidth { X[l] X[l] X[l]}"
        print "\t\t\\centering \\textbf{Semana4} &  \\centering\\textbf{Semana5}  &   \centering\\textbf{Semana6}  \\\\"
        
    print "\t\t\\toprule"


def imprimeDia(vNumerosDia, letraDia):   
    #Para pag izquierda pasarle como argumento matriz[0][:(nSemanasDelMes/2)+(nSemanasDelMes%2)]
    #Para pag derecha pasarle como argumento matriz[0][(nSemanasDelMes/2)+(nSemanasDelMes%2):] 
    # vNumerosDia tiene la mitad de los números de un mismo día del mes, es decir xej Lunes 1, Lunes 8, Lunes 16 --> [1,8,16]
    cadenaImprimir = '\t\t'
    i = 1
    for dia in vNumerosDia:
        if(letraDia != 'S' and letraDia != 'D'):
            if(dia == 0):
                cadenaImprimir += letraDia
            else:
                cadenaImprimir += letraDia + '_{' + str(int(dia)) + '}'
        else:
            if(dia == 0):
                cadenaImprimir += "\\textit{" + letraDia + '}'
            else:
                cadenaImprimir += "\\textit{" + letraDia + '}_{' + str(int(dia)) + '}'            

        if (i < len(vNumerosDia)):
            cadenaImprimir += ' & '
        else:
            cadenaImprimir += ' \\\\'
        i += 1  
    print cadenaImprimir


def imprimeCuadradosParaUnDia(vNumerosDia):
    #Para pag izquierda pasarle como argumento matriz[0][:(nSemanasDelMes/2)+(nSemanasDelMes%2)]
    #Para pag derecha pasarle como argumento matriz[0][(nSemanasDelMes/2)+(nSemanasDelMes%2):]
    cadenaImprimir = '\t\t'
    cadenaImprimir2 = '\t\t'
    i = 1
    for dia in vNumerosDia:
        if(dia == 0):
            cadenaImprimir += ' '
            cadenaImprimir2 += ' '
        else:
            cadenaImprimir += '\\makebox{$\\square$}\\dotfill'
            cadenaImprimir2 += '\\dotfill'
 
        if (i < len(vNumerosDia)):
            cadenaImprimir += ' & '
            cadenaImprimir2 += ' & '
        else:
            cadenaImprimir += ' \\\\'
            cadenaImprimir2 += ' \\\\'
        i += 1
    print cadenaImprimir
    print cadenaImprimir2


def imprimePaginaDch(matriz, nMes): 
    nSemanasDelMes = len(matriz[0])
    letraDias = ['L', 'M', 'X', 'J', 'V', 'S', 'D']
    
    imprimeMesCabeceraDch(nSemanasDelMes)
    
    for iterador in range(7):
        imprimeDia(matriz[iterador][(nSemanasDelMes/2)+(nSemanasDelMes%2):], letraDias[iterador])
        imprimeCuadradosParaUnDia(matriz[iterador][(nSemanasDelMes/2)+(nSemanasDelMes%2):])

    print("\n\t\t\\hline\n")
    
    cierraPagina()


def imprimePaginaIzq(matriz, nMes):
    nSemanasDelMes = len(matriz[0])
    letraDias = ['L', 'M', 'X', 'J', 'V', 'S', 'D']
    mesEnTexto = ['cero', 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

    imprimeMesCabeceraIzqd(mesEnTexto[nMes], nSemanasDelMes)

    for iterador in range(7):
        imprimeDia(matriz[iterador][:(nSemanasDelMes/2)+(nSemanasDelMes%2)], letraDias[iterador])
        imprimeCuadradosParaUnDia(matriz[iterador][:(nSemanasDelMes/2)+(nSemanasDelMes%2)])

    print("\n\t\t\\hline\n")
    
    cierraPagina()
