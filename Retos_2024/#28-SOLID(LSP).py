""" /*
* EJERCICIO:
 * Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)"
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
 * DIFICULTAD EXTRA(opcional):
 * Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
 * cumplir el LSP.
 * Instrucciones:
 * 1. Crea la clase Vehículo.
 * 2. Añade tres subclases de Vehículo.
 * 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
 * 4. Desarrolla un código que compruebe que se cumple el LSP.
 */ """


class vehicle:
    def accelerate(self):
        return "Acelerate"

    def brake(self):
        return "Brake"


class bus(vehicle):
    pass


class car(vehicle):
    pass


class trailer(vehicle):  # remolque
    def accelerate(self):
        return "Can't accelerate"


def test_drive(vehicle):
    try:
        test = vehicle.accelerate()
        test += ", "
        test += vehicle.brake()
        return test

    except NotImplementedError as e:
        return str(e)


iveco = bus()
opel = car()
remolque = trailer()

print(f"Iveco: {test_drive(iveco)}")
print(f"Opel: {test_drive(opel)}")
print(f"Trailer: {test_drive(remolque)}")
