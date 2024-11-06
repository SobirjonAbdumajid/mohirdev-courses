

import pickle

with open('pi_million_digits.txt', 'r') as file:
    pi = file.read().replace('\n', '')
    main_pi = float(pi)

# with open('file_for_pi', 'wb') as file:
#     pickle.dump(main_pi, file)

with open('file_for_pi', 'rb') as file:
    pi_test = pickle.load(file)
print(pi_test)


# import pickle

# # Read the pi digits from the file, convert to float, and save using pickle
# with open('pi_million_digits.txt', 'r') as file:
#     pi_digits = file.read().replace('\n', '')
#     pi_float = float(pi_digits)

# # Save the float value using pickle
# with open('pi_float.pkl', 'wb') as pickle_file:
#     pickle.dump(pi_float, pickle_file)
