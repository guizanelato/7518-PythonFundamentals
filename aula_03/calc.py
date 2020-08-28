
"""
Crie um programa em python que peça ao usuário informar dois números, e depois
escolha as seguintes opções:

    1- Soma
    2- Subtração
    3- Divisao
    4- Multiplicação
    5- Sair
    

De acordo com a opção executar a operação com os números informados.

Cada operação deverá ser armazenada em uma função.

"""

def soma(num1, num2):
    """
    Recebe dois números inteiros e retorna a soma entre eles

    """
    return num1+num2

def subtracao(num1, num2):
    """
    Recebe dois números inteiros e retorna a diferença entre eles

    """
    return num1-num2

def multiplicacao(num1, num2):
    """
    Recebe dois números inteiros e retorna a multiplicação entre eles

    """
    return num1*num2

def divisao(num1, num2):
    """
    Recebe dois números inteiros e retorna a divisão entre eles.
    Caso o denominador for zero, será apresetado a seguinte mensagem:
    -'Não Didivirás por Zero'

    """
    if num2 == 0:
        print('Não dividirás por zero')
    else:
        return num1/num2

def sair(num1, num2):
    exit()



#1: capturar dois números
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: ')) 

#2: Apresentar as opções de cálculo

print('Digite a opção desejada')
print('1- Soma\n2- Subtração\n3- Divisão\n4- Multiplicação\n5- Sair')

#3: definir uma forma de _chavear_ as funções a partir da escolha
escolha = input('')

## poderia ser feito com 5 condições utilizando if, elif, else ...

opcoes = {
        '1':soma,
        '2':subtracao,
        '3':divisao,
        '4':multiplicacao,
        '5':sair
        }

if escolha in opcoes.keys():
#3: executar as operações de acordo com a escolha
    print(f'{opcoes[escolha](n1,n2)}')
else:
    print('Opção Inválida')


#4: criar as funcionalidade de soma, sub, div, mult

