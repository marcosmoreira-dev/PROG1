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
    existe = bd.get(mat, False)
    if existe == False:
        aluno = {"nome": nome, "curso": curso}
        bd[mat] = aluno
        return True
    else:
        return False
    
novoAluno = adicionar_aluno(bd, 111, "Carlos", "Engenharia")
print(bd)
        