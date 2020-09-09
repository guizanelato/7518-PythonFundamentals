
import psycopg2

DB_NAME = 'pf' # armazenar de forma escondida - ex. variável de ambiente
DB_USER = 'developer'
DB_HOST = 'localhost'
DB_PASSWD = '4linux'

sql_string = 'SELECT * from produto;'

dsn = f"dbname='{DB_NAME}' user='{DB_USER}' host='{DB_HOST}' password='{DB_PASSWD}'"

try:
    conexao = psycopg2.connect(dsn)
except Exception as err:
    print('Erro ao conectar com o banco de dados', err) 

else:
    cursor = conexao.cursor()
    #cursor.execute("INSERT INTO produto VALUES(2, 'brownie', 'um quadrado de chocolate', 5.50, true)")
    cursor.execute(sql_string)

    for registro in cursor.fetchall():
        print(registro)
    
    conexao.commit()
    conexao.close()
