#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
lightsout.py
------------

Tarea sobre búsquedas, donde lo que es importante es crear nuevas heurísticas

"""
__author__ = 'Jorge Carvajal'


from busquedas import *
import copy
import random


class Lights_out(ProblemaBusqueda):
#----------------------------------------------------------------------------
# Problema 2 (25 puntos): Completa la clase para el problema de lights out
#
#----------------------------------------------------------------------------
    """
    Problema del jueguito "Ligths out".

    La idea del juego es el apagar o prender todas las luces.
    Al seleccionar una casilla, la casilla y sus casillas adjacentes cambian
    (si estan prendidas se apagan y viceversa). El juego consiste en una matriz
    de 5 X 5, cuyo estado puede ser apagado 0 o prendido 1. Por ejemplo el estado

       (0,0,1,0,0,1,1,0,0,1,0,0,1,1,0,1,0,1,0,1,0,0,0,0,0)

    corresponde a:

    ---------------------
    |   |   | X |   |   |
    ---------------------
    | X | X |   |   | X |
    ---------------------
    |   |   | X | X |   |
    ---------------------
    | X |   | X |   | X |
    ---------------------
    |   |   |   |   |   |
    ---------------------
    
    Las acciones posibles son de elegir cambiar una luz y sus casillas adjacentes, por lo que la accion es
    un número entre 0 y 24.

    Para mas información sobre el juego, se puede consultar

    http://en.wikipedia.org/wiki/Lights_Out_(game)

    """
    def __init__(self, pos_inicial):
        # ¡El formato y lo que lleva la inicialización de 
        # la super hay que cambiarlo al problema!
        s0 = pos_inicial
        def meta(estado):
            meta = True
            for i in xrange(25):
                if(estado[i] == 1):
                    meta = False
                    break
            return meta
            #return True if estado[0:23] == estado[1:24] else False
        super(Lights_out, self).__init__(s0, meta)
        #raise NotImplementedError('Hay que hacerlo de tarea')

    def acciones_legales(self, estado):
        return range(25)
        raise NotImplementedError('Hay que hacerlo de tarea')

    def sucesor(self, estado, accion):
        
        sucesor =list(estado)
        sucesor[accion] = 1-sucesor[accion]
        if(accion%5 > 0):
            sucesor[accion-1] = 1-sucesor[accion-1]
        if (accion%5 < 4):
            sucesor[accion+1] = 1-sucesor[accion+1]
        if(accion > 4):
            sucesor[accion-5] = 1-sucesor[accion-5]
        if(accion < 20):
            sucesor[accion+5] = 1-sucesor[accion+5]
        return tuple(sucesor)
        raise NotImplementedError('Hay que hacerlo de tarea')

    def costo_local(self, estado, accion):
        return 1
        raise NotImplementedError('Hay que hacerlo de tarea')

    @staticmethod
    def bonito(estado):
        """
        El prettyprint de un estado dado

        """
        cadena = "---------------------\n"
        for i in range(5):
            for j in range(5):
                if estado[5 * i + j]:
                    cadena += "| X "
                else:
                    cadena += "|   "
            cadena += "|\n---------------------\n"
        return cadena

#-------------------------------------------------------------------------------------------------
# Problema 3 (25 puntos): Desarrolla una política admisible. 
#-------------------------------------------------------------------------------------------------
def h_1(nodo):
    return sum(i for i in nodo.estado)
    
    """
    DOCUMENTA LA HEURÍSTICA QUE DESARROLLES Y DA UNA JUSTIFICACIÓN PLATICADA DE PORQUÉ CREES QUE
    LA HEURÍSTICA ES ADMISIBLE

    Esta heuristica se basa en el numero de luces que hay prendidas en el tablero. NO es admisible
    (Basta con ver que en el caso de tener solo una cruz de luces, h(s) = 5, donde nomas falta 1 movimiento).
    Sin embargo, lo hace en chinga, por eso la meti :D
    """
    return 0

#-------------------------------------------------------------------------------------------------
# Problema 4 (25 puntos): Desarrolla otra política admisible. 
# Analiza y di porque piensas que es (o no es) dominante una respecto otra política
#-------------------------------------------------------------------------------------------------
def h_2(nodo):
    costo = 0
    if nodo.estado[0] == 1:
        costo+=1
    if nodo.estado[4] == 1:
        costo+=1
    if nodo.estado[20] == 1:
        costo+=1
    if nodo.estado[24] == 1:
        costo+=1
    return costo
    """
    DOCUMENTA LA HEURÍSTICA DE DESARROLLES Y DA UNA JUSTIFICACIÓN PLATICADA DE PORQUÉ CREES QUE
    LA HEURÍSTICA ES ADMISIBLE

    Esta heuristica devuelve el numero de luces prendidas en las esquinas. Claramente es admisible 
    cuando el tablero es mayor que 3x3, ya que prender una esquina no afecta a las demas, por lo que 
    siempre sobre-estima, o nos da igual al costo. No es muy buena, pero creo que es un concepto que 
    un jugador podria abarcar al jugar (andar jugando en una seccion del tablero es mejor que en todas).

    """
    return costo

def meta2(estado):
            meta = True
            for i in xrange(25):
                if(estado[i] == 1):
                    meta = False
                    break
            return meta
def prueba_clase():
    """
    Prueba la clase Lights_out
    
    """
    
    pos_ini = (0, 1, 0, 1, 0,
               0, 0, 1, 1, 0,
               0, 0, 0, 1, 1,
               0, 0, 1, 1, 1,
               0, 0, 0, 1, 1)

    pos_a0 =  (1, 0, 0, 1, 0,
               1, 0, 1, 1, 0,
               0, 0, 0, 1, 1,
               0, 0, 1, 1, 1,
               0, 0, 0, 1, 1)

    pos_a4 =  (1, 0, 0, 0, 1,
               1, 0, 1, 1, 1,
               0, 0, 0, 1, 1,
               0, 0, 1, 1, 1,
               0, 0, 0, 1, 1)

    pos_a24 = (1, 0, 0, 0, 1,
               1, 0, 1, 1, 1,
               0, 0, 0, 1, 1,
               0, 0, 1, 1, 0,
               0, 0, 0, 0, 0)

    pos_a15 = (1, 0, 0, 0, 1,
               1, 0, 1, 1, 1,
               1, 0, 0, 1, 1,
               1, 1, 1, 1, 0,
               1, 0, 0, 0, 0)

    pos_a12 = (1, 0, 0, 0, 1,
               1, 0, 0, 1, 1,
               1, 1, 1, 0, 1,
               1, 1, 0, 1, 0,
               1, 0, 0, 0, 0)
    entorno = Lights_out(pos_ini)

    assert entorno.acciones_legales(pos_ini) == range(25)
    assert entorno.sucesor(pos_ini, 0) == pos_a0
    assert entorno.sucesor(pos_a0, 4) == pos_a4
    assert entorno.sucesor(pos_a4, 24) == pos_a24
    assert entorno.sucesor(pos_a24, 15) == pos_a15
    assert entorno.sucesor(pos_a15, 12) == pos_a12
    print "Paso la prueba de la clase"
    

def prueba_busqueda(pos_inicial, metodo, heuristica=None, max_prof=None):
    """
    Prueba un método de búsqueda para el problema del ligths out.

    @param pos_inicial: Una tupla con una posicion inicial
    @param metodo: Un metodo de búsqueda a probar
    @param heuristica: Una función de heurística, por default None si el método de búsqueda no requiere heuristica
    @param max_prof: Máxima profundidad para los algoritmos de DFS y IDS.

    @return nodo: El nodo solución

    """
    if heuristica:
        return metodo(Lights_out(pos_inicial), heuristica)
    elif max_prof:
        return metodo(Lights_out(pos_inicial), max_prof)
    else:
        return metodo(Lights_out(pos_inicial))


def compara_metodos(pos_inicial, heuristica_1, heuristica_2):
    """
    Compara en un cuadro lo nodos expandidos y el costo de la solución de varios métodos de búsqueda

    @param pos_inicial: Una tupla con una posicion inicial
    @param heuristica_1: Una función de heurística
    @param heuristica_2: Una función de heurística

    @return None (no regresa nada, son puros efectos colaterales)

    Si la búsqueda no informada es muy lenta, posiblemente tendras que quitarla de la función
    """
    #n1 = prueba_busqueda(pos_inicial, busqueda_ancho)
    #n2 = prueba_busqueda(pos_inicial, busqueda_profundidad_iterativa)
    #n3 = prueba_busqueda(pos_inicial, busqueda_costo_uniforme)
    n4 = prueba_busqueda(pos_inicial, busqueda_A_estrella, heuristica_1)
    n5 = prueba_busqueda(pos_inicial, busqueda_A_estrella, heuristica_2)

    print '\n\n' + '-' * 50
    print u'Metodo'.center(10) + 'Costo de la solucion'.center(20) + 'Nodos explorados'.center(20)
    print '-' * 50
    #print 'BFS'.center(10) + str(n1.costo).center(20) + str(n1.nodos_visitados)
    #print 'IDS'.center(10) + str(n2.costo).center(20) + str(n2.nodos_visitados)
    #print 'UCS'.center(10) + str(n3.costo).center(20) + str(n3.nodos_visitados)
    print 'A* con h1'.center(10) + str(n4.costo).center(20) + str(n4.nodos_visitados)
    print 'A* con h2'.center(10) + str(n5.costo).center(20) + str(n5.nodos_visitados)
    print ''
    print '-' * 50 + '\n\n'

if __name__ == "__main__":

    print "Antes de hacer otra cosa vamos a verificar medianamente la clase Lights_out"
    prueba_clase()

    # Tres estados iniciales interesantes
    diagonal = (0, 0, 0, 0, 1,
                0, 0, 0, 1, 0,
                0, 0, 1, 0, 0,
                0, 1, 0, 0, 0,
                1, 0, 0, 0, 0)

    simetria = (1, 0, 1, 0, 1,
                1, 0, 1, 0, 1,
                0, 0, 0, 0, 0,
                1, 0, 1, 0, 1,
                1, 0, 1, 0, 1)

    problemin = (0, 1, 0, 1, 0,
                 0, 0, 1, 1, 0,
                 0, 0, 0, 1, 1,
                 0, 0, 1, 1, 1,
                 0, 0, 0, 1, 1)

    print u"\n\nVamos a ver como funcionan las busquedas para un estado inicial"
    print "\n" + Lights_out.bonito(diagonal)
    compara_metodos(diagonal, h_1, h_2)

    print u"\n\nVamos a ver como funcionan las busquedas para un estado inicial"
    print "\n" + Lights_out.bonito(simetria)
    compara_metodos(simetria, h_1, h_2)
    
    print u"\n\nVamos a ver como funcionan las busquedas para un estado inicial"
    print "\n" + Lights_out.bonito(problemin)
    compara_metodos(problemin, h_1, h_2)
    
