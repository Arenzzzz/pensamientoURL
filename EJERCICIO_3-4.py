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

#EJERCICIO 6
POEMA_AMOR = "Te amo como se aman ciertas cosas oscuras, secretamente, entre la sombra y el alma."
CANTO_ALEGRE = "Buenos días, alegría (Buenos días, Señor Sol) Buenos días al amor (Bueno días ah ah) Buenos días a la vida (Buenos días, Señor Sol) Buenos días, Señor Sol (Bueno días ah ah) Yo seguiré tratando ser mejor Yo seguiré tratando ser mejor"
POEMA_TRISTE = "Se desprendió mi sangre para formar tu cuerpo. Se repartió mi alma para formar tu alma. Y fueron nueve lunas y fue toda una angustia de días sin reposo y noches desveladas."
DATO_INTERESANTE = "La tripofobia es el miedo a los agujeros muy juntos. O más específicamente, una aversión a la vista de patrones irregulares o grupos de pequeños agujeros o protuberancias."

texto = str(input("¿De qué quiere hablar hoy?: "))
print()

a = texto.split()

if ("amor" in a):
    print(POEMA_AMOR)
elif ("alegre" in a):
    print(CANTO_ALEGRE)
elif("triste" in a):
    print(POEMA_TRISTE)
elif("interesante" in a):
    print(DATO_INTERESANTE)

