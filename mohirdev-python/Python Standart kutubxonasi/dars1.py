# # # import datetime as dt

# # # hozir = dt.datetime.now()
# # # print(hozir.date())

# # import re

# # email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

# # # Email manzillarni tekshirish uchun namuna

# # matn = 'Email manzillarni tekshirish x@example.com uchun namuna'
# # emails = ["example@example.com", "user.name+tag+sorting@example.com", "x@example.com", "example-indeed@strange-example.com", "admin@mailserver1", "example@s.solutions"]

# # print(re.findall(email_regex, matn))

# # # for email in emails:
# # #     if re.match(email_regex, email):
# # #         print(f"{email}: To'g'ri")
# # #     else:
# # #         print(f"{email}: Xato")


# import re

# password_regex = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]{8,}$'

# # Parolni tekshirish uchun namuna
# passwords = ["Password123!", "pass123", "PASSWORD!@#", "Passw0rd", "Pa$$w0rd"]

# for password in passwords:
#     if re.match(password_regex, password):
#         print(f"{password}: To'g'ri")
#     else:
#         print(f"{password}: Xato")


# import datetime as dt

# today = dt.date.today()
# tYil = dt.date(2005, 3, 5)

# somsa = today - tYil
# vaqt = somsa.strftime("%Y:%H:%M:%S")
# # sana = somsa.strftime("%d-%m-%Y")
# print(vaqt)




# import datetime as dt
# from dateutil.relativedelta import relativedelta

# def hisobla(tugilgan_kun):
#     today = dt.date.today()
#     fark = relativedelta(today, tugilgan_kun)
#     return fark.years, fark.months, fark.days

# tugilgan_kun = dt.date(2005, 3, 5)
# yil, oy, kun = hisobla(tugilgan_kun)

# print(f"Tug'ilgan kundan beri o'tgan vaqt: {yil} yil, {oy} oy, {kun} kun.")




# bugun = dt.date.today()
# qurbonHayit = dt.date(2021, 7, 19)
# farq = qurbonHayit-bugun
# print(farq)
# print(f"Qurbon Hayitiga {farq.days} kun qoldi")



# import datetime as dt

# def tYilFarqniAniqla(tugilgan_kun):
#     today = dt.date.today()
#     yil_farqi, oy_farqi, kun_farqi = today.year - tugilgan_kun.year, today.month - tugilgan_kun.month, today.day - tugilgan_kun.day
#     return yil_farqi, oy_farqi, kun_farqi


# tugilgan_kun = dt.date(2005, 3, 5)

# yil, oy, kun = tYilFarqniAniqla(tugilgan_kun)

# print(f"Tug'ilgan kundan beri o'tgan vaqt: {yil} yil, {oy} oy, {kun} kun.")
