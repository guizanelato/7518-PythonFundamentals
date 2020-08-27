


###
### Revisitando Strings
###

"""
Escreva um script em python que conte, na música Faroeste Caboclo:

    - número de vogais
    - número de consoantes
    - Quantas vezes aparece a palavra João
    - Total de caracteres da música
  
Dica: Como a letra da música é muito grande, utilize uma string com aspas tripla:
    letra = '''
       <conteúdo da música>
    '''
        

"""



###
### for
###

"""
Aproveitando o exercício do menu, implemente:

    - A somatória do pedido
"""

###
### While
###

"""
Criem um menu interativo que contenha as seguintes opções:

   - 1: X-Salada (3.50)
   - 2: X-Bacon (4.50)
   - 3: X-Tudo (6.00)
   - 4: Mostrar Pedido
   - 5: Sair

A cada vez que a pessoa escolher algum lanche, ele deverá ser adicionado ao pedido;
Caso o usuário escolher a opção 4, deverá apresentar a lista de itens escolhidos

Ao digitar 5, o programa deve ser encerrado


"""

exit()
#1: criar um menu de apresentação
#2: permitir mais de uma escolha 
#3: poder acumular as escolhas em algum tipo de estrura do python
#4: preciso mostrar todas as escolhas até o momento
#5: preciso encerrar o pedido

pedido = []

while True: #2
    op = input('Informe a opção desejada:\n1- X-Salada(3.50)\n2- X Bacon(4.50)\n3- X-Tudo(6.00)\n4- Mostrar Pedido\n5- Sair\n') #1
    
    #4 - bloco de escolhas
    if op == '1':
        pedido.append(('X-Salada', 3.50))
    elif op == '2':
        pedido.append(('X-Bacon', 4.50))
    elif op == '3':
        pedido.append(('X-Tudo', 6.00)) 
    elif op == '4':
        for item in pedido:
            print(f' Lanche: {item[0]} - Preço: {item[1]}') #4
    elif op == '5': #5
        break
    else:
        print('Opção inválida')








exit()
"""
1) Escreva um programa que receba o ano de nascimento, e que ele retorne à geração
a qual a pessoa pertence. Para definir a qual geração uma pessoa pertence temos a
seguinte tabela:
    
    Geração         Intervalo
    Baby Boomer     Até 1964
    Geração X       1965 - 1979
    Geração Y       1980 - 1994
    Geração Z       1995 - Atual
    

    Para testar se seu script está funcionando, considere os seguintes resultados esperados:
        • ano nascimento = 1988: Geração: Y
        • ano nascimento = 1958: Geração: Baby Boomer
        • ano nascimento = 1996: Geração: Z
"""

#1: pegar a informação de ano

ano = int(input('Informe o ano de nascimento: '))

#2: preciso _comparar_ o ano informado em relação aos intervalos de referência
#3: de acordo com o intervalo, apresentar a mensagem da geração
if ano < 1964:
    print('Baby Boomer')
elif ano < 1979:
    print('Geração X')
elif ano < 1994:
    print('Geração Y')
else:
    print('Geração Z')

