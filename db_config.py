import mysql.connector
from mysql.connector import errorcode

print("Conectando...")
try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='753129senha'
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Existe algo errado no nome de usuário ou senha')
    else:
        print(err)

cursor = conn.cursor()

# Criando banco de dados do consumidor
cursor.execute("DROP DATABASE IF EXISTS `consumidor`;")
cursor.execute("CREATE DATABASE `organic_food`;")
cursor.execute("USE `organic_food`;")

# Criando tabelas
TABLES = {}
TABLES['Consumidor'] = ('''
      CREATE TABLE `consumidor` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `nome` varchar(50) NOT NULL,
      `CPF` varchar(15) NOT NULL,
      `Endereco` varchar(60) NOT NULL,
      `usuario` varchar(20) NOT NULL,
      `senha` varchar(20) NOT NULL,
      `email` varchar(25) NOT NULL,
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Produtor'] = ('''
      CREATE TABLE `produtor` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `razao` varchar(50) NOT NULL,
      `CNPJ` varchar(20) NOT NULL,
      `endereco` varchar(60) NOT NULL,
      `site` varchar(20),
      `usuario` varchar(20) NOT NULL,
      `senha` varchar(20) NOT NULL,
      `email` varchar(25) NOT NULL,
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')


for tabela_nome in TABLES:
    tabela_sql = TABLES[tabela_nome]
    try:
        print('Criando tabela {}:'.format(tabela_nome), end=' ')
        cursor.execute(tabela_sql)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print('Já existe')
        else:
            print(err.msg)
    else:
        print('OK')
