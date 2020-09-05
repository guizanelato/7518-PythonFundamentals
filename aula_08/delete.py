
import sqlite3

#1: Estabelece conexão com o banco
conexao = sqlite3.connect('cafe.db')

#2: Crio um cursor para mediar as solicitações
cursor = conexao.cursor()

#3: Instrução em SQL a ser executada no banco
sql_delete = """
DELETE FROM produto
WHERE nome like '{nome}'

"""

nome_produto = input('Informe o nome do produto a ser removido: ')

#4: executar instrução no banco
cursor.execute(sql_delete.format(nome = nome_produto))
#5: efetivar as alterações
conexao.commit()

#6: fechar a conexão
conexao.close()


