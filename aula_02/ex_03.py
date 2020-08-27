# Laços, Loops, Repetição ...


## Revisitando Strings

for caractere in 'palavra':
    print(caractere)

for caractere in '4 Linux OpenSoftware Specialists':
    if caractere in 'aeiouAEIOU':
        print(f'{caractere} é uma vogal')

 ## ZIP        


## Laços indefinidos (infinitos)

lista = [0,1,2,3]

for item in lista:
    if item == 4:
        print('Achei o número alvo')
        break
else:
    print('Número não encontrado')

while True:
    print('Digite a opção desejada:')
    print('1 - Mostrar Saldo')
    print('2 - Transferência')
    print('3 - Saque')
    print('4 - Sair')

    if input('') == '4':
        break
else:
    # executo o block

exit()
# for => foreach
### variável de escopo na própria declaração
### sabe quando parar

for num in range(1,10,2): # retorna um intervalo (0,1,2,3,4,5,6,7,9)
    print(num)

#1:

### num = 0
### print(num) 
#### 0

#2:
### num = 1
### print(num)
#### 1


## associação loop <> dados de coleção

tupla = (0,1,3,4,'String')

lista = [0,1,2,3,'String']

for elemento in lista:
    print(elemento)

print()
## com while

indice = 0

while indice < len(lista): 
    print(lista[indice])
    indice += 1


for indice in range(0,len(lista)):
    print(lista[indice])

print('')


for elemento in tupla:
    print(elemento)

print('')

dic = {'nome':'Guilherme', 'cpf':111111-11, 'UF':'SP'}

for chave in dic.keys():
    print(f'campo: {chave}:', dic[chave])
    #if dic[chave] == 'Guilherme':
    #    print('Achei')




exit()
# while
## -> variável de controle 
## -> ritmo | passo 
## -> condição de parada 

variavel_controle = 0

while variavel_controle < 10:
    print(variavel_controle)
    variavel_controle = variavel_controle + 2 # variavel_controle += 1

#1:

### variavel_controle < 10?
### variavel_controle = 0
### 0
### variavel_controle +=1 (variavel_controle=1)

#2:

### variavel_controle < 10? 1 < 10?
### variavel_controle = 1
### 1
### variavel_controle +=1 (variavel_controle=2)

#3:

### variavel_controle < 10?
### variavel_controle = 2
### 2
### variavel_controle +=1 (variavel_controle=2)

#....

#variável_controle < 10 == False.




