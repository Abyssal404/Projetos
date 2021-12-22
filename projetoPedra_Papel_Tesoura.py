from random import choice, random

jogadas = ['PEDRA', 'PAPEL', 'TESOURA']
ganha = 'Você ganhou!'
jogadawin = [['PAPEL', 'PEDRA'], ['PEDRA', 'TESOURA'], ['TESOURA', 'PAPEL']]
vitorias = 0

def main():
    a = input("Bem vindo ao pedra, papel, tesoura. Deseja jogar? ")
    if a.lower() == 'sim':
        jogadap1 = jogador1()
        chutebot = jogador2()
        ganhou_perdeu(jogadap1, chutebot)
    else:
        print(":(")
    
        

def jogador1():
    print("UTILIZE [PEDRA], [PAPEL] OU [TESOURA]")
    jogada = str(input("faça sua jogada: ")).lower()
    if jogada.upper() in jogadas:
        print("Você escolheu: {0}!".format(jogada))
        return jogada
    else:
        print("Digite um valor válido")
    


def jogador2(): #AQUI É SÓ UM BOT
    chute = choice(jogadas).lower()
    print("O bot escolheu: {0}".format(chute))
    return chute



def ganhou_perdeu(jogadap1, chutebot):
    global vitorias
    vitorias += 1
    
    if([jogadap1.upper(), chutebot.upper()] in jogadawin):
        print(ganha)
        print("%i Pontos"%vitorias)
    elif(jogadap1.upper() == chutebot.upper()):
        print("Empate!")
    else:
        print("Você Perdeu!")
    
    main()
    
    
    
    







if __name__ == "__main__":
    main()