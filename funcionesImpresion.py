# -*- coding: utf-8 -*-
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

def imprimeFormatoDia(matriz, nDia):    
    cadenaImprimir = '\t\t'
    lDia = ['L', 'M', 'X', 'J', 'V', 'S', 'D']
    iterador = 1
    semanas = len(matriz[0])
    if (semanas == 4):
        nColum  = 2
    else:
        nColum = 3
    
    for valorVectorDia in matriz[nDia]:
        #formato de Letra del día
        if(valorVectorDia == 0):
            if(nDia < 5): #formato de lunes a viernes fuera de mes
                cadenaImprimir +=  lDia[nDia]
            else: # formato de sábados y domingos fuera de mes
                cadenaImprimir +=   "\\textit{" + lDia[nDia] + '}'
        else:
            if(nDia < 5): #formato de lunes a viernes
                cadenaImprimir += lDia[nDia] + '_{' + str(int(valorVectorDia)) + '}'
            else: #formato sábados y domingos
                cadenaImprimir += "\\textit{" + lDia[nDia] + '}_{' + str(int(valorVectorDia)) + '}'
        #formato de espaciado e intro
        if (iterador < nColum):
            cadenaImprimir += ' & '
        else:
            cadenaImprimir += ' \\\\'
            break
        iterador += 1       
    print cadenaImprimir

def imprimeFormatoCuadrados(matriz, nDia):
    cadenaImprimir = '\t\t'
    cadenaImprimir2 = '\t\t'
    iterador = 1
    semanas = len(matriz[0])

    if (semanas == 4):
        nColum  = 2
    else:
        nColum = 3

    for valorVectorDia in matriz[nDia]:
        if(valorVectorDia == 0):
            cadenaImprimir += ' '
            cadenaImprimir2 += ' '
        else:
            cadenaImprimir += '\\makebox{$\\square$}\\dotfill'
            if(nDia < 5):
                cadenaImprimir2 += '\\dotfill'
        if (iterador < nColum):
            cadenaImprimir += ' & '
            if(nDia < 5):
                cadenaImprimir2 += ' & '
        else:
            cadenaImprimir += ' \\\\'
            if(nDia < 5):
                cadenaImprimir2 += ' \\\\'
            break
        iterador += 1
    print cadenaImprimir
    print cadenaImprimir2


def cierraPaginaUno():
    print '\t\t\\bottomrule'
    print '\t\\end{longtabu}'
    print '\\clearpage'


def imprimePaginaIzq(matriz, nMes): 

    meses = ['cero', 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

    imprimeMesCabeceraIzqd(meses[nMes], len(matriz[0]))
    
    nSemanasDelMes = len(matriz[0])
    if(nSemanasDelMes == 5):
        Col = 3
    elif(nColum == 4):
        Col = 2
    elif(nColum == 6):
        Col = 3
    
    for dia in range(7):
        imprimeFormatoDia(matriz, dia)
        if(dia < 5):
            for i in range(Col):
                imprimeFormatoCuadrados(matriz, dia)
        else:
            imprimeFormatoCuadrados(matriz, dia)

        if(dia < 5):
            print("\n\t\t\\hline\n")
    
    cierraPaginaUno()


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


