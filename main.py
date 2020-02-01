
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

def get_num(difficulty, type='linear'):
    if difficulty == 1:
        return np.random.randint(2, 10)
    elif type=='linear':
        return np.random.randint((difficulty + 1), (difficulty * 10))
    elif type=='log':
        return np.random.randint((difficulty + 1), (difficulty * 3)**2)

def get_operator():
    err_msg = 'Please select an integer between 1 and 7 in the following list! Try again:'
    operator = get_int('Choose from the following math operations:\n1. addition\n2. subtraction\n3. multiplication\n4. division\n5. floor division\n6. modulus\n7. exponentiation\nYou choose? ', err_msg)
    if (operator >= 1) & (operator <= 7):
        return operator
    else:
        print(err_msg)
        get_operator()

def math_questions():
    operator = get_operator()
    question_count = get_question_count()
    difficulty = get_difficulty()

    q = []
    correct_count = 0
    for i in range(question_count):
        x = get_num(difficulty)
        y = get_num(difficulty)

        if operator == 1:
            x = get_num(difficulty, type='log')
            y = get_num(difficulty, type='log')
            question_string = str(x) + ' + ' + str(y) + ' = '
            answer = get_int(question_string)
            correct = answer == x + y
        if operator == 2:
            x = get_num(difficulty, type='log')
            y = get_num(difficulty, type='log')
            if x < y: x, y = y, x
            question_string = str(x) + ' - ' + str(y) + ' = '
            answer = get_int(question_string)
            correct = answer == x - y
        if operator == 3:
            question_string = str(x) + ' * ' + str(y) + ' = '
            answer = get_int(question_string)
            correct = answer == x * y
        if operator == 4:
            z = x * y
            question_string = str(z) + ' / ' + str(y) + ' = '
            answer = get_int(question_string)
            correct = answer == z / y
        if operator == 5:
            if x < y: x, y = y, x
            question_string = str(x) + ' // ' + str(y) + ' = '
            answer = get_int(question_string)
            correct = answer == x // y
        if operator == 6:
            if x < y: x, y = y, x
            question_string = str(x) + ' % ' + str(y) + ' = '
            answer = get_int(question_string)
            correct = answer == x % y
        if operator == 7:
            y = 2
            question_string = str(x) + ' ** ' + str(y) + ' = '
            answer = get_int(question_string)
            correct = answer == x ** y
        
        q.append([x, y, answer, correct])

        if correct:
            correct_count += 1
            print('Correct! {}/{}\n'.format(correct_count, i+1))
        else:
            print('Incorrect! {}/{}\n'.format(correct_count, i+1))

    for i in q:
        print(i)

def main():
    math_questions()

if __name__ == '__main__':
    main()
