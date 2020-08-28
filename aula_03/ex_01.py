# Funções 

var_global = 1


#1: Funções Nativas - https://docs.python.org/3/library/functions.html

print('isto é uma função nativa da linguagem')

#2: Funções a partir de bibliotecas 
import random

random.randint(0,10)

#3: Funções definidas pelo usuário
def soma(num1, num2):
    num1 = 0
    return num1 + num2 + var_global

print('defino a variavel com valor n1 10')
n1 = 10
print(soma(n1,15))
print(f'Apresento o valor de n1 depois da função: {n1}')


### imutáveis : passagem de dados por valor 

def adiciona_lanche(pedido, lanche):
    pedido.append(lanche)

lista = []
adiciona_lanche(lista, 'X-Bacon')

### mutáveis :  passagem é por referência


## num1 = 1
## num2 = 15

#argumentos: strings, inteiros, booleanos, floats, listas, tuplas, dicionários, função
#retornar valores ou funções...

def func(nome):
    print(f'Olá! Meu nome é {nome}')

# parametros

### parametros com valor padrão

def consolida_carrinho(lista_compras, desconto=1):
    total = 0
    for item in lista_compras:
        total += item
    return total * desconto

lista = [10.3,2.45]

print(consolida_carrinho(lista))
print(consolida_carrinho(lista,0.8))

def soma_multipla(*jujuba):
    print(jujuba, jujuba[0], jujuba[1])
    soma = ''
    for num in jujuba:
        soma += num
    return soma

print(soma_multipla(1,2,3,4))
print(soma_multipla(1,2))
print(soma_multipla(1,4,6,7,2,54.5))

####

def exemplo_kwargs(**kwargs): #keyword arguments
    print(kwargs)


#4: Funções anônimas

anonima = lambda x,y: x+y
anonima(4,5) # 9
