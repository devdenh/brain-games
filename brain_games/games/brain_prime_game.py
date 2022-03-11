from random import randint


def get_description():
    return 'brain-prime\n'


def get_annotation():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_logic():
    number = randint(2, 50)
    divider = 2
    while divider <= number / 2:
        if number % divider == 0:
            question = f'Question: {number}'
            right_answer = 'no'
            return right_answer, question
        divider += 1
    question = f'Question: {number}'
    right_answer = 'yes'
    return right_answer, question

