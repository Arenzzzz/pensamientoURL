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

def imprimir_tablero(a):
    for i in a:
        for j in i:
            print(j, end=" ")
        print()

imprimir_tablero(matriz)

m = [1,0,1,1,0]
m2 = []

for i in m:
    b = m.index(i)
    if i == 1:
        if (m[b-1] == 0 and m[b+1] == 1) or (m[b-1] == 1 and m[b+1] == 0):
            m2.append(1)
        elif m[b-1] == 0 and m[b+1] == 0:
            m2.append(0)
        elif m[b-1] == 1 and m[b+1] == 1:
            m2.append(0)
    elif i == 0:
        if ((m[b-1] == 1 and m[b+1] == 0) or (m[b-1] == 0 and m[b+1] == 1)):
            m2.append(1)
        else:
            m2.append(0)
        
print(m2)
