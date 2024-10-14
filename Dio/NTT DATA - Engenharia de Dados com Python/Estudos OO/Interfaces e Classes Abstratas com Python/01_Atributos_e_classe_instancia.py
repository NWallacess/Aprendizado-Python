class Estudante:
    escola = "Dio"

    def __init__(self,nome,matricula):
        self.nome = nome
        self.matricula = matricula
        
    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
def Mostra_alunos(*objs):
    for obj in objs:
        print(obj)

aluno1 = Estudante("Guilherme",1)
aluno2 = Estudante('Maria',2)

Mostra_alunos(aluno1,aluno2)
aluno1.matricula  = 3
aluno3 = Estudante("Everton",4)
Estudante.escola = "Python"
Mostra_alunos(aluno1,aluno2)

