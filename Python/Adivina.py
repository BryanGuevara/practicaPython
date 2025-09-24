import random

limit = 100
numRan = random.randint(1,limit)
numPlayer = -1
intentos = 0

numPlayer = int(input(f"Estoy pendando en un numero entre el 1 y el {limit}: "))

while numRan != numPlayer:
  if numRan > numPlayer:
    numPlayer = int(input("El numero en el que pienso es mas alto, intenta de nuevo: "))
  else:
    numPlayer = int(input("El numero en el que pienso es mas bajo, intenta de nuevo: "))
  
  intentos = intentos + 1 
  
  
print(f"¡Felicidades! era el {numRan}\nNumero de intentos: {intentos}")