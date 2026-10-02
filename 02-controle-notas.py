nome = input("Digite o nome: ")
nota = float(input(f"Digite a nota de {nome}: "))
quantia = 1
sim_nao = input(f"Você deseja digitar outra nota para {nome}?\n").lower()
soma_notas = nota

while sim_nao == 'sim':
    nova_nota = float(input(f"Digite a nota de {nome}: "))
    soma_notas += nova_nota
    quantia += 1
    nota_final = soma_notas / quantia
    sim_nao = input(f"Você deseja digitar outra nota para {nome}?\n").lower()

if nota_final >= 5:
    situacao = "Aprovado(a)!"
else:
    situacao = "Reprovado(a)."

print(f"Relatório do aluno\nNome:{nome}\nMédia:{nota_final}\nSituação:{situacao}")