# -*- coding: utf-8 -*-
import calendar
from calendar import monthrange
import sys
import numpy as np
from funcionesImpresion import *

ano = 2019
mes = 6
diaSemana = ['L', 'M', 'X', 'J', 'V', 'S', 'D']
numSemanasDelMes = len(calendar.monthcalendar(ano,mes))

def cantidadSemanasDelMes(mes, ano):
    #print "número de mes: " + str(mes)
    #print "número de semanas de ese mes: " + str(len(calendar.monthcalendar(ano,mes)))
    return len(calendar.monthcalendar(ano,mes))

def generaMatrizMensual(mes, ano):
    posicionDelCursor = 0
    valorDeDia = 1
    cantidadSemanas = cantidadSemanasDelMes(mes,ano)
    posicionDelDiaDeLaSemana = monthrange(ano, mes)[0]
    cantidadDiasDelMes = monthrange(ano, mes)[1]     
    a = np.zeros((7, cantidadSemanas))

    for j in range(cantidadSemanas):
        for i in range(7):
            if (posicionDelCursor >= posicionDelDiaDeLaSemana and valorDeDia <= cantidadDiasDelMes):
                a[i,j] = valorDeDia
                valorDeDia += 1
            else:
                a[i,j] = 0
            posicionDelCursor += 1
    return a

matriz = generaMatrizMensual(mes, ano)
#print (cantidadSemanasDelMes(mes, ano))
#print matriz
#imprimePaginaIzq(matriz, mes)
imprimeMesCabeceraDch(5)