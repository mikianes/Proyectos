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
