
def inicio():
    nome = str(input('BEM VINDO A CALCULADORA BOLADA, PRESSIONE [C] PARA CALCULADORA OU [T] PARA TABUADA: '))
    if nome.lower() == 'c':
        calculadora()
    if nome.lower() == 't':
        tabuadaaa()



def main():
    print('##############################################################')
    print('MADE BY @offstersi')
    print('USE [**], [*], [-], [+], [/] COMO OPERADORES!')
    inicio()
    sair()
    


       
def tabuadaaa():
    tabuada = 0
    numero = int(input("Insira o número: "))
    for i in range(10):
        tabuada += 1
        print(numero * tabuada)
        
    

def calculadora():
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
    if sair.upper() == 'S':
        main()
        

if __name__ == "__main__":
    main()
