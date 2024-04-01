from datetime import datetime, date
from PruebasUnitarias import sum
from PruebasUnitarias import names
import unittest
import logging
import sys


class TestCalculaSuma(unittest.TestCase):
    def test_1(self):
        resultado = sum(5, 1)
        self.assertEqual(resultado, 6)

    def test_2(self):
        resultado = sum(-5, 3.1)
        self.assertEqual(resultado, -1.9)

# dic = {"name":"Pedro","age":"41","birth_date":"10/03/1983","programming_languajes":["Java","Python","SQL"]}


class TestDictComprobation(unittest.TestCase):
    def test_1(self):
        result = 0
        key = ["name", "age", "birth_date", "programming_languajes"]

        for value in key:
            if names.get(value) is not None:
                result += 1

        self.assertEqual(result, len(key))

    def test_2(self):
        dictionary = {"name": "Pedro", "age": "41", "birth_date": "10/03/1983",
                      "programming_languajes": ["Java", "Python", "SQL"], "Prueba": "Prueba"}

        self.assertEqual(dictionary, names)


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr)
    logging.getLogger("TestDectComprobation.test_1").setLevel(logging.DEBUG)
    unittest.main()


# Corrección Moure


"""
Ejercicio
"""


""" def sum(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Los argumentos deben ser enteros o decimales.")
    return a + b


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(5, 7), 12)
        self.assertEqual(sum(5, -7), -2)
        self.assertEqual(sum(0, 0), 0)
        self.assertEqual(sum(2.5, 2.1), 4.6)
        self.assertEqual(sum(2, 2.1), 4.1)
        self.assertEqual(sum(2.5, 2.5), 5)

    def test_sum_type(self):
        with self.assertRaises(ValueError):
            sum("5", 7)
        with self.assertRaises(ValueError):
            sum(5, "7")
        with self.assertRaises(ValueError):
            sum("5", "7")
        with self.assertRaises(ValueError):
            sum("a", 7)
        with self.assertRaises(ValueError):
            sum(None, 7)


"""
# Extra
"""


class TestData(unittest.TestCase):

    def setUp(self) -> None:
        self.data = {
            "name": "Brais Moure",
            "age": 36,
            "birth_date": datetime.strptime("29-04-87", "%d-%m-%y").date(),
            "programming_languages": ["Python", "Kotlin", "Swift"]
        }

    def test_fields_exist(self):
        self.assertIn("name", self.data)
        self.assertIn("age", self.data)
        self.assertIn("birth_date", self.data)
        self.assertIn("programming_languages", self.data)

    def test_data_is_correct(self):
        self.assertIsInstance(self.data["name"], str)
        self.assertIsInstance(self.data["age"], int)
        self.assertIsInstance(self.data["birth_date"], date)
        self.assertIsInstance(self.data["programming_languages"], list)
 """
