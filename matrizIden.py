from colorama import Fore, Style

def matrizIdentidad():

    matriz = []

    n = int(input("Ingrese el tamaño de la matriz: "))

    for i in range(n):
        matriz.append([])

        for j in range(n):

            if i == j:
                matriz[i].append(1)

            else:
                matriz[i].append(0)

    for i in range(n):
        for j in range(n):

            if i == j:
                print(Fore.BLUE + str(matriz[i][j]) + Style.RESET_ALL, end=" ")

            else:
                print(matriz[i][j], end=" ")

        print()