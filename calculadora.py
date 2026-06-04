def somar (a, b):
    return a + b
def subtrair (a, b):
    return a - b
def multiplicar (a, b):
    return a * b
def dividir (a, b):
    if b == 0:
        return "Não é possível dividir por zero."
    else:
        return a / b
def sair ():
    print("Saindo da calculadora.")
def calculadora ():
    while True:
        print("Escolha a operação:")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Sair")

        escolha = input("Digite sua escolha (1/2/3/4/5): ")

        if escolha == '5':
            sair()
            break

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print(f"O resultado da soma é: {somar(num1, num2)}")
        elif escolha == '2':
            print(f"O resultado da subtração é: {subtrair(num1, num2)}")
        elif escolha == '3':
            print(f"O resultado da multiplicação é: {multiplicar(num1, num2)}")
        elif escolha == '4':
            print(f"O resultado da divisão é: {dividir(num1, num2)}")
        else:
            print("Opção inválida. Por favor, tente novamente.")
calculadora()