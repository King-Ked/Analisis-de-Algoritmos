import math

X = []
X1 = []

X.append(int(input("Ingrese cuantos billetes de 1000 hay disponibles: ")))
X.append(int(input("Ingrese cuantos billetes de 500 hay disponibles: ")))
X.append(int(input("Ingrese cuantos billetes de 200 hay disponibles: ")))
X.append(int(input("Ingrese cuantos billetes de 100 hay disponibles: ")))
X.append(int(input("Ingrese cuantos billetes de 50 hay disponibles: ")))
X.append(int(input("Ingrese cuantos billetes de 20 hay disponibles: ")))
X.append(int(input("Ingrese cuantas monedas de 10 hay disponibles: ")))
X.append(int(input("Ingrese cuantas monedas de 5 hay disponibles: ")))
X.append(int(input("Ingrese cuantas monedas de 2 hay disponibles: ")))
X.append(int(input("Ingrese cuantas monedas de 1 hay disponibles: ")))

X1.append(1000)
X1.append(500)
X1.append(200)
X1.append(100)
X1.append(50)
X1.append(20)
X1.append(10)
X1.append(5)
X1.append(2)
X1.append(1)

Y = int(input("Ingrese la cantidad a evaluar:"))


def ret_listofvalues(X, X1, Y, i=0):
    if Y == 0:
        return "/0"
    elif i == 10:
        return "/NS"
    else:
        if math.floor(Y / X1[i]) < X[i]:
            return (
                "/"
                + str(math.floor(Y / X1[i]))
                + ret_listofvalues(X, X1, (Y % X1[i]), i + 1)
            )
        else:
            return (
                "/" + str(X[i]) + ret_listofvalues(X, X1, (Y - (X1[i] * X[i])), i + 1)
            )


endstr = ret_listofvalues(X, X1, Y, i=0)
endstr = endstr[1:]

if endstr.find("NS") != -1:
    print("No se pudo crear el cambio exacto")

else:
    for x in range(10):
        if endstr == "":
            break
        elif endstr.find("/") == -1:
            print("Se necesitan " + endstr + " de " + str(X1[x]))
        else:
            print("Se necesitan " + endstr[: endstr.find("/")] + " de " + str(X1[x]))
            endstr = endstr[endstr.find("/") + 1 :]
