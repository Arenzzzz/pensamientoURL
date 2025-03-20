print("Hecho por: Arenz Peláez - 1556425\n")
print("CAJERO AUTOMÁTICO")

saldo = 3000; print(f"Su saldo es Q{saldo:.2f}")    #SALDO INICIAL
n = float(input("Ingrese monto a retirar: ")); print()      #LEER MONTO A RETIRAR
intentos = 1    #DECLARAR EL CONTADOR DE INTENTOS

while True:
#CASOS PARA CONTINUAR EL CICLO
    if (n <= saldo):    #SI EL MONTO ES MENOR O IGUAL AL SALDO: REINICIAR EL CONTADOR DE INTENTOS, CALCULAR EL NUEVO SALDO Y MOSTRARLO
        intentos = 1    
        saldo = saldo - n 
        print(f"Su saldo es Q{saldo:.2f}") 
        
        if(saldo > 0):  #SI EL SALDO ES MAYOR A 0 SE PUEDE RETIRAR MÁS DINERO
            n = float(input("Ingrese monto a retirar: ")); print()
            
    elif (n > saldo):   #SI EL MONTO ES MAYOR AL SALDO: MOSTRAR MENSAJE DE MONTO INVÁLIDO Y PEDIR NUEVAMENTE EL MONTO
        print(f"Monto inválido, tiene {3-intentos} inteto(s)")
        intentos += 1
        n = float(input("Ingrese monto a retirar: ")); print()

#CASOS PARA ROMPER EL CICLO
    if (intentos == 3) and (n > saldo):    #SI SE EXCEDEN LOS INTENTOS: ROMPER EL CICLO
        print("Intentos excedidos")
        break
    if (saldo == 0) or (n == 0):    #SI EL SALDO ES 0 O EL MONTO ES 0 (OPCIÓN DE SALIR): ROMPER EL CICLO
        print("Gracias por usar el cajero")
        break
