'''
# AMALIYOT

- `Avto` degan yangi klass yarating. Unga avtomobillarga doir bo'lgan bir nechta xususiyatlar (model, rang, korobka, narh va hokazo) qo'shing. Ayrim xususiyatlarga standart qiymat bering (masalan, `kilometer=0`)
- `Avto` ga oid obyektning xususiyatlarini qaytaradigan metodlar yozing
    + `get_info()` metodi avto haqida to'liq ma'lumotni matn ko'rinishida qaytarsin
- `Avto` ga oid obyektning xususiyatlarini yangilaydigan metodlar yozing.
    + `update_km()` metodi son qabul qilib olib, avtomobilning yurgan kilometrajini yangilab borsin
- Yangi, `Avtosalon` degan klass yarating va kerakli xususiyatlar bilan to'ldiring (salon nomi, manzili, sotuvdagi avtomobillar va hokazo)
- Avtosalonga yangi avtomobillar qo'shish uchun metod yozing
- Avtosalondagi avtomobillar haqida ma'lumot qaytaruvchi metod yozing
- Yuqoridagi obyektlar va ularga tegishli metodlarni tekshirib ko'ring
- `dir()` funksyasi va `__dict__` metodi yordamida o'zingiz yozgan va Pythondagi turli klass va obyektlarning xususiyatlari va metodlarini toping (`dir(str)`, `dir(int)` va hokazo)
'''

class Avto:
    def __init__(self, model, rang, narh):
        self.model = model
        self.rang = rang
        self.narh = narh
        self.kilometir = 0
        

    def get_model(self):
        return self.model
    
    def get_rang(self):
        return self.narh
    
    def get_narh(self):
        return self.narh
    
    def get_info(self):
        return f'{self.kilometir} yurgan {self.rang} rangli {self.model}ning narhi {self.narh}$'
    
    def update_km(self, new_km):
        self.kilometir = new_km
        return self.kilometir
    
avtomabil1 = Avto('malibu', 'qora', 22000)
avtomabil2 = Avto('spark', 'oq', 10000)

avtomabil1.update_km(1000)



class Avtosalon:
    def __init__(self, salon_nomi, manzili):
        self.salon_nomi = salon_nomi
        self.manzili = manzili
        self.sotuvdagi_avtomobillar = []

    def add_avtos(self, avtos):
        self.sotuvdagi_avtomobillar.append(avtos)

    def give_avtos(self):
        return [avtos.get_info() for avtos in self.sotuvdagi_avtomobillar]
    
    def see_methods(self):
        return [methods for methods in dir(Avtosalon) if not methods.startswith('__')]
    
avtosalon1 = Avtosalon('gm', 'toshkent')

avtosalon1.add_avtos(avtomabil1)
avtosalon1.add_avtos(avtomabil2)

print(avtosalon1.give_avtos())


print(avtosalon1.see_methods())

print(avtomabil1.__dict__)
print(avtomabil1.__dict__.keys())
print(avtomabil1.__dict__.values())
print(dir(str))
print(dir(int))