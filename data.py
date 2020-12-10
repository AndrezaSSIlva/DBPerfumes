# script inserindo dados ao banco BDPerfumes
import sqlite3
path = r"C:\Users\ANDREZA\PycharmProjects\BDPerfumes"
banco = sqlite3.connect(path + r"\BDPerfumes.db")
cursor = banco.cursor()


cursor.execute ( "INSERT INTO volumes (nome) VALUES ('vinte') ")
cursor.execute ( "INSERT INTO volumes (nome) VALUES ('cinquenta')" )
cursor.execute ( "INSERT INTO volumes (nome) VALUES ('cem')" )
cursor.execute ( "INSERT INTO volumes (nome) VALUES ('duzentos')" )

cursor.execute ( "INSERT INTO essencias (nome) VALUES ('morango')" )
cursor.execute ( "INSERT INTO essencias (nome) VALUES ('amora')" )
cursor.execute ( "INSERT INTO essencias (nome) VALUES ('cabela')" )
cursor.execute ( "INSERT INTO essencias (nome) VALUES ('jasmin')" )

cursor.execute ( "INSERT INTO marcas (nome) VALUES ('boticario')" )
cursor.execute ( "INSERT INTO marcas (nome) VALUES ('calvin klein')" )
cursor.execute ( "INSERT INTO marcas (nome) VALUES ('natura')" )
cursor.execute ( "INSERT INTO marcas (nome) VALUES ('avon')" )

cursor.execute ( "INSERT INTO fixacoes (nome) VALUES ('perfume 20%')" )
cursor.execute ( "INSERT INTO fixacoes (nome) VALUES ('perfum 17%')" )
cursor.execute ( "INSERT INTO fixacoes (nome) VALUES ('eua fraiche 8%')" )
cursor.execute ( "INSERT INTO fixacoes (nome) VALUES ('eua cologne 7%')" )


print("registro(s) inserido(s) com sucesso.")



print("conexao finalizada")
banco.commit()
