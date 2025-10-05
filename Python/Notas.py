division = 30

notas = ["DO","DO#", "RE", "RE#", "MI", "FA", "FA#", "SOL", "SOL#", "LA", "LA#", "SI"]
letras = [chr(i) for i in range(ord("a"), ord("z") + 1)]

palabra = input("Ingrese la palabra para sacar las notas musicales: ").lower()
palabraList = list(palabra)

for i in range(len(palabra)):
  index = letras.index(palabraList[i]) % 12
  
  print(notas[index])