#EJERCICIO 1
print("CLÍNICA VETERINARIA");print()

class Animal:
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso

    def mostrar_datos(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad} años, Peso: {self.peso} kg"

    def calcular_dosis(self):
        # Método general, será sobreescrito en las subclases
        return 0

    def generar_ficha(self):
        datos = self.mostrar_datos()
        dosis = self.calcular_dosis()
        return f"{datos}\nDosis recomendada: {dosis} mg"


class Perro(Animal):
    def __init__(self, nombre, edad, peso, raza):
        super().__init__(nombre, edad, peso)
        self.raza = raza

    def calcular_dosis(self):
        return self.peso * 5  # mg por kg (ejemplo)

    def mostrar_datos(self):
        base = super().mostrar_datos()
        return f"{base}, Raza: {self.raza}"


class Gato(Animal):
    def __init__(self, nombre, edad, peso, color):
        super().__init__(nombre, edad, peso)
        self.color = color

    def calcular_dosis(self):
        return self.peso * 3  # mg por kg (ejemplo)

    def mostrar_datos(self):
        base = super().mostrar_datos()
        return f"{base}, Color: {self.color}"


class Ave(Animal):
    def __init__(self, nombre, edad, peso, tipo_ave):
        super().__init__(nombre, edad, peso)
        self.tipo_ave = tipo_ave

    def calcular_dosis(self):
        return self.peso * 2  # mg por kg (ejemplo)

    def mostrar_datos(self):
        base = super().mostrar_datos()
        return f"{base}, Tipo de ave: {self.tipo_ave}"


class Reptil(Animal):
    def __init__(self, nombre, edad, peso, especie):
        super().__init__(nombre, edad, peso)
        self.especie = especie

    def calcular_dosis(self):
        return self.peso * 1.5  # mg por kg (ejemplo)

    def mostrar_datos(self):
        base = super().mostrar_datos()
        return f"{base}, Especie: {self.especie}"


# Ejemplo de uso
perro1 = Perro("Fido", 5, 20, "Labrador")
gato1 = Gato("Michi", 3, 4, "Negro")
ave1 = Ave("Piolín", 2, 0.3, "Canario")
reptil1 = Reptil("Rex", 4, 5, "Iguana")

animales = [perro1, gato1, ave1, reptil1]

for animal in animales:
    print(animal.generar_ficha())
    print("-" * 40)

#EJERCICIO 2
print("PERSONAS EN UNA INSTITUCIÓN");print()

class Persona():
    def __init__(self, nombre, edad, DNI):
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI
    
    def info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.DNI}")

class Estudiante(Persona):
    def __init__(self, nombre, edad, DNI, carrera):
        super().__init__(nombre, edad, DNI)
        self.carrera = carrera
    
    def info(self):
        super().info()
        print(f"Carrera: {self.carrera}")

class Profesor(Persona):
    def __init__(self, nombre, edad, DNI, asignatura):
        super().__init__(nombre, edad, DNI)
        self.asignatura = asignatura
    
    def info(self):
        super().info()
        print(f"Asignatura: {self.asignatura}")

class Admin(Persona):
    def __init__(self, nombre, edad, DNI, puesto):
        super().__init__(nombre, edad, DNI)
        self.puesto = puesto
    
    def info(self):
        super().info()
        print(f"Puesto: {self.puesto}")

P1 = Estudiante("Juan", 20, "12345678A", "Ingeniería")
P2 = Profesor("María", 35, "87654321B", "Matemáticas")
P3 = Admin("Pedro", 40, "11223344C", "Director")

P1.info()
print("-" * 20)
P2.info()
print("-" * 20)
P3.info()
print("-" * 20)
