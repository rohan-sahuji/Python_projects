# Random Password generator

import string
import random

def gen_pass():
    character = list(string.ascii_letters + '!§$%&#^()@' + string.digits)
    random.shuffle(character)

    print('Do you want to generate a random password?')
    ans = input('Y/N:')

    if ans.lower() == 'y':
        length = int(input('Enter number of characters:'))
        password = []
        while len(password) != length:
            password.append(random.choice(character))

        random.shuffle(password)
        password="".join(password)
        print(password)
    elif ans.lower() == 'n':
        quit()
    else:
        print('Invalid Response!')

gen_pass()