from models import Pessoas, Usuarios

#Insere dados na tabela Pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Tatavo',idade= 27)
    print(pessoa)
    pessoa.save()
    pessoa = Pessoas(nome='Marciano', idade=20)
    print(pessoa)
    pessoa.save()

#Realiza consulta na  tabela Pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome = 'Gustavo').first()
    print(pessoa.idade)

#Altera dados na tabela Pessoa
def altera_pessoas():
    pessoa = Pessoas.query.filter_by(nome= 'Damelão').first()
    pessoa.nome = 'Dameli'
    pessoa.save()

#Exclui dados na tabela Pessoa
def exclui_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Dameli').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
     insere_usuario('Gustavo', '123459')
     insere_usuario('Tatavo' , '102045')
     consulta_todos_usuarios()
     # insere_pessoas()
     # altera_pessoas()
     # exclui_pessoas()
     # consulta_pessoas()

