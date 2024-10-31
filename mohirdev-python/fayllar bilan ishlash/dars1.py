# file = open('file1.txt') # maslahat berilmaydigan usul
# PI = file.write('somsa1')
# print(PI)
# file.close()

# with open('file3.txt', 'r+') as file:
#     # file.write('somsa')
#     ovqat = file.read()
# print(ovqat)

# filepath = 'data/media.txt'
# with open(filepath) as file:
#     for line in file:
#         print(line)
    # file.write('somsa')

# with open(filepath) as file:
#     somsalar = file.read()
# print(somsalar)

# somsalar = somsalar.rstrip() # it can remove emty spaces
# somsalar = somsalar.replace('\n', '') # it can replace elements
# somsalar = str(somsalar)
# print(somsalar)


# with open(filepath) as file:
#     somsalar = file.readlines()
# print(somsalar)
# somsalar = [somsa.rstrip() for somsa in somsalar] # writing a tsikl in a line
# print(somsalar)

# filename = 'fan.txt'
# fan1 = 'ITPM'
# grade = 'Destiction'

# with open(filename, 'a') as file:
#     file.write(fan1+'\n')
#     file.write(grade+'\n')

import pickle

person1 = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "occupation": "Engineer",
    "hobbies": ["reading", "hiking", "coding"]
}
person2 = {
    "name": "Bob",
    "age": 25,
    "city": "San Francisco",
    "occupation": "Designer",
    "hobbies": ["photography", "traveling", "painting"]
}

# with open('info', 'wb') as file:
#     pickle.dump(person1, file) # saving variable
#     pickle.dump(person2, file)

with open('info', 'rb') as file: # rb = read binary | binary -> 0 1 counting system
    odam1 = pickle.load(file) # reading variable
    odam2 = pickle.load(file)

print(odam1)
print(odam2)