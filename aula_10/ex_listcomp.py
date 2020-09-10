# Comprehensions

from random import randint

def retorna_quadrados(num):
    quadrados = []
    for elemento in range(num):
        quadrados.append(elemento**2)
    return quadrados

lista_50_quadrados = retorna_quadrados(50)

mesma_lista = [ num **2 for num in range(50) ] # <- 

aleatorios = [ randint(1,60) for x in range(50)  ]


