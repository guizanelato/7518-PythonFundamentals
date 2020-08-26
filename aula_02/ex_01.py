# Estruturas de Decisão

## Crie um script em python que retorne o seu IMC

## IMC = (PESO / ALTURA) ** 2

### IMC < 18.5 - Magreza
### 18.5 < IMC 24.9 - Normal
### 25 < IMC < 29.9 - Sobrepeso
### 30 < IMC < 39.9 - Obesidade
### IMC > 40 - Obesidade Grave

#1: capturar os dados de peso e altura

peso = float(input('Informe o seu peso: '))
altura = float(input('Informe a sua altura: '))

#2: calcular o IMC com a seguinte fórmula: (peso / altura) ** 2

imc = peso/altura ** 2

#3: classificar o imc de acordo com a tabela de referência

if imc < 18.5:
    print(f' Peso: {peso} - Altura: {altura} - IMC: {imc} - Classificação: Magreza')
elif imc < 24.9:
    print(f' Peso: {peso} - Altura: {altura} - IMC: {imc} - Classificação: Normal')
elif imc < 29.9:
    print(f' Peso: {peso:.2f} - Altura: {altura:02.2f} - IMC: {imc:.2f} - Classificação: Sobrepeso')
elif imc < 39.9:
    print(f' Peso: {peso} - Altura: {altura} - IMC: {imc} - Classificação: Obesidade')
else:
    print(f' Peso: {peso} - Altura: {altura} - IMC: {imc} - Classificação: Obesidade Grave')
   # print('Peso: '+ peso +' - Altura: '+ altura ...)
   # print('Peso : {var:.2f}'.format(var= peso) 

    



exit()
## and/ or/ not

##  Validar se uma pessoa pode dirigir
### ter idade acima de 17 
### precisar ter habilitação

#1: Capturar a idade
idade = int(input('Informe a sua idade: '))

#2: Capturar se a pessoa possui habilitação
hab = False

if input('Possui Habilitação? / (S/N): ').upper() == 'S':
    hab = True

#3: validar se a pessoa tem:
## idade maior do que 17
## possui habilitação

if idade > 17 and hab: #hab == True
    print("Pode dirigir")
else:
    print("Não pode dirigir")


exit()
### decisão simples / múltipla


idade = int(input('Informe sua idade : '))

if idade <= 18:
    if input('Possui acompanhante maior de idade?') == 'N':
            print('Não pode Entrar')
else:
    print('Pode entrar')



