# Rock, Paper, Scissors

import random

elements = ['Rock','Paper','Scissor']
user_score = 0
comp_score = 0
user_wins = [('Rock','Scissor'),('Paper','Rock'),('Scissor','Paper')]
exit = False
while True:
    comp_value = random.choice(elements)
    print("")
    print('''Select one of following:
        R: Rock
        P: Paper
        S: Scissor
        E: Exit
        ''')
    user_input = input('Enter R, P, S or E: ')
    if user_input.lower() == 'r':
        user_value = elements[0]
    elif user_input.lower() =='p':
        user_value = elements[1]
    elif user_input.lower() == 's':
        user_value = elements[2]
    elif user_input.lower() == 'e':
        print('Final Score:')
        print('You:',user_score, 'Computer:',comp_score)
        quit()
    else:
        print('Incorrect input!')

    judge_tuple = (user_value,comp_value)
    print('You selected',user_value, 'and Computer selected', comp_value)
    if user_value == comp_value:
        print('It is a tie! Score:')
        print('You:', user_score, 'Computer:', comp_score)
    else:
        if judge_tuple in user_wins:
            print ('You won! Score:')
            user_score += 1
            print('You:', user_score, 'Computer:', comp_score)
        else:
            print ('Computer wins. Score:')
            comp_score += 1
            print('You:', user_score, 'Computer:', comp_score)