# my_input = ['d', 't', 'a','g', 'q', 'i', 'i']
# variable = 'a'

# for i, value in enumerate(my_input):
#     if value == variable:
#         my_input.remove(my_input[i])
#     print(my_input[i])
    
# print(my_input)


# --------------------

my_list = ['d', 't', 'ag', 'g', 4,'d', 'a']
big_list = []

for i in range(0, len(my_list)-1, 2):
    big_list.append([my_list[i], my_list[i+1]])
             
if len(my_list)%2==1:
    big_list.append([my_list[-1]])

print(big_list)




# my_list = ['d', 't', 'ag', 'g']
# big_list = []

# # Iterate through the list in steps of 2
# for i in range(0, len(my_list), 2):
#     # If the next element exists, pair the current and next element
#     if i + 1 < len(my_list):
#         big_list.append([my_list[i], my_list[i + 1]])
#     else:
#         big_list.append([my_list[i]])

# print(big_list)


# first_word = "afds, new_order.address".split(',')[0].strip()
# print

    # get_order_price(first_word)