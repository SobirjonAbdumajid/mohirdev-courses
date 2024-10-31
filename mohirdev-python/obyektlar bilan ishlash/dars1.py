class Talaba:
    def __init__(self, ism, familiya, yosh):
        self.ism = ism
        self.familiya = familiya
        self.yosh = yosh
         
    def get_name(self):
        return self.ism

    def update_age(self, yangi_yosh):
        self.yosh = yangi_yosh
        
    def get_info(self):
        return self.ism, self.familiya, self.yosh


talaba1 = Talaba('sobirjon','abdumajidov',12)
# print(talaba1.get_name())
talaba2 = Talaba('sardorbek', 'odiljovon', 2002)
talaba1.update_age(19)
# print(talaba1.get_info())


class Fan:
    def __init__(self, fan):
        self.fan = fan
        self.talaba_soni = 0
        self.talabalar = []

    def add_student(self, student):
        self.talabalar.append(student)
        self.talaba_soni=+1

    def get_name(self):
        return self.fan
    
    def get_talaba_soni(self):
        return self.talaba_soni
    
    def get_talabalar(self):
        # talabalar = []
        # for talaba in self.talabalar:
        #     talabalar.append(talaba.get_name())
        # return talabalar
        return [talaba.get_name() for talaba in self.talabalar]
    
    def get_methods(self, class_name):
        return [methods for methods in dir(class_name) if not methods.startswith('__')]
    
it = Fan('IT')

it.add_student(talaba1)
it.add_student(talaba2)

# print(it.get_talabalar())
# print(it.get_methods(Talaba))
print(it.get_methods(talaba1))

# print(talaba1.__dict__)
# print(talaba1.__dict__.keys())
# print(talaba1.__dict__.values())

    



        

# fan = {'somsa':'zor', 'somsa':'zor','somss':'zor'}
# fan=  ('somsa','somsa','so')
# print(fan.get('somsak', 's'))

# class Somsa:
#     goshtlik = 8000
#     __kartoshkalik = 5000

#     def getter(self):
#         return self.__kartoshkalik

#     def setter(self, yangi_narx):
#         self.__kartoshkalik = yangi_narx
#         return self.__kartoshkalik
    
#     def __hello(self):
#         return 'hello world'
#     def getfunc(self):
#         return self.__hello()
    

# somsajon = Somsa()
# print(somsajon.getfunc())
# print(somsajon.setter(6000))

# import math
# class plimorfizm:
#     def __init__(self, name):
#         self.name = name
#     def yuzi(self):
#         pass

# class Doira(plimorfizm):
#     def __init__(self, radius):
#         super().__init__(radius)
#         self.radius = radius

#     def yuzi(self):
#         return self.radius * math.pi *2
#     def __str__(self):
#         return f'{self.yuzi()}'
    

# obj = Doira(4)

# print(obj)




    # def __init__(self, radius):
    #     super().__init__('somsa')
    

# sal = 'zor' # does not work
# sal[1] = 'p'
# print(sal[1])


