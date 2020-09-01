#!/usr/bin/python3

"""
Crie um script em python que seja capaz de interagir com arquivos:

    - seja possível ler um arquivo CSV
    - inserir novos registros
    - remover registros
    - alterar registros
    - exibir registros
    - busca por cpf

"""

def buscar_registro():
    cpf = input('Informe o cpf: ')
    
    with open('arquivo.csv') as arquivo:
        conteudo = arquivo.readlines() # como uma lista de strings
        for linha in conteudo:
            if cpf in linha.split(';'):
                registro = linha.split(';') # possível candidato a função\
                print('CPF:', registro[0])
                print('Nome:', registro[1])
                print('Idade:', registro[2])
                print('Sexo:', registro[3])
                print('UF:', registro[4])
                break
        else:
            print('Registro não encontrado')


def remover_registro():
    cpf = input('Informe o cpf a ser deletado: ')
    
    with open('arquivo.csv', 'r') as arquivo:
        conteudo = arquivo.readlines() # como uma lista de strings
        
    for indice in range(len(conteudo)):
        if cpf in conteudo[indice].split(';'):
            registro = conteudo[indice].split(';') # possível candidato a função\
            print('CPF:', registro[0])
            print('Nome:', registro[1])
            print('Idade:', registro[2])
            print('Sexo:', registro[3])
            print('UF:', registro[4])
            
            if input('Deseja realmente excluir o registro?') == 'S':
                del conteudo[indice]
                registro = ';'.join(conteudo) + ';'
                with open('arquivo.csv', 'w') as arquivo:
                    arquivo.write(registro)
                print('Registro removido com sucesso!')
                break
            else:
                print('Cancelado pelo usuário')
                break
    else:
        print('Registro não encontrado')

def inserir_registro():
    #capturar as informações do registro
    #formatar para a saída do arquivo
    #adicionar a string no arquivo
    #salvar arquivo

def alterar_registro():
    pass

def exibir_todos():
    pass

def sair():
    pass



def menu():
    
    while True:
        
        opcoes = {
                '1':buscar_registro,
                '2':remover_registro,
                '3':alterar_registro,
                '4':exibir_todos,
                '5':sair
                }

        escolha = input(f'Informe a opção desejada:\n'
                      f'1- Buscar registro\n'
                      f'2- Remover registro\n'
                      f'3- alterar registro\n'
                      f'4- exibir todos os registros\n'
                      f'5- Sair\n')






