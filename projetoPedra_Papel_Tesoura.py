from random import choice, random


def main():
    a = input("Bem vindo ao pedra, papel, tesoura. Deseja jogar? ")
    if a.lower() == 'sim':
        jogador1()
        jogador2()
        ganhou_perdeu()
    
        


def jogador1():
    print("UTILIZE [PEDRA], [PAPEL] OU [TESOURA]")
    global jogada 
    jogada = str(input("faça sua jogada: "))

    if jogada.lower() == 'pedra':
        print("Você escolheu Pedra!")
    elif jogada.lower() == 'tesoura':
        print("Você escolheu Tesoura!")
    elif jogada.lower() == 'papel':
        print("Você escolheu Papel!")
    else:
        print("Digite um valor válido")
    


def jogador2(): #AQUI É SÓ UM BOT
    global chute
    nomes = ['Pedra!', 'Papel!', 'Tesoura!']
    chute = choice(nomes)

    print("O bot escolheu: {0}".format(chute))



def ganhou_perdeu():
    if jogada == 'papel' and chute == 'Pedra!':
        print("Você Ganhou!")
    elif jogada == 'pedra' and chute == 'Papel!':
        print('Você perdeu!')
    elif jogada == 'tesoura' and chute == 'Pedra!':
        print("Você perdeu!")
    elif jogada == 'pedra' and chute == 'Tesoura!':
        print("Você ganhou!")
    elif jogada == 'papel' and chute == 'Tesoura!':
        print("Você perdeu!")
    elif jogada == 'tesoura' and chute == 'Papel!':
        print("Você ganhou!")
    else:
        print("Empate!")
    
    


    






if __name__ == "__main__":
    main()