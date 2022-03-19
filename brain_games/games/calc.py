import random
from random import randint
import operator


def get_annotation():
    return 'What is the result of the expression?'


def get_question_and_answer():
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }
    operation = random.choice(list(operations.keys()))
    number1 = randint(1, 20)
    number2 = randint(1, 20)
    question = f'{number1} {operation} {number2}'
    right_answer = operations[operation](number1, number2)
    return right_answer, question
