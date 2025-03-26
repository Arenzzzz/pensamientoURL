#EJERCICIO 1
print("Números impares del 1 al 10 (FOR)")

for i in range(1,11):
    if (i % 2 != 0):
        print(i)

#EJERCICIO 2
print("Números impares del 1 al 10 (WHILE)")

x = 1

while x < 11:
    if (x % 2 != 0):
        print(x)
    x += 1

#ESCENARIO 1

secreta = "chupacabra"

while True:
    a = str(input("Adivine la palabra secreta para salir: "))
    a = a.lower()
    
    if (a == secreta):
        break
    
print("¡Has dejado el bucle con éxito")

#ESCENARIO 2
print("Devorador de palabras"); print()

w = str(input("Ingrese una palabra para devorar 🫦: "))
w = w.upper()
vocales = ['A','E','I','O','U']

for i in w:
    if (i == "A") or (i == "E") or (i == "I") or (i == "O") or (i == "U"):
        continue
    
    print(i)
