
import sqlite3

#1: Estabelece conexão com o banco
conexao = sqlite3.connect('cafe.db')

#2: Crio um cursor para mediar as solicitações
cursor = conexao.cursor()

#3: Instrução em SQL a ser executada no banco
sql_select = """
SELECT nome, preco FROM produto

"""

#4: executar instrução no banco
resultado = cursor.execute(sql_select)

#--: efetivar as alterações não são necessárias quando as instruções são de consulta

#5: Verificar o retorno dos dados
for registro in resultado.fetchall():
    print('----------------------------------------')
    print('Nome:', registro[0])
    print('Preço:', registro[1])

#6: fechar a conexão
conexao.close()




