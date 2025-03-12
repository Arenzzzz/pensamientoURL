#EJERCICIO 1
print("CÁLCULO DE SERVICIO DE AGUA \n")

consumo = float(input("Ingrese el consumo de agua en m³: "))        #LEER EL CONSUMO
h = int(input("Ingrese el número de habitantes en el área: "))      #LEER NÚMERO DE HABITANTES
print()

if (consumo<15):    #Si el consumo es menor a 15 m³
    print(f"La tarifa es de Q{5*consumo}")

elif (consumo>=15 and consumo<=30): #Si el consumo está entre 15 y 30 m³
    if(h>3):
        print(f"La tarifa es de Q{4*consumo}")
    elif(h==3):
        print(f"La tarifa es de Q{4.5*consumo}")
    else:
        print(f"La tarifa es de Q{5*consumo}")

elif (consumo>30):  #Si el consumo es mayor a 30 m³
    if(h>5):
        print(f"La tarifa es de Q{3.5*consumo}")
    elif(h%2==0):
        print(f"La tarifa es de Q{4*consumo}")
    else:
        print(f"La tarifa es de Q{4.2*consumo}")
