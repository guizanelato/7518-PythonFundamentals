
import sqlite3

#1: Estabelece conexão com o banco
conexao = sqlite3.connect('cafe.db')

#2: Crio um cursor para mediar as solicitações
cursor = conexao.cursor()

#3: Instrução em SQL a ser executada no banco
sql_update = """
UPDATE produto
SET preco = {preco}
WHERE id = {id}

"""

preco_produto = input('Digite o valor a ser alterado: ')
id_produto = input('Informe o código do produto a ser alterado: ')


#4: executar instrução no banco
resultado = cursor.execute(sql_update.format(preco=preco_produto, id=id_produto))

conexao.commit()

#6: fechar a conexão
conexao.close()




