""" /*
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 */ """


class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    def sonido(self):
        pass

    def descripcion(self):
        print(
            f"Soy un Animal del tipo {self.especie} y tengo {self.edad} años.")


class Perro(Animal):

    sound: int = "Guau"

    def __init__(self, especie, edad, sound):
        super().__init__(especie, edad)
        self.sound = sound

    def mostrar(self):
        print(
            f"Soy un Animal del tipo {self.especie} y tengo {self.edad} años.{self.sound}")


class Gato(Animal):
    def sonido(self):
        print("Miau")


""" Extra """


class Jerarquia:
    def __init__(self, identificador, nombre):
        self.identificador = identificador
        self.nombre = nombre


class Empleado(Jerarquia):
    def __init__(self, identificador, nombre, empleados):
        super().__init__(identificador, nombre)
        self.empleados = empleados


class Gerente(Empleado, Jerarquia):
    def __init__(self, identificador, nombre, empleados):
        super().__init__(identificador, nombre, empleados)
        self.puesto = "Gerente"
        self.funcion = ["Mando", "Despido"]

    def Mostrar_empleados(self):
        print(
            f"Identificador:{self.identificador}, Nombre:{self.nombre}, Empleados:{self.empleados},Puesto:{self.puesto},Función:{self.funcion}")


class GerenteProyectos(Empleado, Jerarquia):
    def __init__(self):
        self.puesto = "Gerente Proyectos"
        self.funcion = ["Pido", "Me quejo"]


class Programador(Empleado, Jerarquia):
    def __init__(self):
        self.puesto = "Programador"
        self.funcion = ["Pico", "Aguanto"]


my_animal = Animal("Pajaro", 5,)
my_animal.descripcion()
print("-----------")
my_perro = Perro("Perro", 10, "Guau")
my_perro.descripcion()
my_perro.mostrar()
print("-----------")
my_gato = Gato("Gato", 5)
my_gato.descripcion()
my_gato.sonido()
print("----------")
print("EXTRA")
my_empleado = Empleado(23, "Pedro", ["Juan", "Juana"])
# my_empleado.Mostrar_empleados()
my_gerente = Gerente(00, "Pedro", ["Pepe", "Pepa"])
my_gerente.Mostrar_empleados()
