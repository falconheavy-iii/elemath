
import math
import numpy as np


def get_int(question_string, err_msg='Please answer with an integer! Try again:'):
    try:
        return int(input(question_string))
    except:
        print(err_msg)
        return get_int(question_string, err_msg)

def get_difficulty():
    err_msg = 'Please select an integer between 1 and 5! Try again:'
    difficulty = get_int('From 1 to 5, 1 being easiest and 5 being hardest, which level of difficulty would you choose? ', err_msg)
    if (difficulty >= 1) & (difficulty <= 5):
        return difficulty
    else:
        print(err_msg)
        get_difficulty()

def get_question_count(c=30):
    err_msg = 'Please select an integer between 1 and ' + str(c) + '! Try again:'
    question_count = get_int('How many questions would you like to answer? choose between 1 and ' + str(c) + '? ', err_msg)
    if question_count <= c:
        return question_count
    else:
        print(err_msg)
        get_question_count(c)

# def get_num(difficulty):
#     if difficulty > 2:
#         num = ''
#         for i in range(np.random.randint(math.ceil((difficulty)/2), difficulty+1)):
#             num += str(np.random.randint(10))
#         return int(num)
#     elif difficulty == 1:
#         return np.random.randint(5, 20)
#     else:
#         return np.random.randint(3, 15)

def get_num(difficulty):
    return np.random.randint((difficulty)**2, (difficulty+1)**3)

def additions():
    difficulty = get_difficulty()
    question_count = get_question_count()
    
    q = []
    correct_count = 0
    for i in range(question_count):
        x = get_num(difficulty)
        y = get_num(difficulty)
        question_string = str(x) + ' + ' + str(y) + ' = '
        answer = get_int(question_string)
        q.append([x, y, answer, x + y == answer])
        if answer == x + y:
            correct_count += 1
            print('Correct! {}/{}\n'.format(correct_count, i+1))
        else:
            print('Incorrect! {}/{}\n'.format(correct_count, i+1))

    for i in q:
        print(i)

def main():
    additions()

if __name__ == '__main__':
    main()
