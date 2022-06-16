import datetime
import csv
from decimal import Decimal
class MedadRangi:
    y, x = (35.74317403843504, 51.50185488303431)
    Discount_rate = 0.1
    def __init__(self, name, price, count, made, factory):
        self.name_pro = name
        self.price_pro = price
        self.count = count
        self.country = made
        self.factory_name = factory

        MedadRangi.welcome()

    def final_price(self):
        return self.price_pro*self.count*(1-MedadRangi.Discount_rate)

    @staticmethod
    def welcome():
        if 6 < datetime.datetime.now().hour <= 11:
            print("GOOD MORNING")

        else:
            print("GOOD AFTERNOON")


    def claculate_distance(self, x, y):
        distance = ((x - self.x)**2 + (y-self.y)**2)**(1/2)
        return distance

    def load_csv(self, name_file):
        dict_property_product = {}
        with open(name_file + '.txt') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=':')

            for i in list(csv_reader):
                dict_property_product[i[0]] = i[1]
            print(dict_property_product)
            MedadRangi(**dict_property_product)

#-------------------------------------------------------

import unittest
class Test_Medad(unittest.TestCase):
    def test_create_instans1(self):
        name, price, count, made, factory = 'Pen', 2000, 5, 'Italy', 'lian'
        medad_rangi = MedadRangi(name, price, count, made, factory)
        self.assertEqual(('Pen'), medad_rangi.name_pro)
        self.assertEqual(2000 ,medad_rangi.price_pro)
        self.assertEqual(5, medad_rangi.count)
        self.assertEqual('Italy', medad_rangi.country)
        self.assertEqual('lian', medad_rangi.factory_name)

    def test_final_price(self):
        name = "pen"
        price = 5000
        count = 5
        country = "France"
        factory_name = "bic"
        medadrangi = MedadRangi(name,price,count,country,factory_name)
        self.assertEqual(Decimal("22500.0"),medadrangi.final_price())

    def test_calculate_distance(self):
        name = 'Pencil'
        price = 3000
        count = 7
        country = 'Iran'
        factory = 'kian'
        medad = MedadRangi(name ,price ,count ,country,factory)
        self.assertEqual(17.890388459546173, medad.claculate_distance(60, 20))

if __name__ == '__main__':
    unittest.main()
