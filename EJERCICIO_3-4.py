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

#EJERCICIO 3
mail = str(input("Ingrese un correo: "))
print()

dominio = mail.split('@')
a = dominio[1]

print(f"El dominio es: {a}")

#EJERCICIO 4
file = str(input("Ingrese un archivo: "))
print()

tipo = file.split('.')
a = tipo[1]

val = bool(a == 'pdf')

print(f"¿El archivo es .pdf? = {val}")

#EJERCICIO 5
texto = str(input("Ingrese una oración: "))
print()

a = texto.split()
b = a[::-1]
c = ' '.join(b)

print(c)

