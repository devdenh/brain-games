import random


def get_annotation():
    return 'What number is missing in the progression?'


def get_question_and_answer():
    start = random.randint(1, 50)
    step = random.randint(1, 20)
    length = 10

    progression = list(range(start, (start + length * step), step))

    hidden_index = random.randrange(0, length)
    right_answer, progression[hidden_index] = progression[hidden_index], '..'
    question = ' '.join(map(str, progression))
    return right_answer, question
