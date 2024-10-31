# def daraja(n):
#     return lambda x:x**n

# kvadrat = daraja(2)
# kub = daraja(3)
# print(kvadrat(5))


# from math import sqrt

# sonlar = list(range(1,11))
# # ildizlar = list(map(sqrt, sonlar))

# a = [2,4,5]
# b = [4,1,7]

# qoshilma = list(map(lambda x,y:x+y,a,b))

# kvadratlar = list(map(lambda x:x*x, sonlar))
# print(qoshilma)



# import random as r

# sonlar = r.sample(range(100),10)
# # print(sonlar)

# def juftmi(x):
#     return x%2 == 0
# # print(juftmi(2))

# # saralangan_sonlar = list(filter(juftmi, sonlar))
# # print(saralangan_sonlar)

# saralangan_sonlar = list(filter(lambda x:x%2==0, sonlar))
# print(saralangan_sonlar)




# mevalar = ['olma','banan']

# sara = list(filter(lambda x:x.startswith('o') and x.endswith('a'),mevalar))
# print(sara)
# print('sobirjon'.startswith('q'))