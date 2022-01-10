import numpy as np
import math


def manejaBase(cadena, base, Guia):

    if Guia == 0 and base != 10:
        cadena = str(int(cadena, base))

    elif Guia == 1 and base == 2:
        cadena = int(cadena)
        cadena = bin(cadena)[2:]

    elif Guia == 1 and base == 16:
        cadena = int(cadena)
        cadena = hex(cadena)[2:]

    return cadena


def manejaLongitud(cadena1, cadena2):

    if len(cadena1) != len(cadena2):
        auxmax = max(len(cadena1), len(cadena2))
        auxmin = min(len(cadena1), len(cadena2))

        if auxmax == len(cadena1):
            cadena2 = ("0" * (auxmax - auxmin)) + cadena2
        elif auxmax == len(cadena2):
            cadena1 = ("0" * (auxmax - auxmin)) + cadena1

    if np.log2(len(cadena1)).is_integer() == False:
        aux = math.ceil(np.log2(len(cadena1)))
        aux = 2 ** aux
        aux = aux - len(cadena1)
        cadena1 = ("0" * aux) + cadena1
        cadena2 = ("0" * aux) + cadena2

    return cadena1, cadena2


def productoNormal(x, y):
    aux = int(x) * int(y)
    aux = str(aux)
    return aux


def dividir(xy, dir, n):
    aux = xy

    if dir == "i":
        aux = aux[: int(n / 2)]
    elif dir == "d":
        aux = aux[int(n / 2) :]
    return aux


def multiplica(x, y, n):
    if n == 1:
        return productoNormal(x, y)

    else:
        xi = dividir(x, "i", n)
        xd = dividir(x, "d", n)
        yi = dividir(y, "i", n)
        yd = dividir(y, "d", n)
        p1 = multiplica(xi, yi, int(n / 2))

        aux1 = int(xi) + int(xd)
        aux1 = str(aux1)
        aux2 = int(yi) + int(yd)
        aux2 = str(aux2)

        aux1, aux2 = manejaLongitud(aux1, aux2)

        p2 = multiplica(aux1, aux2, int(len(aux1)))
        p3 = multiplica(xd, yd, int(n / 2))

        resultado = (
            ((10 ** n * int(p1)))
            + (10 ** int(n / 2) * (int(p2) - int(p1) - int(p3)))
            + int(p3)
        )

    return resultado


x = input("Ingrese el primer numero a multiplicar: ")
y = input("Ingrese el segundo numero a multiplicar: ")
base = int(input("Ingrese la base que se quiere manejar: "))

x = manejaBase(x, base, 0)
y = manejaBase(y, base, 0)

x, y = manejaLongitud(x, y)

n = int(len(x))

resultado = multiplica(x, y, n)
resultado = manejaBase(resultado, base, 1)

print(resultado)
