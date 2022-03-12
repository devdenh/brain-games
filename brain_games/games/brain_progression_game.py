from random import randint


def get_description():
    return 'brain-progression\n'


def get_annotation():
    return 'What number is missing in the progression?'


def game_logic():
    random_element = randint(1, 9)
    progression_length = 11
    random_step = randint(2, 6)
    progression_line = ''
    for progression in range(0 + random_step,
                             random_step * progression_length, random_step):
        if progression == random_step * random_element:
            progression = '..'
        progression_line += '{} '.format(str(progression))
        right_answer = random_step * random_element
        question = f'Question: {progression_line}'
    return right_answer, question
