from random import randint


def get_question():
    question = f'Question: {random_number}'
    return print(question)


def game_description():
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    return print(description)


random_number = randint(1, 20)


def get_answer_and_check():
    if random_number % 2 == 0:
        correct_answer = "'yes'"
    else:
        correct_answer = "'no'"
    player_answer = input('Your answer: ')
    if player_answer != 'yes' and random_number % 2 == 0 or (player_answer == 'yes' and random_number % 2 != 0):
        print(f"'{player_answer}' is wrong answer ;(. Correct answer was {correct_answer}.")
    else:
        print('Correct!')
game_description()
get_question()
get_answer_and_check()
