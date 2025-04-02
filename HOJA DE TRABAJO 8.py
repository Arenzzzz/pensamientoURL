#EJERCICIO 1
print("MÚLTIPLOS")
n = int(input("Ingrese cantidad de múltiplos: "))
m = int(input("Ingrese valor base: "));print()

multiplos = []

for i in range(1,n+1):
    multiplos.append(i*m)
print(f"Los primeros {n} múltiplos de {m} = {multiplos}")

#EJERCICIO 2
print("LONGITUD DE NOMBRES")
n = int(input("Ingrese cantidad de nombres: "))

nombres = []
longitud = []

for i in range(0,n):
    a = input(f"Ingrese nombre {i+1}: ")
    nombres.append(a)
    longitud.append(len(nombres[i]))
    
print(f"\n{nombres}")
print(f"La longitud de cada nombres es {longitud}")

#ESCENARIO 1
print("ENCUESTA DE SATISFACCIÓN")
n = int(input("Número de clientes a encuestar: "))

dic_encuesta = {5:"Excelente", 4:"Muy bueno", 3:"Bueno", 2:"Regular", 1:"Malo"}

print("Escala")
print("5. Excelente")
print("4. Muy buena")
print("3. Buena")
print("2. Regular")
print("1. Malo")

e = 0
m = 0
b = 0
r = 0
ma = 0
encuesta = []


for i in range(0,n):
    x = int(input("¿Cuál es tu calificación?: "))
    encuesta.append(str(x))
    
    if x == 5:
        e += 1
    elif x == 4:
        m += 1
    elif x == 3:
        b += 1
    elif x == 2:
        r += 1
    elif x == 1:
        ma += 1
        
print(f"\nEXCELENTE: {e}")
print(f"MUY BUENO: {m}")
print(f"BUENO: {b}")
print(f"REGULAR: {r}")
print(f"MUY MALO: {ma}")
#print(f"\nENCUESTA: {encuesta}")
moda = max(encuesta, key=encuesta.count)
print(f"MODA: {moda} = {dic_encuesta[int(moda)]}")
