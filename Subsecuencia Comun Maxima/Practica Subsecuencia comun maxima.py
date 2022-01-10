X = input("Ingrese la primera cadena:")
Y = input("Ingrese la segunda cadena:")

L = [""] * (len(X) + 1)

for x in range(len(X) + 1):
    aux = L[x]
    for y in range(len(Y) + 1):
        if x == 0 or y == 0:
            aux = aux + "0"
        elif X[x - 1] == Y[y - 1]:
            aux = aux + str(int(L[x - 1][y - 1]) + 1)
        elif X[x - 1] != Y[y - 1]:
            aux = aux + str(max(int(aux[y - 1]), int(L[x - 1][y])))

    L[x] = aux


def max_sub(L, i, j):

    if i == 0 or j == 0:
        return ""
    if L[i][j] == L[i - 1][j - 1]:
        return max_sub(L, i - 1, j - 1)
    elif L[i][j] == L[i][j - 1]:
        return max_sub(L, i, j - 1)
    elif L[i][j] == L[i - 1][j]:
        return max_sub(L, i - 1, j)
    elif L[i][j] != L[i][j - 1]:
        return max_sub(L, i - 1, j - 1) + str(i)


print("   " + Y)
for x in range(len(L)):
    if x == 0:
        print("  " + L[x])
    else:
        print(X[x - 1] + " " + L[x])

aux = max_sub(L, len(X), len(Y))
auxF = ""
for x in range(len(aux)):
    auxF = auxF + X[int(aux[x]) - 1]

print(auxF)
