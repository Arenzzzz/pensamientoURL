#Hecho por: ARENZ PELÁEZ - 1556425
print("PROGRAMA DE SALUD");print()

# Número de días a registrar
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

# Datos simulados de 1 semana de paciente
azucar = [120, 160, 95, 175, 160] # mg/dL
sal = [2000, 2400, 1800, 2400, 2700] # mg
presion = [115, 130, 110, 125, 175] # mmHg


for i in range(len(dias)):
    print("***********************************")
    print(f"Registro del día {dias[i]}")
    #AZUCAR
    print(f"Azúcar: {azucar[i]}")
    if azucar[i] < 70:
        print("     Nivel de azúcar BAJO")
    elif azucar[i] > 140:
        print("     Nivel de azúcar ALTO\nCONSULTE A SU MÉDICO")
    else:
        print("     AZÚCAR NORMAL")

    #SAL
    print(f"Sal: {sal[i]}")
    if sal[i] > 2300:
        print("     Consumo elevado de sal\nCONSULTE A SU MÉDICO")
    else:
        print("     SAL NORMAL")

    #PRESIÓN    
    print(f"Presión: {presion[i]}")
    if presion[i] < 120:
        print("     PRESIÓN NORMAL")
    elif 120 <= presion[i] <= 129:
        print("     Presión elevada")
    elif 130 <= presion[i] <= 139:
        print("     ALERTA: Hipertensión etapa 1\nCONSULTE A SU MÉDICO")
    elif 140 <= presion[i]:
        print("     ALERTA: Hipertensión etapa 2\nCONSULTE A SU MÉDICO")


print("\nPROMEDIO SEMANAL:")
print(f"Azúcar: {sum(azucar)/len(azucar)} mg/dL")
print(f"Sal: {sum(sal)/len(sal)} mg")
print(f"Azúcar: {sum(presion)/len(presion)} mmHg")
