#Multiplicacion de matrices cuadradas 2x2

matrizA= []
matrizB= []
matrizMulti=[]

print("Matriz1")

for i in range(2):
    matrizA.append([])

    for j in range(2):
        valor1= int(input("Ingrese los valores que iran en la matriz:"))
        matrizA[i].append(valor1)

print("="*13)
print("Matriz 2")

for i in range(2):
    matrizB.append([])
    for j in range(2):
        valor2= int(input("Ingrese los valores que iran en la segunda matriz:"))
        matrizB[i].append(valor2)

#Multiplicacion de matrices
for i in range(2):
    matrizMulti.append([])

    for j in range(2):
        multi = 0

        for k in range(2):
            multi = multi + matrizA[i][k] * matrizB[k][j]

        matrizMulti[i].append(multi)

for fila in matrizMulti:
    print(fila)