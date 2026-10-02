def convertirIdentidad():
    matrizA= []
    matrizIden= []

    print("Matriz original.")

    for i in range(2):
         matrizA.append([])

         for j in range(2):
            valor1= int(input("Ingrese los valores que iran en la matriz original:"))
            matrizA[i].append(valor1)
    print("Matriz ingresada:")

    for fila in matrizA:
        print(fila)

    #convertir esta matriz a identidad 

    for i in range(2):
        matrizIden.append([])

        for j in range(2):

            if i ==j:
                matrizIden[i].append(1)
            else:
                matrizIden[i].append(0)
    print("Matriz identidad:")
    for fila in matrizIden:
        print(fila)

