coisaboba = print('##############################################################')
made = print('MADE BY @offstersi')
nome2 = print('USE [**], [*], [-], [+], [/] COMO OPERADORES!')
nome = str(input('BEM VINDO A CALCULADORA BOLADA, PRESSIONE [C] PARA CALCULADORA OU [T] PARA TABUADA: '))
tabuada = 0



while True:

    if nome.lower() == 't':
        numero = int(input("Insira o número: "))
        for i in range(10):
            tabuada += 1
            print(numero * tabuada)


    if nome.lower() == 'c':
        num1 = (input("Digite o primeiro número: "))
        num2 = (input("Digite o segundo número: "))
        operador = (input("Digite o operador: "))


        if num1.isdigit() or num2.isdigit():
            num1 = int(num1)
            num2 = int(num2)
        else:
            print("Digite um número!!!!")

        #A = ['+': +, '-': -]
       
        if operador == '+':
            print(num1 + num2)
        elif operador == '-':
            print(num1 - num2)
        elif operador == '/':
            print(num1 / num2)
        elif operador == '*':
            print(num1 * num2)
        elif operador == '**':
            print(num1 ** num2)
        else:
            print("Insira um operador válido.")


    sair = input("Digite [N] para sair ou [S] para continuar")

    if sair.lower() == 's':
        nome = str(input('PRESSIONE [C] PARA CALCULADORA OU [T] PARA TABUADA: '))
    else:
        break







