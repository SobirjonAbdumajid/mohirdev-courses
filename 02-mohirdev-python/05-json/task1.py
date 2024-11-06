import json
import pickle

# # data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}

# # data_json = json.dumps(data, indent=4)
# # # print(data_json)
# # # print(type(data_json))



# # talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
# # talaba_json_new = json.loads(talaba_json)
# # # print(talaba_json['ism'], '\n', talaba_json['familiya'])

# # # with open('alohida', 'wb') as f:
# # #     # json.dump(talaba_json, f)    
# # #     pickle.dump(data, f)
# # #     pickle.dump(talaba_json_new, f)

# # with open('alohida', 'rb') as f:
# #     somsa1 = pickle.load(f)
# #     somsa2 = pickle.load(f)
# # print(somsa1)
# # print(somsa2)

# # #     pickle.dump(person1, file) # saving variable
# # #     pickle.dump(person2, file)





# bemor1 = {
#     "name": "Sobir",
#     "surename": "Uroqboyev",
#     "age": 25,
#     "oila": True,
#     "kurs": 2,
#     "fakulteti": 'beologiya',
#     "farzandlar": ("ahmad", "toshmat"),
#     "arlergiyasi" : None,
#     "dorilar": [
#         {"nome": "Analgin", "miqdori": 0.5},
#         {"nome": "Alergy", "miqdori": 1.5}
#     ],
#     "city": "San Francisco",
#     "occupation": "Designer",
#     "hobbies": ["photography", "traveling", "painting"]
# }


# bemor2 = {
#     "name": "Sardor",
#     "surename": "Odiljonov",
#     "age": 25,
#     "oila": True,
#     "kurs": 1,
#     "fakulteti": 'Kimyo',
#     "farzandlar": ("ahmad", "toshmat"),
#     "arlergiyasi" : None,
#     "dorilar": [
#         {"nome": "Analgin", "miqdori": 0.5},
#         {"nome": "Alergy", "miqdori": 1.5}
#     ],
#     "city": "San Francisco",
#     "occupation": "Designer",
#     "hobbies": ["photography", "traveling", "painting"]
# }


# bemor3 = {
#     "name": "Bobjon",
#     "surename": "Bobov",
#     "age": 250,
#     "oila": True,
#     "kurs": 1,
#     "fakulteti": 'IT',
#     "farzandlar": ("ahmad", "sardor"),
#     "arlergiyasi" : None,
#     "dorilar": [
#         {"nome": "parasetamol", "miqdori": 0.5},
#         {"nome": "yodamarin", "miqdori": 1.5}
#     ],
#     "city": "San Francisco",
#     "occupation": "Designer",
#     "hobbies": ["photography", "traveling", "painting"]
# }




# # with open('bemorjon', 'wb') as f:
# #     pickle.dump(bemor1, f)
# #     pickle.dump(bemor2, f)
# #     pickle.dump(bemor3, f)

    
# with open('bemorjon', 'rb') as f:
#     somsacha1 = pickle.load(f)
#     somsacha2 = pickle.load(f)
#     somsacha3 = pickle.load(f)
# print(
#     "ism - ", somsacha1['name'], '\n',
#     "familiyasi - ", somsacha1['surename'], '\n',
#     "fakulteti - ", somsacha1['fakulteti'], '\n',
#     "kurs - ", somsacha1['kurs'], '\n',

#     "ism - ", somsacha2['name'], '\n',
#     "familiyasi - ", somsacha2['surename'], '\n',
#     "fakulteti - ", somsacha2['fakulteti'], '\n',
#     "kurs - ", somsacha2['kurs'], '\n',

#     "ism - ", somsacha3['name'], '\n',
#     "familiyasi - ", somsacha3['surename'], '\n',
#     "fakulteti - ", somsacha3['fakulteti'], '\n',
#     "kurs - ", somsacha3['kurs'], '\n',
    
# )

# # print(somsacha2)
# # print(somsacha3)


# with open('api-result.json', 'rb') as f:
#     zor = f.read()

with open('api-result.json') as f:
    zor_dict = json.load(f)

print(
    'title - ', zor_dict['query']['pages']['13801']['title'], '\n',
    'extract - ', zor_dict['query']['pages']['13801']['extract'], 
)
# print(
#     'title - ', zor_dict['title'],
#     'extract - ', zor_dict['extract'],
# )