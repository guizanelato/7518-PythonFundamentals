import sqlite3

#1: Estabelece conexão com o banco
conexao = sqlite3.connect('cafe.db')

#2: Crio um cursor para mediar as solicitações
cursor = conexao.cursor()

#3: Instrução em SQL a ser executada no banco
sql_insert = """
INSERT INTO produto(nome, desc, preco, ativo)
VALUES ('{nome}', '{desc}', {preco}, {ativo})

"""

nome_produto = input('Digite o nome do produto: ')
desc_produto = input('Informe a descrição: ')
preco_produto = input('Indique o preço de venda: ')
ativo_produto = input('Produto está a pronta entrega? (1 - Sim, 0- Não): ')


#4: executar instrução no banco
cursor.execute(sql_insert.format(nome = nome_produto,
                                 desc = desc_produto, 
                                 preco = preco_produto,
                                 ativo = ativo_produto))

#5: efetivar as alterações
conexao.commit()

#6: fechar a conexão
conexao.close()


