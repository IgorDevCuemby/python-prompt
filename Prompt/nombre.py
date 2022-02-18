# -*- coding: utf-8 -*-
# -- coding: utf-8 --

# Librerias
import os

# Funciones Auxiliares


def suma(num1, num2):
    # ToDo: validar cual es el mayor de los dos numeros
    # if

    return num1 + num2


# funcion principal
def main():
    # Variables nombres y telefono solicitados al usuario
    nombres = raw_input("¿Cual es tu nombre? ")
    telefono = raw_input("¿Cual es tu telefono? ")

    num1 = int(raw_input("Ingrese un numero: "))
    num2 = int(raw_input("Ingrese otro numero: "))

    # Variable resultado, almacena la suma de los dos numeros definida en la funcion suma
    resultado = suma(num1, num2)

    print(nombres + " tiene " + str(len(nombres)) + " letras")
    print("Su numero es " + telefono)

    print("El resultado de la suma es " + str(resultado))


if __name__ == '__main__':
    main()
