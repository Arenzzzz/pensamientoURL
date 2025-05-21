matriz = [
 [0,0,0,0,0,0,0,1,1,0],
 [0,1,1,0,0,0,0,0,0,0],
 [0,1,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,1,1,0,0,0],
 [0,0,0,0,0,1,1,0,0,0],
 [0,0,1,1,0,0,0,0,0,0],
 [0,0,1,1,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,1,0],
]

# Matrices donde se guardarán las generaciones de células a partir de la generación 0 (matriz)
m2 = []
m3 = []

# Función para comprobar vida de cada célula dentro de la matriz
def matrices(a,b):
    for i in a:
        x = []
        for j in range(len(i)):
            # Comprobación a células en el primer índice de cada lista
            if j == 0:
                if i[j+1]==1:
                    x.append(1)
                else:
                    x.append(0)
            # Comprobación a células en el último índice de cada lista
            elif j == (len(i)-1):
                if i[j-1]==1:
                    x.append(1)
                else:
                    x.append(0)
            # Comprobación a las demás células dentro de cada lista
            else:
                # Células que mueren (si están entre 2 vivas o entre 2 muertas)
                if (i[j-1]==1 and i[j+1]==1) or (i[j-1]==0 and i[j+1]==0):
                    x.append(0)
                # Células que viven o nacen de nuevo (si están entre una viva y una muerta o viceversa)
                elif (i[j-1]==1 and i[j+1]==0) or (i[j-1]==0 and i[j+1]==1):
                    x.append(1)
        b.append(x)
    return b

# Función para imprimir más estéticas las matrices
def imprimir_tablero(a):
    for i in a:
        for j in i:
            print(j, end=" ")
        print()
    return " "

# Imprimir cada generación
print("Generación 0:");print(imprimir_tablero(matriz))
print("Generación 1:");print(imprimir_tablero(matrices(matriz,m2)))
print("Generación 2:");print(imprimir_tablero(matrices(m2,m3)))
