from random import randint


def get_description():
    return 'brain-even\n'


def get_annotation():
    return 'Answer "yes" if the number is even, otherwise answer "no"'


def game_logic():
    number1 = randint(1, 20)
    if number1 % 2 == 0:
        question = f'Question: {number1}'
        right_answer = 'yes'
        return right_answer, question
    else:
        question = f'Question: {number1}'
        right_answer = 'no'
        return right_answer, question
