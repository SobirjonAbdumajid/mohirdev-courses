my_input = ['d', 't', 'a','g', 'q', 'i', 'i']
variable = 'a'

for i, value in enumerate(my_input):
    if value == variable:
        my_input.remove(my_input[i])
    print(my_input[i])
    
print(my_input)