import datetime
from decimal import Decimal
from math import sqrt
import csv


class MedadRangi:
    offer_rate = Decimal('0.1')
    store_longitude = 51.50185488303431  # tool
    store_latitude = 35.74317403843504  # arz

    def __init__(self, name, price, count, country, factory_name):
        self.name = name
        self.price = price
        self.count = count
        self.country = country
        self.factory_name = factory_name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError
        elif len(value.strip()) == 0:
            raise ValueError
        self._name = value

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        if not isinstance(value, str):
            raise TypeError
        elif len(value.strip()) == 0:
            raise ValueError
        self._country = value

    @property
    def factory_name(self):
        return self._factory_name

    @factory_name.setter
    def factory_name(self, value):
        if not isinstance(value, str):
            raise TypeError
        elif len(value.strip()) == 0:
            raise ValueError
        self._factory_name = value

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        if not isinstance(value, int):
            raise TypeError
        self._count = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, int) and not isinstance(value, float) and not isinstance(value, Decimal):
            raise TypeError
        self._price = value

    @staticmethod
    def welcome():
        if 6 <= datetime.datetime.now().hour < 12:
            print("Good Morning")
        elif 12 <= datetime.datetime.now().hour < 18:
            print("Good Evening")
        else:
            print("Good Night")

    def final_price(self):
        self.price_final = self.price * self.count * (1 - MedadRangi.offer_rate)
        return self.price_final

    @classmethod
    def calculate_distance(cls, destination_longitude, destination_latitude):
        return (round(
            sqrt((destination_longitude - cls.store_longitude) ** 2 + (destination_latitude - cls.store_latitude) ** 2),
            3))

    def load_csv(self):
        with open("test.csv", "r", newline='') as test:
            reader = csv.reader(test)
            for row in reader:
                try:
                    q = row[0] + row[1]
                    exec(q)
                except:
                    pass


#########################################################
import unittest


class TestMedadRangi(unittest.TestCase):
    def test_create_instance1(self):
        name = "pen"
        price = 2000
        count = 3
        country = "France"
        factory_name = "bic"
        medadrangi = MedadRangi(name, price, count, country, factory_name)
        self.assertEqual("pen", medadrangi.name)
        self.assertEqual(2000, medadrangi.price)
        self.assertEqual(3, medadrangi.count)
        self.assertEqual("France", medadrangi.country)
        self.assertEqual("bic", medadrangi.factory_name)

    def test_create_instance2(self):
        name = " "
        price = 3000
        count = 4
        country = "Canada"
        factory_name = "canco"
        with self.assertRaises(ValueError):
            test = MedadRangi(name, price, count, country, factory_name)

    def test_final_price(self):
        name = "pen"
        price = 5000
        count = 5
        country = "France"
        factory_name = "bic"
        medadrangi = MedadRangi(name, price, count, country, factory_name)
        self.assertEqual(Decimal("22500.0"), medadrangi.final_price())

    def test_calculate_distance(self):
        name = "pencil"
        price = 3000
        count = 7
        country = "France"
        factory_name = "bic"
        medadrangi = MedadRangi(name, price, count, country, factory_name)
        self.assertEqual(24.233,
                         medadrangi.calculate_distance(destination_longitude=70.54315, destination_latitude=20.754365))


if __name__ == '__main__':
    unittest.main()




















