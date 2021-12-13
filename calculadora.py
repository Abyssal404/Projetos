
def inicio():
    nome = str(input('BEM VINDO A CALCULADORA, PRESSIONE [C] PARA CALCULADORA, [T] PARA TABUADA, [O] PARA SABER SE O NÚMERO É ÍMPAR OU PAR OU [F] PARA CALCULAR FATORIAL: '))
    

    if nome.lower() == 'c':
        calculadora()
    if nome.lower() == 't':
        tabuadaaa()
    if nome.lower() == 'o':
        ImparPar()
    if nome.lower() == 'f':
        fatorial()
    


def calculoimc():
    print("Bem vindo a página 2, mais opções em breve!")
    print("Calcule seu IMC aqui :D")
    peso = (input("Digite seu peso: "))
    altura = (input("Digite sua altura: "))

    if peso.isdigit() or altura.isdigit():
        peso = float(peso)
        altura = float(altura)
    else:
        print("Insira valores válidos!")
        calculoimc()

    imc = peso / altura
    print("Seu IMC é:{0:.2f}".format(imc))




def fatorial():
    n = int(input("Digite o valor: "))
    resultado=1
    for n in range(1,n+1):
        resultado *= n
        print(resultado)


def ImparPar():
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        print("é par!")
    else:
        print("é ímpar!")  


def creditos():
     saas = 'https://www.instagram.com/offstersi/'
     print('MADE BY: {0}'.format(saas))
   



def main():
    print('##############################################################')
    print('USE [**], [*], [-], [+], [/] COMO OPERADORES!')
    inicio()
    maisopc()
    sairr()
    
    
       
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
        calculadora()


    
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

    
def sairr():
    sair = input("Digite [N] para sair, [S] para continuar ou [Y] para ir aos créditos: ")
    if sair.upper() == 'S':
        main()

    if sair.upper() == 'Y':
        creditos()
        main()

def maisopc():
    mais = str(input("Digite [+] para mais opções ou [-] para continuar!!!"))
    if mais == '+':
        calculoimc()
    if mais == '-':
        main()


    
    
    
        
    


if __name__ == "__main__":
    main()
