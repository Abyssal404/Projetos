coisaboba = print('##############################################################')
made = print('MADE BY @offstersi')
nome2 = print('USE [**], [*], [-], [+], [/] COMO OPERADORES!')
nome = str(input('BEM VINDO A CALCULADORA BOLADA, PRESSIONE [C] PARA CALCULADORA OU [T] PARA TABUADA: '))




def main():
    if nome.lower == 'c':
        return(calculadora.__name__)
    if nome.lower == 't':
        return(tabuadaaa.__name__)


       
def tabuadaaa():
    if nome.lower() == 't':
        tabuada = 0
        numero = int(input("Insira o número: "))
        for i in range(10):
            tabuada += 1
            print(numero * tabuada)
        
    

def calculadora():
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

    
def sair():
    sair = input("Digite [N] para sair ou [S] para continuar")
    if sair.lower() == 'S':
        return(nome)
        
