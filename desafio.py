import time

def main():
    
    for numero in range(100):
        time.sleep(1)
        
        if (numero % 3 == 0) and (numero % 5 == 0):
            print("FizzBuzz")
        elif numero % 3 == 0:
            print("Fizz")
        elif numero % 5 == 0:
            print("Buzz")
        else:
            print(numero)

if __name__ == "__main__":
    main()
    
    


