"""
Módulo de estrategias para el juego del Tateti

Este módulo contiene las estrategias para elegir la acción a realizar.
Los alumnos deben implementar la estrategia minimax.

Por defecto, se incluye una estrategia aleatoria como ejemplo base.
"""

import random
from typing import List, Tuple
from tateti import Tateti, JUGADOR_MAX, JUGADOR_MIN

def estrategia_aleatoria(tateti: Tateti, estado: List[List[str]]) -> Tuple[int, int]:
    """
    Estrategia aleatoria: elige una acción al azar entre las disponibles.
  
    Args:
        tateti: Instancia de la clase Tateti
        estado: Estado actual del tablero
        
    Returns:
        Tuple[int, int]: Acción elegida (fila, columna)

    Raises:
        ValueError: Si no hay acciones disponibles
    """
    acciones_disponibles = tateti.acciones(estado)
    if not acciones_disponibles:
        raise ValueError("No hay acciones disponibles")
    
    return random.choice(acciones_disponibles)

def estrategia_minimax(tateti: Tateti, estado: List[List[str]]) -> Tuple[int, int]:
    """
    Estrategia minimax: elige la mejor acción usando el algoritmo minimax.
    
    Args:
        tateti: Instancia de la clase Tateti
        estado: Estado actual del tablero
        
    Returns:
        Tuple[int, int]: Acción elegida (fila, columna)
    """
    def minimax_max(estado_actual: List[List[str]]) -> float:
        if tateti.test_terminal(estado_actual):
            return tateti.utilidad(estado_actual, JUGADOR_MAX)
        
        valor = float('-inf')
        for accion in tateti.acciones(estado_actual):
            sucesor = tateti.resultado(estado_actual, accion)
            valor = max(valor, minimax_min(sucesor))
        return valor

    def minimax_min(estado_actual: List[List[str]]) -> float:
        if tateti.test_terminal(estado_actual):
            return tateti.utilidad(estado_actual, JUGADOR_MAX)
        
        valor = float('inf')
        for accion in tateti.acciones(estado_actual):
            sucesor = tateti.resultado(estado_actual, accion)
            valor = min(valor, minimax_max(sucesor))
        return valor

    jugador_actual = tateti.jugador(estado)

    if jugador_actual == JUGADOR_MAX:
        sucs = {
            accion: minimax_min(tateti.resultado(estado, accion))
            for accion in tateti.acciones(estado)
        }
        return max(sucs, key=sucs.get)
        
    if jugador_actual == JUGADOR_MIN:
        sucs = {
            accion: minimax_max(tateti.resultado(estado, accion))
            for accion in tateti.acciones(estado)
        }
        return min(sucs, key=sucs.get)

    # raise NotImplementedError(
    #     "\n" + "="*60 +
    #     "\n🚫 ALGORITMO MINIMAX NO IMPLEMENTADO" +
    #     "\n" + "="*60 +
    #     "\n\nPara usar la estrategia Minimax debe implementarla primero." +
    #     "\n\nInstrucciones:" +
    #     "\n1. Abra el archivo 'estrategias.py'" +
    #     "\n2. Busque la función 'estrategia_minimax()'" +
    #     "\n3. Elimine la línea 'raise NotImplementedError(...)'" +
    #     "\n4. Implemente el algoritmo minimax" +
    #     "\n\nMientras tanto, use la 'Estrategia Aleatoria'." +
    #     "\n" + "="*60
    # )
    
