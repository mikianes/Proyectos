"""
/*
* EJERCICIO:
 * Empleando tu lenguaje, explora la definición del tipo de dato
 * que sirva para definir enumeraciones(Enum).
 * Crea un Enum que represente los días de la semana del lunes
 * al domingo, en ese orden. Con ese enumerado, crea una operación
 * que muestre el nombre del día de la semana dependiendo del número entero
 * utilizado(del 1 al 7).
 *
 * DIFICULTAD EXTRA(opcional):
 * Crea un pequeño sistema de gestión del estado de pedidos.
 * Implementa una clase que defina un pedido con las siguientes características:
 * - El pedido tiene un identificador y un estado.
 * - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
 * - Implementa las funciones que sirvan para modificar el estado:
 * - Pedido enviado
 * - Pedido cancelado
 * - Pedido entregado
 *   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
 * - Implementa una función para mostrar un texto descriptivo según el estado actual.
 * - Crea diferentes pedidos y muestra cómo se interactúa con ellos.
 */
"""
from enum import Enum

# EJERCICIO


""" class week(Enum):
    Lunes = 1
    Martes = 2
    Miercoles = 3
    Jueves = 4
    Viernes = 5
    Sabado = 6
    Domingo = 7


print(week(1).name)
print(week(7).name)
# print(week(8).name) """

# EXTRA

orders = {}


class Status(Enum):
    Pendiente = 0
    Enviado = 1
    Entregado = 2
    Cancelado = 3


class Order:

    def __init__(self, id: int, state: str):
        self.id = id
        self.state = state
        orders[self.id] = self.state

    def print(self):
        print(
            f"Id: {self.id} | Status: {self.state} ")


def update(id: int, state: str, orders: dict):

    # Comprobar si existe el pedido.
    if id is not None and id in orders:
        if (validate_order(id, state, orders)):
            orders[id] = Status(state).name
            print(orders)
        else:
            print("No se puede actualizar el estado")

    else:
        print("Pedido no encontrado")


def validate_order(id: int, state: str, orders: dict) -> bool:

    new_status = Status(state).name
    print(f" id:{id} | New Status:{new_status} | Original Orders: {orders}")

    # Si está pendiente no puede ser recibida
    status = orders.get(id)
    if status == Status(0).name and new_status == Status(2).name:
        print("Un pedido pendiente no puede ser recibido.")
        return False

    # Si está enviada no puede ser pendiente
    if status == Status(1).name and new_status == Status(0).name:
        print("Un pedido enviado no puede estar pendiente.")
        return False

    # Si está recibida no puede ser enviada
    if status == Status(2).name and new_status == Status(1).name:
        print("Un pedido recibido no puede ser enviado.")
        return False

    # Si está cancelada no puede tener mas estados
    if status == Status(3).name:
        print("Un pedido cancelado no puede cambiar de estado.")
        return False

    return True


def main():

    my_order = Order(1, Status(0).name)
    my_order1 = Order(2, Status(1).name)

    update(1, 1, orders)  # OK pasa de Pendiente a Enviado
    update(2, 0, orders)  # NOK de envíado no puede pasar a Pendiente
    update(5, 0, orders)  # NOK no existe el pedido


if __name__ == "__main__":

    main()
