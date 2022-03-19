from random import randint


def get_annotation():
    return 'Answer "yes" if the number is even, otherwise answer "no"'


def get_question_and_answer():
    number1 = randint(1, 20)
    question = number1
    right_answer = 'no' if question % 2 else 'yes'
    return right_answer, question


print(get_question_and_answer())
