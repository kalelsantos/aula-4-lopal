nome_digitado = input("Digite o nome: ")
senha_digitada = input("Digite a senha: ")
senha_cadastrada = "0502"
nome_cadastrado = "Rebecca"

cor_rebecca = "\033[38;2;102;51;153m"
cor_vermelha = "\033[31m"
reset = "\033[0m"


while senha_digitada != senha_cadastrada or nome_cadastrado != nome_digitado:
    print(f"{cor_vermelha}Senha incorreta ou nomes incorretos, tente novamente. {reset}")
    nome_digitado = input("Digite o nome: ")
    senha_digitada = input("Digite a senha: ")


print(f"{cor_rebecca}Bem-vindo(a) ao sistema, {nome_cadastrado}! {reset}")