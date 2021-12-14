from random import randint
import random


def main():

    dado = str(input("Você gostaria de jogar o dado? "))
    
    if dado == 'sim':
        jogardado()
    if dado == 'não':
        print("Então tá.")
        main()


def jogardado():
    a = random
    b = random.randint(1, 6)
    print(b)




















if __name__ == '__main__':
    main()

