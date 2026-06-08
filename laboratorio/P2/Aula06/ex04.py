# Crie um pequeno "banco de dados" de alunos usando um dicionário aninhado. A chave principal será a matrícula do aluno (um inteiro), e o valor será outro dicionário contendo as informações ("nome" e "curso").
# Crie uma função adicionar_aluno que recebe o BD, matrícula, nome e curso e adiciona um novo aluno ao BD. A função deve verificar se a matrícula já existe antes de adicionar. Se existir, deve retornar False. Se for adicionado, deve retornar True.
# Crie uma função buscar_nome_curso que recebe o BD e a matrícula. A função deve retornar o nome do aluno e o curso dele, usando uma tupla (nome, curso). Se a matrícula não for encontrada, deve retornar (None, None).

bd = {
    123: {
        "nome": "José",
        "curso": "Sistemas de Informação",
    },

    456: {
        "nome": "Maria",
        "curso": "Ciência da Computação",
    },
}

def adicionar_aluno(bd, mat, nome, curso):
    # Verifica se a matrícula já está cadastrada
    existe = bd.get(mat, False) # Procura a chave mat dentro de bd, se encontrar retorna a matrícula, se não encontrar, retorna False.

    # Se a matrícula não existir, cadastra aluno
    if existe == False:
        aluno = {"nome": nome, "curso": curso} # cria um dicionário aluno
        bd[mat] = aluno # adiciona item no dicionário
        return True
    # Caso exista, não cadastra
    else:
        return False

def buscar_nome_curso(bd, mat):
    existe = bd.get(mat, False)

    # Se a matrícula exisitr
    if existe: 
        return (bd[mat]["nome"], bd[mat]["curso"]) # Tupla contendo nome e curso
    else: # Se a matrícula não existir
        return (None, None)

def buscar_nome_curso2(bd, mat):
    # Procura a matrícula 'mat' no dicionário 'bd'.
    # Se encontrar, retorna o dicionário com os dados do aluno.
    # Se não encontrar, retorna None.
    aluno = bd.get(mat)

    # Verifica se a variável 'aluno' contém algum valor.
    # Se a matrícula foi encontrada, 'aluno' será um dicionário e a condição será verdadeira.
    if aluno: # é igual a if aluno != none
        # aluno["nome"] acessa o valor associado à chave "nome".
        # aluno["curso"] acessa o valor associado à chave "curso".
        return (aluno["nome"], aluno["curso"])
    
    return (None, None)

def buscar_nome_curso(bd, mat):
    aluno = bd.get(mat, None)
    if aluno == None:
        return (None, None)
    else:
        nome = aluno['nome']
        curso = aluno['curso']
        return (nome, curso)

    
    
novoAluno = adicionar_aluno(bd, 111, "Carlos", "Engenharia")
print(bd)
        