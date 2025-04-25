#EJERCICIO 1
print("NÚMERO PAR O IMPAR");print()

n = int(input("Ingrese un número entero: "));print()

if(n%2 == 0):
    print("Número Par")
else:
    print("Número Impar")
-----------------------------------------------------
#EJERCICIO 2
print("SUMA_LISTA");print()

def suma_lista(lista):
    print(lista)
    print(sum(lista))
suma_lista([2,4,6])
---------------------------
#EJERCICIO 3
print("CUENTA REGRESIVA");print()

def cuenta_regresiva(n):
    if (n<0):
        print("¡DESPEGUE!")
    else:
        print(n)
        cuenta_regresiva(n-1)
cuenta_regresiva(10)
-----------------------------------
#EJERCICIO 4
print("CUENTA ASCENDENTE");print()

def cuenta_ascendente(n):
    for i in range(0,n+1):
        print(i)
cuenta_ascendente(10)
----------------------------------
#EJERCICIO 5
print("SUMA_HASTA");print()

def suma_hasta(n):
    a = 0
    for i in range(0,n+1):
        a += i
    print(f"Sumatoria hasta {n}: {a}")
suma_hasta(5)
----------------------------------------
#EJERCICIO 6
print("FUNCIÓN FACTORIAL");print()

def factorial(f):
    a = 1
    for i in range (1,f+1):
        a *= i
    print(f"Factorial de {f}: {a}")
factorial(100)
-------------------------------------
#EJERCICIO 7
print("MÍNIMO EN LISTA");print()

def minimo(lista):
    print(lista)
    print(f"Mínimo: {min(lista)}")
minimo([10,20,30,2,48])
------------------------------------
#JUEGO
import time

def adivina_el_numero(numero_secreto, intentos, tiempo_inicio):
    if intentos == 0:
        print("¡Te has quedado sin intentos! El número era:", numero_secreto)
        return

    intento = int(input("Ingresa tu intento: "))

    if intento == numero_secreto:
        tiempo_final = time.time()
        tiempo_total = round(tiempo_final - tiempo_inicio, 2)
        print(f"¡Felicidades! Adivinaste el número en {tiempo_total} segundos.")
    elif intento < numero_secreto:
        print("Un poco más arriba")
        adivina_el_numero(numero_secreto, intentos - 1, tiempo_inicio)
    else:
        print("Un poco más abajo")
        adivina_el_numero(numero_secreto, intentos - 1, tiempo_inicio)

# Número secreto fijo (puedes usar random si quieres que sea aleatorio)
numero_secreto = 80

# Iniciar el juego con 5 intentos
print("Bienvenido al juego de Adivina el Número.")
print("Elige un número entre 1 y 100.")
print("¡Buena suerte!\n")

tiempo_inicio = time.time()  # Marca el inicio del tiempo
adivina_el_numero(numero_secreto, 5, tiempo_inicio)
