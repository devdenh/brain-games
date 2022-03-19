from random import randint
import math


def get_annotation():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    for divisior in range(2, int(math.sqrt(number)) + 1):
        if number % divisior == 0:
            return False
    return True


def get_question_and_answer():
    number = randint(2, 50)
    if is_prime(number):
        right_answer = 'yes'
        question = number
        return right_answer, question
    right_answer = 'no'
    question = number
    return right_answer, question
