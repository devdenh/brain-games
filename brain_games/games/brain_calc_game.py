import random
from random import randint


def get_description():
    return 'brain-calc\n'


def get_annotation():
    return 'What is the result of the expression?'


def game_logic():
    operator_list = ['+', '-', '*']
    operator1 = random.choice(operator_list)
    number1 = randint(1, 20)
    number2 = randint(1, 20)
    if operator1 == '+':
        question = f'Question: {number1} + {number2}'
        right_answer = number1 + number2
        return int(right_answer), question
    elif operator1 == '-':
        question = f'Question: {number1} - {number2}'
        right_answer = number1 - number2
        return int(right_answer), question
    else:
        question = f'Question: {number1} * {number2}'
        right_answer = number1 * number2
    return int(right_answer), question
