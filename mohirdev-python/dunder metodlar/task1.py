'''
# AMALIYOT

- Avvalga darslarda yaratilgan obyektlarga (Shaxs, Talaba) turli dunder metodlarni qo'shishni mashq qiling. 
    + Obyekt haqida ma'lumot (`__rerp__`)
    + Talabalarni bosqichi bo'yicha solishtirish (`__lt__`, `__eg__` va hokazo)
- `Fan` degan yangi klass yarating. Fan obyetklari tarkibida shu fanga yozilgan talabalarning ro'yxati saqlansin. Buning uchun Fanga `add_student()`, `__getitem__`,` __setitem__`, `__len__` kabi metodlarni qo'shing.
- Fanga qo'shish `+` operatori yordamida talaba qo'shish metodini yozing
- Minus (`-`) operatori yordamida fandan talaba olib tashlash metodini yozing (bunda talabaning passport raqami yoki ID raqami bo'yicha topib, olib tashlash mumkin)
- `Fan` obyektlarini chaqiriladigan qiling (masalan, `fizika()`, yoki `fizika(talaba1)`). Bu metodlarni o'zingiz istagandek talqin qiling.
'''

class Manzil:
    def __init__(self, uy, kocha, tuman, viloyat):
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat
        

    def __repr__(self) -> str:
        return f'{self.uy}-uy {self.viloyat}'

    def get_manzil(self):
        info = f'{self.viloyat} {self.tuman} '
        info += f'{self.kocha} {self.uy}-uyda taradi'
        return info

    def __add__(self, qiymat):
        return f'{self.kocha}' + qiymat.kocha

talaba1_manzil1 = Manzil(11, 'Temur Malik', 'Mirzo Ulug\'bek', 'Toshkent shahar')
talaba1_manzil2 = Manzil(11, 'Temur Malik2', 'Mirzo Ulug\'bek', 'Toshkent viloyat')
talaba1_manzil3 = Manzil(11, 'Temur Malik2', 'Mirzo Ulug\'bek', 'Toshkent viloyat')
print(talaba1_manzil1 + talaba1_manzil2)


class Talaba:
    def __init__(self, ism, familiya, passport, tyil, bosqich):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        self.bosqich = bosqich
        self.manzil = []

    def __lt__(self, value):
        return self.bosqich < value.bosqich
    
    def __le__(self, value):
        return self.bosqich >= value.bosqich
    
    def __len__(self):
        return len(self.manzil)

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
    
    def add_item(self, *qiymat):
        for i in qiymat:
            if isinstance(i, Manzil):
                self.manzil.append(i)
            else:
                print('Faqat talabalar uchun')

    def __getitem__(self, index):
        return self.manzil[index]
    
    def __setitem__(self, index, qiymat):
        self.manzil[index] = qiymat
        
    
talaba1 = Talaba('Sobirjon', 'Abdumajidov', 'AD200555', 2005, 1)
talaba2 = Talaba('Sardorbek', 'Odiljonov', 'AD200555', 2005, 2)
talaba3 = Talaba('Sardorbek', 'Odiljonov', 'AD200555', 2005, 2)

talaba1.add_item(talaba1_manzil1, talaba1_manzil2, talaba1_manzil3)


print(len(talaba1))

# print(talaba1 <= talaba2)

# print(shaxs1[0])