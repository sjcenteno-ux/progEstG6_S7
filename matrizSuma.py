def sumarMatrices():
    #Suma de matrices
 matriz= []
 matriz2= []
 matrizSumada= []

 print("Matriz 1")
 for i in range(3):
     matriz.append([])

     for j in range(3):
      valor= int(input("Ingrese el valor:"))
      matriz[i].append(valor)


 for fila1 in matriz:
   print(fila1)

 print("="*14)
 print("Matriz 2")
 for i in range(3):
   matriz2.append([])
   for j in range(3):
      valor2= int(input("Ingrese los valores de la matriz 2: "))
      matriz2[i].append(valor2)

 for fila2 in matriz2:
   print(fila2)

 #suma de las matrices.
 print("----Resultado de las matrices----")
 for i in range(3):
   matrizSumada.append([])

   for j in range(3):
      suma= matriz[i][j] + matriz2[i][j]
      matrizSumada[i].append(suma)

 for filaSuma in matrizSumada:
    print(filaSuma)   


    



