import matrizIden as iden
import matrizMulti as multi
import matrizSuma as suma
import convertirIden as convertir 

while True:
    print("---Bienvenido al menu de matrices de Santiago---")
    print("Presione la opcion que usted desea calcular.")
    print("1. Sumar matrices.")
    print("2. Multiplicacion de matrices.")
    print("3. Crear una matriz de identidad")
    print("4. Convertir matriz a identidad")
    print("5. Salir ")

    try:
        opcion= int(input("Seleccione una opcion:"))

        if opcion ==1:
            suma.sumarMatrices()

        elif opcion ==2:
            multi.multiplicarMatrices()
        elif opcion ==3:
            iden.matrizIdentidad()
        elif opcion== 4:
            convertir.convertirIdentidad()
        elif opcion == 5:
            print("Programa finalizado.")
            break 
        else:
            print("Debe seleccionar una opcion del 1 al 5.")
    except ValueError:
        print("Error: debe ingresar un valor numerico")