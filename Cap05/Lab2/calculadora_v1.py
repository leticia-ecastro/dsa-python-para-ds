# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")

print("Selecione o número da operação desejada: \n1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão")

opcao = int(input("\nDigite sua opção: "))

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

while opcao not in {1, 2, 3, 4}:
    print("ERRO! Informe apenas uma das opções apresentadas.")
    opcao = int(input("\nDigite sua opção: "))
    
if opcao == 1:
    soma = lambda num1, num2: num1 + num2
    print("Soma:", soma(num1, num2))
elif opcao == 2:
    subtracao = lambda num1, num2: num1 - num2
    print("Subtração:", subtracao(num1, num2))
elif opcao == 3:
    multiplicacao = lambda num1, num2: num1 * num2
    print("Multiplicação:", multiplicacao(num1, num2))
elif opcao == 4:
    divisao = lambda num1, num2: num1 / num2 if num1 != 0 and num2 != 0 else print("ERRO! Não é possível dividir um número por zero!")
    print("Divisão:", divisao(num1, num2))


