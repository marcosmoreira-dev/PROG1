# 3) Crie dois conjuntos: alunos_segunda e alunos_quarta, contendo nomes de alunos que compareceram a essas aulas. Exiba:
# ● Os alunos que vieram em ambos os dias.
# ● Os alunos que vieram apenas na segunda.
# ● A lista completa de alunos distintos que assistiram a pelo menos uma aula.

alunos_segunda = {"Marcos","Claudia","Lucas"}
alunos_quarta = {"José","Claudia","João"}

print(f"{alunos_segunda & alunos_quarta}")
print(f"{alunos_segunda - alunos_quarta}")
print(f"{alunos_segunda | alunos_quarta}")