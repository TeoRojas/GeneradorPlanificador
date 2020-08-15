# -*- coding: utf-8 -*-
from funcionesgeneracion import *

ano = 2019
mes = 9

matriz = generaMatrizMensual(mes, ano)

imprimePaginaIzq(matriz, mes)
imprimePaginaDch(matriz, mes)