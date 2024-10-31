import re

# word1 = "sobirjon"
# word2 = "sardorbek"
# word3 = "somsajon"

# andoza = "^s......n$"

# print(re.match(andoza, word1))
# print(re.match(andoza, word2))
# print(re.match(andoza, word3))




# ## Emailni ajratib olish
# matn = """Maqolalar  2020-yilning 20-martiga qadar rtmkonferensiya2021@mail.ru elektron pochtasida qabul qilinadi.
# Quyidagi yo'nalishdagi maqolalar qabul qilinadi:
# 👉 Aniq va tabiiy fanlarni zamonaviy pedagogik texnologiyalar asosida o‘qitish  metodikasi.
# 👉 Umumta’lim  fanlarini o‘qitishda  STEAM yondashuvning o’rni va ahamiyati. """

# andoza = "[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
# email = re.findall(andoza, matn)
# print(email)


# # Kuchli parolni tekshirish
# andoza = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$"
# msg = "Yangi parol kiriting"
# msg += "(kamida 8 belgidan iborat, kamida 1 ta lotin bosh harf, 1 ta kichik harf, "
# msg += "1 ta son va 1 ta maxsus belgi boʻlishi kerak): "

# while True:
#     password = input(msg)
#     if re.match(andoza, password):
#         print("Maxfiy so'z qabul qilindi")
#         break
#     else:
#         print("Maxfiy so'z talabga javob bermadi")


# # Telefon raqamni tekshirish
# andoza = "^\+?\d{1,3}?[-.\s]?\(?\d{1,4}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}$"
# msg = "Telefon raqam kiriting: "

# while True:
#     raqam = input(msg)
#     if re.match(andoza, raqam):
#         print('To\'gri!')
#         break
#     else:
#         print('Raqamingiz standartlarga to\'g\'ri kelmadi!')


# Emailni ajratib olish
matn = """
Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz YouTubega yuklandi: https://youtu.be/vsxJPRLXpgI
Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar va metodlarini tekshiruvchi dastur yozishni o'rganamiz. Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test
"""

andoza = r"https?://(?:www\.)?[\w.-]+(?:\.[\w\.-]+)+[/\w\.-]*"

webSites = re.findall(andoza, matn)
print(webSites)