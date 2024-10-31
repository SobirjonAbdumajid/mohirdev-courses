from uuid import uuid4
# from avtos import avto1
class Avto:
    """Avtomobil klassi"""
    avto_num = 0
    def __init__(self,make,model,rang,yil,narh,km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()
        Avto.avto_num += 1
    
    def get_km(self):
        return self.__km
    
    def get_id(self):
        return self.__id

    def add_km(self, km):
        if km >=0:
            self.__km+=km
        else:
            print('Mashina km kamaytirib bo\'lmaydi')

    @classmethod
    def get_numOf_avto(cls):
        return cls.avto_num
    
    # def __str__(self):
    #     return f'{self.make} {self.model}'


    def __repr__(self) -> str:
        return f'{self.make} {self.model}'
    
    def __eq__(self, value):
        return self.narh == value.narh
    
    def __lt__(self, value):
        return self.narh < value.narh
    
    def __le__(self, value):
        return self.narh <= value.narh
    
    
    # def __len__(self):
    #     return self.
    

    


avto1 = Avto('GM', 'Malibu', 'Qora', 2000, 21000, 100)
avto2 = Avto('GM', 'Spark', 'Oq', 2000, 2100, 1000)
# print(isinstance(1.0, int))
# print(avto1<=avto2)

# print(str(avto1))


# avto1.add_km(54)

# print(avto1.get_numOf_avto())



class AvtoSalon:
    def __init__(self, name):
        self.name = name
        self.avtolar = []

    def __repr__(self):
        return f'{self.name}'

    def __getitem__(self, index):
        return self.avtolar[index]
    
    def __setitem__(self, index, qiymat):
        self.avtolar[index] = qiymat
    
    def add_avto(self, *qiymat):
        for avto in qiymat:
            if isinstance(avto, Avto):
                self.avtolar.append(avto)
            else:
                print('Avto kiriting')

salon1 = AvtoSalon('Sobirjon_AvtoSalon')

salon1.add_avto(avto1, avto2)
salon1[0] = Avto('BMW', 'x7', 'Oq', 1990, 21000, 30000)

print(salon1[:])
    