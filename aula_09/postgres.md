#0: verifica se o postgres está no repositório da sua distro
sudo apt search postgresql 

#1: se existir no repositório , instale
sudo apt install postgresql 

#2: verifica o serviço
systemctl status postgresql

#3: acessa o psql através do usuário de sistema
su - postgres
psql 

#4: adicionar um usuário de serviço
CREATE USER developer IDENTIFIED by '4linux';

#5: cria um banco de dados pf
CREATE DATABASE pf;

#6: adiciona as permissões do usuário developer no banco pf
GRANT ALL PRIVILEGES ON DATABASE pf to developer


#7: Instalar o driver de conexão psycopg2

#7.1  instalar o libpq-dev
sudo apt install libpq-dev

# instalar o psycopg2 
pip install psycopg2
