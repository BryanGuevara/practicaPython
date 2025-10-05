division = 30

opcion = 1
cantidad = 0
nota = 0

print("="*division)
while opcion != 0:
  cantidad = cantidad + 1
  nota = nota + int(input(f"Ingrese la nota {cantidad}: "))
  opcion = int(input(f"¿Desea añadir otra nota? (1:Si| 0:No): "))
  
print(f"{cantidad} notas añadidas, su promedio es: {nota//cantidad}")
print("="*division)