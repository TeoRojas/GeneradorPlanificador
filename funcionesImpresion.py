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

def imprimeFormatoDia(matriz, nDia, nColum):    
    cadenaImprimir = '\t\t'
    lDia = ['L', 'M', 'X', 'J', 'V', 'S', 'D']
    iterador = 1
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

def imprimeFormatoCuadrados(matriz, nDia, nColum):
    cadenaImprimir = '\t\t'
    cadenaImprimir2 = '\t\t'
    iterador = 1
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
    #Imprime estructura L & L_{6} & L_{13}
    #nDia = 0 -> 'L', dia = 1 -> 'M', [número de día]
    #lDia [letra de día]
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
        imprimeFormatoDia(matriz, dia, Col)
        if(dia < 5):
            for i in range(Col):
                imprimeFormatoCuadrados(matriz, dia, Col)
        else:
            imprimeFormatoCuadrados(matriz, dia, Col)

        if(dia < 5):
            print("\n\t\t\\hline\n")
    
    cierraPaginaUno()




