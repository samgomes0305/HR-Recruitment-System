class Candidato:
    def __init__(self, nome, nota_entrevista, nota_teste_teórico, nota_teste_prático, nota_soft_skills):
        self.nome = nome
        self.nota_entrevista = nota_entrevista
        self.nota_teste_teórico = nota_teste_teórico
        self.nota_teste_prático = nota_teste_prático
        self.nota_soft_skills = nota_soft_skills

    def atende_critérios(self, nota_minima_entrevista, nota_minima_teste_teórico, nota_minima_teste_prático, nota_minima_soft_skills):
        return (self.nota_entrevista >= nota_minima_entrevista and
                self.nota_teste_teórico >= nota_minima_teste_teórico and
                self.nota_teste_prático >= nota_minima_teste_prático and
                self.nota_soft_skills >= nota_minima_soft_skills)

class ConjuntoCandidatos:
    def __init__(self):
        self.candidatos = []

    def adicionar_candidato(self, candidato):
        self.candidatos.append(candidato)

    def buscar_candidatos_atendendo_critérios(self, nota_minima_entrevista, nota_minima_teste_teórico, nota_minima_teste_prático, nota_minima_soft_skills):
        candidatos_atendendo_critérios = []
        for candidato in self.candidatos:
            if candidato.atende_critérios(nota_minima_entrevista, nota_minima_teste_teórico, nota_minima_teste_prático, nota_minima_soft_skills):
                candidatos_atendendo_critérios.append(candidato.nome)
        return candidatos_atendendo_critérios


conjunto_candidatos = ConjuntoCandidatos()


conjunto_candidatos.adicionar_candidato(Candidato("Tite", 4, 5, 6, 7))
conjunto_candidatos.adicionar_candidato(Candidato("Arrascaeta", 3, 6, 8, 8))
conjunto_candidatos.adicionar_candidato(Candidato("Bruno Henrique", 5, 4, 7, 6))
conjunto_candidatos.adicionar_candidato(Candidato("Gabigol", 4, 4, 8, 9))
conjunto_candidatos.adicionar_candidato(Candidato("Pedro", 3, 4, 5, 7))


nota_minima_entrevista = int(input("Nota mínima em entrevista: "))
nota_minima_teste_teórico = int(input("Nota mínima em teste teórico: "))
nota_minima_teste_prático = int(input("Nota mínima em teste prático: "))
nota_minima_soft_skills = int(input("Nota mínima em avaliação de soft skills: "))


candidatos_encontrados = conjunto_candidatos.buscar_candidatos_atendendo_critérios(nota_minima_entrevista, nota_minima_teste_teórico, nota_minima_teste_prático, nota_minima_soft_skills)

if candidatos_encontrados:
    print(f"Candidatos atendendo aos critérios: {candidatos_encontrados}")
else:
    print("Nenhum candidato atende aos critérios especificados.")


