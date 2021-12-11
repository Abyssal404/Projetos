#nome = "Thallis"
#nome = nome.ljust(1, '@')

#sobrenome = "Fernandes"
#nome = nome.center(20, '#')

#sobrenome2 = "Stersi"
#sobrenome2 = sobrenome2.rjust(10, '$')

#print("{0} {1} {2}".format(nome, sobrenome, sobrenome2))


#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.


nota = int(input("Insira uma nota de 0 a 10: "))

while nota > 10 or nota < 0:
    print("nota inválida, digite novamente!")
    nota = int(input("Insira uma nota de 0 a 10: "))
else:
    print("Valor válido!")



#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

numero = int(input("Taboada de: "))
taboada = 0
for i in range(10):
    taboada += 1
    print(numero * taboada)





numero = int(input("Digite o número: "))
contador = 0

for i in range(numero):
    fatorial = numero - contador
    contador += 1
    print(fatorial2)
















