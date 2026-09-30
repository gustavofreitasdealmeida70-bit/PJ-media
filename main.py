#Criação do banco de dados e da tabela
import sqlite3
conexao = sqlite3.connect("alunos.db")
cursor = conexao.cursor()
conexao.commit()
def criar_tabela():
    cursor.execute("""CREATE TABLE IF NOT EXISTS alunos ( id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL,
         nota1 REAL,
         nota2 REAL,
         nota3 REAL,
          media REAL,
            situacao TEXT)""")
    conexao.commit()
#Função para calcular a média e a situação do aluno
def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3
def situacao_aluno(media):
    if media >= 7:
     return "Aprovado"
    elif media >= 5:
      return "Recuperação"
    else:
        return "Reprovado"
def salvar_aluno(nome, nota1, nota2, nota3):
    media = calcular_media(nota1, nota2, nota3)
    situacao = situacao_aluno(media)
    cursor.execute("""INSERT INTO alunos (nome, nota1, nota2, nota3, media, situacao)
        VALUES (?, ?, ?, ?, ?, ?)""", (nome, nota1, nota2, nota3, media, situacao))
    conexao.commit()
    print(f"{nome} salvo com sucesso! Média: {media:.1f} - {situacao}")
#Função para listar os alunos salvos no banco de dados
def listar_alunos():
    cursor.execute("Select nome, media, situacao FROM alunos")
    resultados = cursor.fetchall()
    for aluno in resultados:
        nome, media, situacao = aluno
        print(f"{nome} - Média: {media:.1f} - {situacao}")
#uso das funções
criar_tabela()
salvar_aluno("Amanda", 8, 8, 6)
print("\n--- Lista de alunos ---")
listar_alunos()
conexao.close()
