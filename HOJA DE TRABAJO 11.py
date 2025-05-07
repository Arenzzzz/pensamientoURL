#EJERCICIO 1
print("SIMULACIÓN DE EXPERIMENTOS DE CAÍDA LIBRE");print()
import math

# Clase abstracta
class ExperimentoFisico():
    def realizar_experimento(self):
        pass

# Subclase CaidaLibre
class CaidaLibre(ExperimentoFisico):
    def __init__(self, altura, gravedad):
        self.altura = altura
        self.gravedad = gravedad

    def realizar_experimento(self):
        if self.altura < 0:
            raise ValueError("La altura no puede ser negativa.")
        if self.gravedad == 0:
            raise ValueError("La gravedad no puede ser cero.")
        
        tiempo = math.sqrt((2 * self.altura) / self.gravedad)
        return tiempo

# Ejemplo de uso

h = float(input("Ingrese altura: "))
g = float(input("Ingrese gravedad: "))

try:
    experimento = CaidaLibre(h, g)
    tiempo_caida = experimento.realizar_experimento()
    print(f"Tiempo de caída: {tiempo_caida:.2f} segundos")
except ValueError as e:
    print("ERROR EN EL EXPERIMENTO:", e)
