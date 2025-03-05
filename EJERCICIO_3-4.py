#EJERCICIO 1
texto = str(input("Ingrese una oración: "))
print()

a = texto.split()
b = len(a)
c = a[0]
d = a[b-1]


print(f"Primera palabra: {c}")
print(f"Última palabra: {d}")

#EJERCICIO 2
texto = str(input("Ingrese una oración: "))
print()

c = texto.split()
a = ' '.join(c)

print(a)
