# !/usr/bin/python3         # Parte I
# -*- coding: utf-8 -*-     # Parte II


# Parte III

"""Programa con funciones básicas aritméticas"""

# Variables del módulo

__author__ = "Cuauhtémoc"  # Parte IV
__version__ = "1.0"
__status__ = "Development"

# Parte V

import math

# Parte VI

VALOR_PI = round(math.pi, 7)

def suma_dos_numeros(x, y):
	"""Calcula la suma de dos números"""
	return x + y


def resta_dos_numeros(x, y):
	"""Calcula la resta de dos números"""
	return x - y


# Parte VII

if __name__ == "__main__":
  print('Suma de dos números')
  x = int(input("Ingresa el primer número: "))
  y = int(input("Ingresa el segundo número: "))
  resultado = suma_dos_numeros(x, y)
  print(f"La suma de el número {x} + {y} = {resultado}")
  print('Cálculo finalizado')
