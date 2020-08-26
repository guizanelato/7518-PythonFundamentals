## Escrever um script em python que some dois números informados pelo usuário
## e apresente o resultado da seguinte forma:
## Números informados: 5 e 4
## resultado esperado: 5 + 4 = 9

### Realizar o Exercício do capítulo 1.


#1: Capturar os números que serão somados
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo  número: '))

#2: Realizar a soma
soma = n1 + n2

#3: Apresentar o resultado de acordo com o formato definido
print(n1, " + ", n2, " = ", soma)

### Saída formatada 

## format 
print("Utilizando Format")
print("{num1} + {num2} = {res} ".format(num1=n1,num2=n2,res=soma))

frase = 'O resultado da soma {} + {} = {}'

print(frase.format(n1,n2,soma))
print('1','2','3', sep=' ')

## f'string 
print('Usando f\'string')
print(f'{n2} + {n1} = {soma}')





