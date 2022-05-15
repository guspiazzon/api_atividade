from models import Pessoas

#Insere dados na tabela Pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Tatavo',idade= 27)
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


if __name__ == '__main__':
     # insere_pessoas()
     # altera_pessoas()
     exclui_pessoas()
     consulta_pessoas()

