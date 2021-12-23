
palavra = 'batata'
listapalavra = []
LetrasErradas = []
resposta = '******'
erros = 0 


def main():
    global letra
    letra = input("Digite uma letra: ").lower()
    letras_corretas()
    letras_erradas()
    ganhou()
    

    
def letras_corretas():
    global erros
    erros += 1
    global resposta
    if letra in palavra:
        listapalavra.append(letra)
        print(listapalavra)
        for i, c in enumerate(palavra):
            if (c == letra):
                temp = list(resposta)
                temp[i] = letra
                resposta = "".join(temp)
                print(resposta)
    else:
        print("Letra errada, %i erros"%erros)
       



def letras_erradas():
    
    if letra not in palavra:
        LetrasErradas.append(letra)
        print(LetrasErradas)

       
def ganhou():
    if (resposta == palavra):
        print("Parabéns, você acertou!")
        input("Digite [+] para jogar novamente!")
    if input == '+':
        main()

    
   


if __name__ == "__main__":
    while True:
        main()