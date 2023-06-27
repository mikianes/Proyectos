"""
/*
 * Crea tres test sobre el reto 12: "Viernes 13".
 * - Puedes copiar una solución ya creada por otro usuario en
 *   el lenguaje que estés utilizando.
 * - Debes emplear un mecanismo de ejecución de test que posea
 *   el lenguaje de programación que hayas seleccionado.
 * - Los tres test deben de funcionar y comprobar
 *   diferentes situaciones (a tu elección).
 */
"""
import unittest
import Viernes13_testing


class TestUtils(unittest.TestCase):
    def test_is_prime(self):
        self.assertFalse(Viernes13_testing.friday("enero",2023))
        self.assertFalse(Viernes13_testing.friday("febrero",2023))
        self.assertFalse(Viernes13_testing.friday(2,2023))
    
if __name__ == '__main__':
    unittest.main()



