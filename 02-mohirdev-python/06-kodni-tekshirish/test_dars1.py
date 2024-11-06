import unittest
from dars1 import toliq_ism

class Test_qilish(unittest.TestCase):
    def test_ism(self):
        name = toliq_ism('sobirjon', 'abdumajidov', 'akmal')
        self.assertEqual(name, 'Sobirjon Abdumajidov Akmal')
    def test_ism_familiya(self):
        nameism = toliq_ism('sobirjon', 'abdumajidov')
        self.assertEqual(nameism, 'Sobirjon Abdumajidov')

unittest.main()