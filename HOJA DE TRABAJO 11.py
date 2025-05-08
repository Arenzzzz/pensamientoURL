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

#EJERCICIO 2
print("CALCULADORA CIENTÍFICA");print()
print("1. Raiz Cuadrada")
print("2. Potencia")
print("3. Logaritmo")
print("4. Factorial")

import math

# Clase abstracta
class OperacionCientifica():
    def Calcular(self):
        pass
    
class RaizCuadrada(OperacionCientifica):
    def __init__(self, radicando):
        self.radicando = radicando
    def Calcular(self):
        raiz = (radicando)**0.5
        if self.radicando < 0:
            raise ValueError("No puedes ingresar números negativos")
        return raiz
        
class Potencia(OperacionCientifica):
    def __init__(self, base, exponente):
        self.base = base
        self.exponente = exponente
    def Calcular(self):
        potencia = base**exponente
        return potencia

class Logaritmo(OperacionCientifica):
    def __init__(self, base, argumento):
        self.base = base
        self.argumento = argumento
    def Calcular(self):
        if self.argumento < 0 or self.base < 0:
           raise ValueError("No puedes ingresar números negativos como argumento o base")
        logaritmo = math.log(argumento, base)
        return logaritmo
    
class Factorial(OperacionCientifica):
    def __init__(self, base):
        self.base = base
    def Calcular(self):
            if self.base < 0:
                raise ValueError("La base debe de ser un número positivo")
            factorial = 1
            for a in range(1, base+1):
                factorial *= a
            return factorial

operacion = int(input("¿Qué operacion desea efectuar?: "));print()

try:
    if operacion == 1:
        radicando = float(input("Ingrese el radicando: "))
        x = RaizCuadrada(radicando).Calcular()
        print(f"La raíz cuadrada de {radicando} es: {x}")
        
    elif operacion == 2:
        base = float(input("Ingrese la base: "))
        exponente = float(input("Ingrese el exponente: "))
        x = Potencia(base, exponente).Calcular()
        print(f"{base} elevado a {exponente} es: {x}")
        
    elif operacion == 3:
        base = float(input("Ingrese la base: "))
        argumento = float(input("Ingrese el argumento: "))
        x = Logaritmo(base, argumento).Calcular()
        print(f"El logaritmo de {argumento} de base {base} es: {x}")
    
    elif operacion == 4:
        base = float(input("Ingrese la base: "))
        if base % 1 == 0:
            base = int(base)
            x = Factorial(base).Calcular()
            print(f"El factorial de {base} es: {x}")
        else:
            raise ValueError("La base debe de ser un número entero")
    else:
        print("OPERACIÓN INVÁLIDA")
except (ValueError, TypeError) as e:
    print("ERROR EN LA OPERACIÓN:",e)
