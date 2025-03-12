#Hecho por: ARENZ PELÁEZ - 1556425

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

#EJERCICIO 2
print("REGLAMENTO PARA REGULACIÓN DE TRÁFICO \n")

año = int(input("Ingrese el año del modelo del vehículo: "))       #LEER AÑO DEL VEHÍCULO
placa = input("Ingrese la placa del vehículo: ")                   #LEER PLACA DEL VEHÍCULO
print()

d =  int(placa[-1])    #CONVERTIR ÚLTIMO DÍGITO A ENTERO

if (año>=2001):    #Si el vehículo es del 2001 en adelante
    if(d%2==0):
        if(año%2==0):
            print("El vehículo NO circula los lunes y sábados circula hasta el mediodía")
        else:
            print("El vehículo NO circula los lunes")
            
    elif(d%2!=0):
        if(año%2==0):
            print("El vehículo NO circula los viernes y sábados circula hasta el mediodía")
        else:
            print("El vehículo NO circula los viernes")
    
else:
    print("ADVERTENCIA: Realice mantenimiento al vehículo")
