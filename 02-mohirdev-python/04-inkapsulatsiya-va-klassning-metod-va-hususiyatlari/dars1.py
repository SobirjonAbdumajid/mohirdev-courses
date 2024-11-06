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

    
# avto1.add_km(54)

# print(avto1.get_numOf_avto())