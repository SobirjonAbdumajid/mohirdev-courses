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
    
    def get_info(self):
        info = f'{self.ism} {self.familiya} passport: {self.passport}, tog\'lgan yili {self.tyil}' # bu ma'lumot qoniqtirmadi va uni voris classga ham yozdik: va bu polimorfizm deb aytiladi. ya'ni bir method qayta yozilsa
        return info
    
shaxs1 = Shaxs('Sobirjon', 'Abdumajidov', 'AD200555', 2005)
    


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
    def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil

    def get_id(self):
        return self.idraqam
    
    def get_bosqich(self):
        return self.bosqich
    
    def get_info(self):
        info = f'{self.ism} {self.familiya} {self.bosqich} - bosqich talabasi. id raqam: {self.idraqam} passport: {self.passport}, tog\'lgan yili {self.tyil}' # tepadagi ma'lumot qoniqtirmadi va uni super (shu) classga ham yozdik: va bu polimorfizm deb aytiladi. ya'ni bir method qayta yozilsa
        return info
    
talaba1 = Talaba('Sardorbek', 'Odiljonov', 'DA555462', 2002, 12331, talaba1_manzil)

print(talaba1.manzil.get_manzil())


    



# print(talaba1.get_info())