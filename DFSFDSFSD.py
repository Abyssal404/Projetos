n = int(input("Digite o valor: "))

if (n % 2) == 0:
    print("Not Weird")

elif (n % 2) >= 2 or (n % 2) >= 5:
    print("Not Weird")

elif (n % 2) >= 6 or (n % 2) >= 20:
    print("Not Weird")

elif (n % 2) > 20:
    print("Not Weird")
else:
    print("Weird")