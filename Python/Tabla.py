division = 30

num = int(input("=" * division + f"\nIngrese el numero a sacar la tabla: "))
mul = int(input("Ingrese hasta que numero llegara la tabla: "))

print(f"\nTabla del {num}:\n" + "=" * division)
for i in range(mul):
  print(f'{num} X {(i+1)} = {num*(i+1)}')
  
print("=" * division)