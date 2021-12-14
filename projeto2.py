from random import randint
import random



def main():
    valor = random
    valor2 = random.randint(1, 20)
    chutar = int(input("Chute um número de 1 a 20: "))
    if chutar == valor2:
        print("Acertou")
    elif chutar > valor2:
        print("Chutou alto!")
        main()
    elif chutar < valor2:
        print("Chutou baixo!")
        main()




if __name__ == "__main__":
    main()