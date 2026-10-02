cor_rebecca = "\033[38;2;102;51;153m"
cor_vermelha = "\033[31m"
reset = "\033[0m"

def somar():
    numero1 = float(input("Digite o primeiro número que deseja somar: "))
    numero2 = float(input("Digite o segundo número que deseja somar: "))
    resultado = numero1 + numero2
    print(f"Conta: {cor_rebecca}{numero1} + {numero2} = {resultado}{reset}")

def subtrair():
    numero1 = float(input("Digite o primeiro número que deseja subtrair: "))
    numero2 = float(input("Digite o segundo número que deseja subtrair: "))
    resultado = numero1 - numero2
    print(f"Conta: {cor_rebecca}{numero1} - {numero2} = {resultado}{reset}")

def multiplicar():
    numero1 = float(input("Digite o primeiro número que deseja multiplicar: "))
    numero2 = float(input("Digite o segundo número que deseja multiplicar: "))
    resultado = numero1 * numero2
    print(f"Conta: {cor_rebecca}{numero1} x {numero2} = {resultado}{reset}")

def dividir():
    numero1 = float(input("Digite o primeiro número que deseja dividir: "))
    numero2 = float(input("Digite o segundo número que deseja dividir: "))
    resultado = numero1 / numero2
    print(f"Conta: {cor_rebecca}{numero1} / {numero2} = {resultado}{reset}")

def par():
    quantidade = int(input("Quantos números você quer ver?\n"))
    contador = 0
    numero = 1
    while contador < quantidade:
        if numero % 2 == 0:
            print(numero)
            contador += 1
        numero+=1

def impar():
    quantidade = int(input("Quantos números você quer ver?\n"))
    contador = 0
    numero = 1
    while contador < quantidade:
        if numero % 2 != 0:
            print(numero)
            contador += 1
        numero+=1

def somatorio():
    limite = int(input("Digite um número: "))
    contador = 1
    soma = 0
    while contador <= limite:
        soma += contador
        contador = contador +1
    print(soma)


def fatorial():
    limite = int(input("Digite um número"))
    contador = 1
    fatorial = 1
    while contador <= limite:
        fatorial *= contador
        contador = contador +1
    print(fatorial)


while True:
    print(f"-------------\n {cor_rebecca}CALCULADORA{reset}\n-------------\n{cor_rebecca}1. Adição\n2. Subtracão\n3. Multiplicacão\n4. Divisão\n5. Pares\n6. Ímpares\n7. Somatório\n8. Fatorial\n{cor_vermelha}0. Sair\n{reset}")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        somar()
    elif opcao == '2':
        subtrair()
    elif opcao == '3':
        multiplicar()
    elif opcao == '4':
        dividir()
    elif opcao == '5':
        par()
    elif opcao == '6':
        impar()
    elif opcao == '7':
        somatorio()
    elif opcao == '8':
        fatorial()
    elif opcao == '0':
        print(f"{cor_vermelha}Saindo . . .{reset}")
        break
    else:
        print(f"{cor_vermelha}Opção Inválida. Tente novamente.{reset}")