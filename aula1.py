#EXERCICIO 1
nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
ano = 2021
imc = peso // altura
calcIdade = ano - idade
print("{0} tem {1} anos, {2} de altura, pesa {3} KG, nasceu em {4} e seu imc é de: {5}".format(nome, idade, altura, peso, calcIdade, imc))

#EXERCICIO 2
nome = str(input("Digite seu nome: "))

import time

while len(nome) <= 3:
    print("Nome inválido, digite novamente!!!!!!!")
    nome = str(input("Digite seu nome: "))
    time.sleep(1)
else:
    print("Belo nome!")


# .isnumeric / .isdigit / .isdecimal  checam se o número digitado é um inteiro ou n

#EXERCICO 3
num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")


if num1.isnumeric() and num2.isnumeric():
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
else:
    print("n vai dar não amigo")


num = input("Digite seu número: ")


if num.isnumeric():
    num = int(num)
    if num % 2 == 0:
        print("é par")
    else:
        print("é impar")
else:
    print("não é inteiro")


#EXERCICIO 4
hora = input("Digite a hora: ")

if hora.isnumeric():
    hora = int(hora)

    if hora < 0 or hora > 23:
        print("N METE O LOUCO N")
    else:
        pass


    if hora <= 11:
        print("Bom dia")
    elif hora >= 12 or hora >= 17:
        print("Boa tarde")
    elif hora >= 18 or hora >= 23:
        print("Boa noite")

#EXERCICIO 5
nome = str(input("Digite seu nome: "))

if len(nome) <= 4:
    print("seu nome é curto!")
elif len(nome) == 5 or nome == 6:
    print("seu nome é normal")
elif len(nome) > 6:
    print("Seu nome é muito grande")









nome = "Thallis"
nome = nome.ljust(10, '#')

sobrenome = "Fernandes"
nome = nome.center()

sobrenome2 = "Stersi"
sobrenome2 = sobrenome2.rjust()









