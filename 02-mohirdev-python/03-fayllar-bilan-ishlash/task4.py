name = 'info_users'

saver = []


with open(name, 'a') as file:
    while True:
        info = input('write your info. if you wanna stop just click enter: ')
        if not info:break
            
        saver.append(info+'\n')
        
    for i in saver:
        file.write(i)
        
# sett = {1,2,2,2}
# tuplee = (1,2,2,2)
# print(sett)
# print(tuplee)