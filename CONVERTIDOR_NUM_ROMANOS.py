#Moshé Arenz Peláez Virula  1556425

print("PROGRAMA QUE CONVIERTE NÚMEROS ARÁBIGOS A ROMANOS EN UN RANGO DE 1 - 9\n")
num = int(input("INGRESE UN NÚMERO\n"))

if num>=1 and num<=9:
    if num <= 3:
        res = num * "I"
        print(f"El número {num} en Romano es: {res}")
    if num == 4:
        print(f"El número {num} en Romano es: IV")
    if num>=5 and num<=8:
        res = "V"+(num - 5)*"I"
        print(f"El número {num} en Romano es: {res}")
    if num == 9:
        print(f"El número {num} en Romano es: IX")
else:
    print("El número ingresado está fuera del rango")
