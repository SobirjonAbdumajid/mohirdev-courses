# # def katta(n1,n2,n3):
# #     return max(n1,n2,n3)
# # print(katta(2,6,1))
    

# # def matn_royhat(*matnlar):
# #     return [matn.title() for matn in matnlar]

# # print(matn_royhat('sobirjon', 'abdumajidov'))



# # def royhat_sonlar(*sonlar: int):
# #     return [son for son in sonlar if son % 2 != 0]

# # print(royhat_sonlar(1,2,3,4))


# # def fibanachi_top(fibanachi):
# #     if fibanachi < 0:
# #         return False
    
# #     fib1, fib2 = 0, 1
# #     while fib1 <= fibanachi:
# #         if fib1 == fibanachi:
# #             return True
# #         fib1, fib2 = fib2, fib1 + fib2
# #     return False

# # print(fibanachi_top(22))


# class Car:
#     """(self,make,model,year,km=0,price=None)"""

#     def __init__(self, make, model, year, km=0, price=None):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.price = price
#         self.__km = km

#     def set_price(self, price):
#         self.price = price

#     def add_km(self, km):
#         """Mashinaning km ga yana km qo'shish"""
#         if km >= 0:
#             self.__km += km
#         else:
#             raise ValueError("km manfiy bo'lishi mumkin emas")

#     def get_info(self):
#         info = f"{self.make.upper()} {self.model.title()}, "
#         info += f"{self.year}-yil, {self.__km}km yurgan."
#         if self.price:
#             info += f" Narhi: {self.price}"
#         return info

#     def get_km(self):
#         return self.__km


class Shaxs:
    """Shaxslar haqida ma'lumot"""

    def __init__(self, ism, familiya, passport, tyil):
        """Shaxsning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil

    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info

    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil


class Talaba(Shaxs):
    """Talaba klassi"""

    def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil

    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam

    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich

    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info