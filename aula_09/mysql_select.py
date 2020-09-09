
from os import environ

import pymysql


try:
    conexao = pymysql.connect(
               host = 'localhost',
               user= environ['DB_USER'],
               password = environ['DB_PASSWD'],
               db = 'pf',
               charset = 'utf8mb4',
               cursorclass = pymysql.cursors.DictCursor)

    sql = 'SELECT * from produto;'

    with conexao.cursor() as cursor:
        cursor.execute(sql)
        for registro in cursor:
            print(registro)


except Exception as err:
    print('Erro ao conectar com o Banco de Dados -', err)


else:
    conexao.close()


