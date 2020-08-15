# -*- coding: utf-8 -*-
import calendar
from calendar import monthrange
import sys
import numpy as np
from funcionesImpresion import *
import math


def cantidadSemanasDelMes(mes, ano):
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