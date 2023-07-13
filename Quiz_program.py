# A program for quiz game

quiz = {
    'Question1' : {
        'question':'What is the capital of India',
        'answer':'delhi'
    },
    'Question2' : {
        'question':'What is the capital of Germany',
        'answer':'berlin'
    },
    'Question3' : {
        'question':'What is the capital of France',
        'answer':'paris'
    },
    'Question4' : {
        'question':'What is the capital of Switzerland',
        'answer':'zurich'
    },
    'Question5' : {
        'question':'What is the capital of Austria',
        'answer':'vienna'
    },
    'Question6' : {
        'question':'What is the capital of Poland',
        'answer':'warsaw'
    },
    'Question7' : {
        'question':'What is the capital of Russia',
        'answer':'moscow'
    },
    'Question8' : {
        'question':'What is the capital of Italy',
        'answer':'rome'
    },
    'Question9' : {
        'question':'What is the capital of Spain',
        'answer':'barcelona'
    },
    'Question10' : {
        'question':'What is the capital of Portugal',
        'answer':'lisbon'
    }
}
score = 0
for key, value in quiz.items():
    print(key,':\n',value['question'])
    answer = input('Answer: ')
    if answer.lower() == value['answer']:
        score += 1
        print('Correct! Score:',score,'\n')
    else:
        print('Wrong! The correct answer is: ',value['answer'], 'Score: ',score,'\n')

print('\n','Your final score is ', score, 'out of 10\n')