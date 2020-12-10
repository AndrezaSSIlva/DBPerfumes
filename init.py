#script para criar o banco de dados e suas tabelas
import sqlite3
path = r"C:\Users\ANDREZA\PycharmProjects\BDPerfumes"
banco = sqlite3.connect(path + r"\BDPerfumes.db")
cursor = banco.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS marcas (id interger AUTO_INCREMENT PRIMARY KEY,nome varchar)" )
cursor.execute("CREATE TABLE IF NOT EXISTS fixacoes (id interger AUTO_INCREMENT PRIMARY KEY, nome vachar)")
cursor.execute("CREATE TABLE IF NOT EXISTS  volumes (id interger AUTO_INCREMENT PRIMARY KEY, nome vachar)")
cursor.execute("CREATE TABLE IF NOT EXISTS essencias (id interger AUTO_INCREMENT PRIMARY KEY, nome vachar)")
cursor.execute("CREATE TABLE IF NOT EXISTS perfurmes (id interger AUTO_INCREMENT PRIMARY KEY , nome vachar, idvolume integer, idmarca interger,idfixacao integer,CONSTRAINT FK_idvolume foreign key (idvolume) REFERENCES volumes (id),CONSTRAINT FK_idmarca foreign key (idmarca) REFERENCES marcas (id), CONSTRAINT FK_idfixacao foreign key (idfixacao) REFERENCES fixacoes (id))")
cursor.execute("CREATE TABLE IF NOT EXISTS essenciaperfume (idessencia integer, idperfurmes integer,CONSTRAINT FK_idessencia foreign key (idessencia) REFERENCES essencias (id), CONSTRAINT FK_idperfumes foreign key (idperfumes) REFERENCES perfumes (id))" )




