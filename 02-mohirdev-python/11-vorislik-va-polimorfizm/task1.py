'''
# AMALIYOT
- `Talaba` klassiga yana bir, `fanlar` degan xususiyat qo'shing. Bu xususiyat parametr sifatida uzatilmasin va obyekt yaratilganida bo'sh ro'yxatdan iborat bo'lsin (`self.fanlar=[]`)
- `Fan` degan yangi klass yarating va bu klassdan turli fanlar uchun alohida obyektlar yarating.
- Talaba klassiga `fanga_yozil()` degan yangi metod yozing. Bu metod parametr sifatida `Fan` klassiga tegishli obyektlarni qabul qilib olsin va talabaning fanlar ro'yxatiga qo'shib qo'ysin.
- Talabaning fanlari ro'yxatidan biror fanni o'chirib tashlash uchun `remove_fan()` metodini yozing. Agar bu metodga ro'yxatda yo'q fan uzatilsa `"Siz bu fanga yozilmagansiz"` xabarini qaytarsin.
- Yuqoridagi `Shaxs` klassidan boshqa turli voris klasslar yaratib ko'ring (masalan `Professor`, `Foydalanuvchi`, `Sotuvchi`, `Mijoz` va hokazo)
- Har bir klassga o'ziga hoz xususiyatlar va metodlar yuklang.
- Barcha yangi klasslar uchun `get_info()` metodini qayta yozib chiqing.
- Voris klasslardan yana boshqa voris klass yaratib ko'ring. Misol uchun `Foydalanuvchi` klassidan `Admin` klassini yarating. 
- `Admin` klassiga foydalanuvchida yo'q yangi metodlar yozing, masalan, `ban_user()` metodi konsolga `"Foydalanuvchi bloklandi"` degan matn chiqarsin.
'''

class Shaxs:
    def __init__(self, ism, familiya, passport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil

    def get_age(self, current_year):
        return current_year - self.tyil
    
    def get_name(self):
        return self.ism
    
    def get_familiya(self):
        return self.familiya

    def get_passport(self):
        return self.passport
    
    def get_info(self): # polimorfizm 43 33
        info = f'{self.ism} {self.familiya} passport: {self.passport}, tog\'lgan yili {self.tyil}' # bu ma'lumot qoniqtirmadi va uni voris classga ham yozdik: va bu polimorfizm deb aytiladi. ya'ni bir method qayta yozilsa
        return info
    
    
class Foydalanuvchi(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, tkun):
        super().__init__(ism, familiya, passport, tyil)
        self.tkun = tkun

    def get_info(self): # plimorfizm 43 33
        info = f'{self.ism} {self.familiya} passport: {self.passport}, tog\'lgan yili {self.tyil}' # bu ma'lumot qoniqtirmadi va uni voris classga ham yozdik: va bu polimorfizm deb aytiladi. ya'ni bir method qayta yozilsa
        info += f'tug\'lgan kun: {self.tkun}'
        return info

class Admin(Foydalanuvchi):
    def __init__(self, ism, familiya, passport, tyil, tkun, oyligi):
        super().__init__(ism, familiya, passport, tyil, tkun)
        self.oyligi = oyligi

    def get_info(self):
        info = f'{self.ism} {self.familiya} passport: {self.passport}, tog\'lgan yili {self.tyil}' # bu ma'lumot qoniqtirmadi va uni voris classga ham yozdik: va bu polimorfizm deb aytiladi. ya'ni bir method qayta yozilsa
        info += f'tug\'lgan kun: {self.tkun} oyligi: {self.oyligi}$'
        return info
    
    def ban_user(self, user_ban):
        try:
            print('user ban bo\'ldi')
        except Exception as e:
            print('Bunday user mavjud emas', e)


shaxs1 = Shaxs('Sobirjon', 'Abdumajidov', 'AD200555', 2005)

admin = Admin('admin', 'adminov', 'ad2113', 2000, 22, 1000)
print(admin.ban_user(shaxs1.tyil))


class Manzil:
    def __init__(self, uy, kocha, tuman, viloyat):
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat


    def get_manzil(self):
        info = f'{self.viloyat} {self.tuman} '
        info += f'{self.kocha} {self.uy}-uyda taradi'
        return info

talaba1_manzil = Manzil(11, 'Temur Malik', 'Mirzo Ulug\'bek', 'Toshkent shahar')


class Fan:
    def __init__(self, fan1 = None, fan2 = None, fan3 = None):
        self.fan1 = fan1
        self.fan2 = fan2
        self.fan3 = fan3

    def get_fanlar(self):
        return f'1-fan: {self.fan1} 2-fan: {self.fan2} 3-fan: {self.fan3}'
    
    def get_fanlar_array(self):
        fanlar = [self.fan1, self.fan2, self.fan3]
        return fanlar
    
    
    
talaba1_fanlar = Fan('Programming', 'ITPM', "Mobile")


class Talaba(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
        self.fanlar = []

    def get_id(self):
        return self.idraqam
    
    def get_bosqich(self):
        return self.bosqich
    
    def get_info(self):
        info = f'{self.ism} {self.familiya} {self.bosqich} - bosqich talabasi. id raqam: {self.idraqam} passport: {self.passport}, tog\'lgan yili {self.tyil}' # tepadagi ma'lumot qoniqtirmadi va uni super (shu) classga ham yozdik: va bu polimorfizm deb aytiladi. ya'ni bir method qayta yozilsa
        return info
    
    def get_fanlar(self):
        return self.fanlar
    
    def fanga_yozil(self):
        for i in talaba1_fanlar.get_fanlar_array():
            self.fanlar.append(i)

    def remove_fan(self, fan_del):
        try:
            self.fanlar.remove(fan_del)
            print('deleted saccessfully')
        except:
            print('Siz bu fanga yozilmagansiz')
    
talaba1 = Talaba('Sardorbek', 'Odiljonov', 'DA555462', 2002, 12331, talaba1_manzil)

talaba1.fanga_yozil()
print(talaba1.remove_fan('ITPMa'))

print(talaba1.get_fanlar())


# print(talaba1.manzil.get_manzil())


    



# print(talaba1.get_info())