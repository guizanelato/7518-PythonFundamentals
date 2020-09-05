import sqlite3

try:
#1: conectar-se com o banco de dados
    conexao = sqlite3.connect('cafe.db')

#2: cursor - intermediário entre o lado do python e do bd. 
    cursor = conexao.cursor()

#3: instrução para ser executada no banco
    sql = """
    CREATE TABLE produto (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(50),
        desc VARCHAR(200),
        preco REAL,
        ativo BOOLEAN
    );
    """
#4: executar a instrução no banco
        cursor.execute(sql)

except sqlite3.OperationalError as err:
    print('Tabela já existente -', err)
except sqlite.Error as err:
    print('Erro Desconhecido - ', err)
else:
#5: efetivar a alteração
    conexao.commit()

#6: encerrar a conexão
    conexao.close()


