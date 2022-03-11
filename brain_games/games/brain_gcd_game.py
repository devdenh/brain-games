import math
from random import randint


def get_description():
    return 'brain-gcd\n'


def get_annotation():
    return 'Find the greatest common divisor of given numbers.'


def game_logic():
    number1 = randint(1, 50)
    number2 = randint(51, 100)
    question = f'Question: {number1} {number2}'
    right_answer = math.gcd(number1, number2)
    return right_answer, question
