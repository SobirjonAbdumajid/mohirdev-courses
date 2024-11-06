'''
# AMALIYOT
- Bugun o'rgangan narsalaringizni matnga yozing va matnni Python yordamida oching
- Quyidagi [pi_million_digits.txt](https://firebasestorage.googleapis.com/v0/b/gitbook-28427.appspot.com/o/assets%2F-MGbkqs1tROquIT6oqUs%2F-MTFShfF-96YP2YMtAFf%2F-MTFmSDSeDIeZAOhX9Yk%2Fpi_million_digits.txt?alt=media&token=224f0425-0448-469d-bc93-dff2f6e5c178) faylini yuklab oling (faylda $\pi$ soni nuqtadan so'ng million xona aniqlik bilan yozilgan). 
- Sizning tug'ilgan kuningiz $\pi$ soni tarkibida uchraydimi yoki yo'q ekanligini aniqlovchi funksiya yozing. Misol uchun, tug'ilgan sanangiz 25 Fevral, 2000-yil bo'lsa, `25022000` ketma-ketligi yuqoridagi matnda uchraydimi yo'q toping.
- Fayl ichidagi matnni float ma'lumot turiga o'tkazing va pickle yordamida yangi faylga saqlang.
- Foydalanuvchidan turli hil ma'lumotlarni so'rab, har bir kiritilgan ma'lumotni yangi qatordan faylga yozib boruvchi dastur tuzing. Dastur qayta chaqirilganida yangi ma'lumotlar fayl oxiridan qo'shilib borsin (yangi faylga emas).
'''

def find_brithday_in_pi(brithday):
    with open('pi_million_digits.txt') as file:
        ozgaruvchi = file.read()
        ozgaruvchi = ozgaruvchi.rstrip()
        ozgaruvchi = ozgaruvchi.replace('\n', '')
        ozgaruvchi = ozgaruvchi.replace('  ', '')
        ozgaruvchi = ozgaruvchi.replace(' ', '')
        return brithday in ozgaruvchi

brithday = '352005'

if find_brithday_in_pi(brithday):
    print(f'{brithday} have found in the txt file')
else:
    print(f'{brithday} have not found in the txt file')