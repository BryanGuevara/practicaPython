num = int(input("Ingrese el numero a sacar la tabla: "))
mul = int(input("Ingrese hasta que numero llegara la tabla: "))

print(f"\nTabla del {num}:\n" + "="*20)
for i in range(mul):
  print(f'{num} X {(i+1)} = {num*(i+1)}')