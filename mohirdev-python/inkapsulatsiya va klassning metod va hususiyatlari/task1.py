'''
Avvalgi darslarimizda yaratgan Shaxs va Talaba klasslariga yopiq xususiyatlar qo'shing va ularning qiymatini ko'rsatuvchi va o'zgartiruvchi metodlar yozing.
Yuqoridagi klasslarga talabalar_soni va odamlar_soni degan klassga oid xususiyatlar qo'shing.
Klassga oid xususiyatlar bilan ishlash uchun maxsus @classmethod lar yozing
'''

class Shaxs:
    __num_shaxs = 0
    def __init__(self, ism, familiya, passport, tyil):
        self.ism = ism
        self.__familiya = familiya
        self.passport = passport
        self.tyil = tyil
        Shaxs.__num_shaxs += 1

    def get_age(self, current_year):
        return current_year - self.tyil
    
    def get_name(self):
        return self.ism
    
    def get_familiya(self):
        return self.__familiya

    def get_passport(self):
        return self.passport
    
    def get_info(self):
        info = f'{self.ism} {self.__familiya} passport: {self.passport}, tog\'lgan yili {self.tyil}' # bu ma'lumot qoniqtirmadi va uni voris classga ham yozdik: va bu polimorfizm deb aytiladi. ya'ni bir method qayta yozilsa
        return info
    
    def change_tyil(self, new_familiya):
        self.__familiya = new_familiya
    

    
    @classmethod
    def getNum_shaxs(cls):
        return cls.__num_shaxs
    
shaxs1 = Shaxs('Sobirjon', 'Abdumajidov', 'AD200555', 2005)
shaxs1 = Shaxs('Sobirjon', 'Abdumajidov', 'AD200555', 2005)
    
print(shaxs1.getNum_shaxs())

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



class Talaba(Shaxs):
    __talaba_soni = 0
    def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
        Talaba.__talaba_soni += 1

    def get_id(self):
        return self.idraqam
    
    def get_bosqich(self):
        return self.bosqich
    
    def get_info(self):
        info = f'{self.ism} {self.familiya} {self.bosqich} - bosqich talabasi. id raqam: {self.idraqam} passport: {self.passport}, tog\'lgan yili {self.tyil}' # tepadagi ma'lumot qoniqtirmadi va uni super (shu) classga ham yozdik: va bu polimorfizm deb aytiladi. ya'ni bir method qayta yozilsa
        return info
    
    @classmethod
    def get_talaba_soni(cls):
        return cls.__talaba_soni
    
talaba1 = Talaba('Sardorbek', 'Odiljonov', 'DA555462', 2002, 12331, talaba1_manzil)
talaba1 = Talaba('Sardorbek', 'Odiljonov', 'DA555462', 2002, 12331, talaba1_manzil)
talaba1 = Talaba('Sardorbek', 'Odiljonov', 'DA555462', 2002, 12331, talaba1_manzil)
talaba1 = Talaba('Sardorbek', 'Odiljonov', 'DA555462', 2002, 12331, talaba1_manzil)


print(Talaba.get_talaba_soni())

# print(talaba1.manzil.get_manzil())


    



# print(talaba1.get_info())