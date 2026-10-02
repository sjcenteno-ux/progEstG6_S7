matriz = []

for i in range(2):
    matriz.append([])

    for j in range(2):
     valor= int(input("Ingrese el valor:"))
     matriz[i].append(valor)


for fila in matriz:
   print(fila)
