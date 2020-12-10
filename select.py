# manupulando arquivos do bd
import sqlite3

def titulo(n, s):
    print ( "=" * n )
    print ( f"{s}".center ( n ) )
    print ( "=" * n )


path = r"C:\Users\ANDREZA\PycharmProjects\BDPerfumes"
banco = sqlite3.connect ( path + r"\BDPerfumes.db" )
cursor = banco.cursor ()

cursor.execute("SELECT * FROM essencias")
tabela = cursor.fetchall()
titulo(77,"Tabela")
print("NOME".ljust(20))
for linha in tabela:
    print(str(linha[1]).ljust(17), end="")




