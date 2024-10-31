# # import unittest
# # from task1 import fibanachi_top

# # class Testla(unittest.TestCase):
# #     # def test_katta(self):
# #     #     self.assertIs(katta(3,5,5), 5)
# #     # def test_kattaHarf(self):
# #     #     self.assertEqual(matn_royhat('sobirjon', 'abdumajidov'), ['Sobirjon', 'Abdumajidov'])
# #     def test_toqson(self):
# #         self.assertEqual(fibanachi_top(21), True)
# #         self.assertEqual(fibanachi_top(22), False)

# # unittest.main()


# import unittest
# from task1 import Car

# class CarTest(unittest.TestCase):
#     def setUp(self):
#         make = "GM"
#         self.model = "Malibu"
#         year = 2020
#         self.price = 40000
#         self.km = 10000
#         self.avto1 = Car(make, self.model, year)
#         self.avto2 = Car(make, self.model, year, price=self.price)

#     def test_create(self):
#         self.assertIsNotNone(self.avto1.make)
#         self.assertIsNotNone(self.avto1.model)
#         self.assertEqual(self.model, self.avto1.model)
#         self.assertIsNotNone(self.avto1.year)
#         # Qiymat mavjud emasligini assertIsNone metodi bilan tekshiramiz
#         self.assertIsNone(self.avto1.price)
#         # Qiymat tengligini assertEquals metodi bilan tekshiramiz
#         self.assertEqual(0, self.avto1.get_km())
#         # avto2 narhini tekshiramiz
#         self.assertEqual(self.price, self.avto2.price)

#     def test_set_price(self):
#         new_price = 45000
#         self.avto2.set_price(new_price)
#         self.assertEqual(new_price, self.avto2.price)

#     def test_add_km(self):
#         # 1 Musbat qiymat berib ko'ramiz
#         self.avto1.add_km(self.km)
#         self.assertEqual(self.km, self.avto1.get_km())
#         self.avto1.add_km(5000)
#         self.assertEqual(15000, self.avto1.get_km())
#         # 2 Manfiy qiymat berib ko'ramiz
#         new_km = -5000
#         try:
#             self.avto1.add_km(new_km)
#         except ValueError as error:
#             self.assertEqual(type(error), ValueError)
# unittest.main()

import unittest
from task1 import Shaxs, Talaba

class CarTest(unittest.TestCase):
    def setUp(self):
        self.ism = 'Sobirjon'
        self.familiya = 'Abdumajidov'
        self.passport = 'passport'
        self.tyil = 2005
        # for class Talaba
        self.idraqam = 12
        self.manzil = 'manzil'
        self.shaxs1 = Shaxs(self.ism, self.familiya, self.passport, self.tyil)
        self.talaba1 = Talaba(self.ism, self.familiya, self.passport, self.tyil, self.idraqam, self.manzil)

    def test_shaxsh(self):
        self.assertIsNotNone(self.shaxs1.ism)
        self.assertIsNotNone(self.shaxs1.familiya)
        self.assertIsNotNone(self.shaxs1.passport)
        self.assertIsNotNone(self.shaxs1.tyil)
        self.assertEqual(self.tyil, self.shaxs1.tyil)

    def test_get_age(self):
        c_year = 2024
        self.assertEqual(c_year - 2005, self.shaxs1.get_age(c_year))

    def test_talaba_getId(self):
        self.assertIs(self.talaba1.idraqam, 12)

unittest.main()