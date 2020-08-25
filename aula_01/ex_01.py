#!/usr/bin/python3 

## shebang! <- shell bang
# isto é um comentário 


jujuba = 10 # inteiros
taxa_juros = 3.50 # flutuantes  
alfanumerico = "10" # string <> texto

## Operadores Aritméticos 

num1 = 5.50
num2 = 4.85

### Operações

## Soma
soma = num1 + num2 

## Subtração
sub = num1 - num2 

## Multiplicação
multi = num1 * num2

## Divisão
div = (num1 + num1) / num2

## Chão (floor) 

res = 5 // 2 # 2

## Resto 
resto = 5 % 2 # 1

## Exponenciação 
exp = 2 ** 2 ** 3 # Ordem de resolução da direita pra esquerda 

### PCAP 


### Booleanos 

estou_ao_vivo = True 
aula_terminou = False

## Operadores de Comparação

## > < == != <= >= 

## 0 < x < 5

### Operadores lógicos 

## or -> "maleável"

x = 5

print(x > 2 or x > 10) # Basta apenas uma setença verdadeira para retornar True

## and -> restritivo

print(x > 2 and x > 10) # Ambas as sentenças precisam ser verdadeiras para retornar TRUE 

## False

print(not x > 2) # Inverte a relação booleana - se é falso torna-se verdadeiro e vice versa.


#### Strings 

frase = '4Linux Open Software Specialists'

mesma_coisa = "4Linux Open Software \\n Specialists"

print(frase == mesma_coisa) 

#####


print('texto', frase sep='_') 









