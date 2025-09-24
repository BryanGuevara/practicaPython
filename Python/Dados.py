import random

division = 30

dados = int(input("=" * division + f"\nCuntos dados desea lanzar: "))
caras = int(input("Cuantas caras tienen los dados: "))
total = 0;

print("=" * division + f"\nTirada minima: {dados}\nTirada maxima: {dados*caras}\n" + "=" * division)

for i in range(dados):
  tirada = random.randrange(1,caras)
  total = total + tirada
  print(f"Dado {i + 1}: {tirada}")

print("=" * division + f"\nTirada {dados}D{caras}: {total}\n" + "=" * division)