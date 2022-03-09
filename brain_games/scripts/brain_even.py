from random import randint
import prompt
from brain_games.engine import run_game
from brain_games.games import brain_even_game


def get_question():
    question = f'Question: {random_number}'
    return print(question)


def get_question_and_answer():
    question = f'Question: {randint(1, 20)}'
    answer = input('Your answer: ')
    return question, answer


def game_description():
    return print('brain-even'), print()


random_number = randint(1, 20)

def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, {user_name}!'.format(user_name=name))
    return name


def engine():
    name = prompt.string('May I have your name? ')
    print('Hello, {user_name}!\nAnswer "yes" if the number is even, otherwise answer "no".'.format(user_name=name))
    rounds_count = 3
    for _ in range(rounds_count):
        random_number = randint(1, 20)
        print(f'Question: {random_number}')
        player_answer = input('your answer: ')
        if random_number % 2 == 0 and player_answer == "yes" or (random_number % 2 != 0 and player_answer == "no"):
            print('Correct!')
        else:
            correct_answer = "'no'"
            wrong_answer = "'yes'"
            return print(f"'{player_answer}' is wrong answer ;(. "
                         f"Correct answer was {wrong_answer}.")
    print('Congratulations, {}!'.format(name))



def main():
    run_game(brain_even_game)


if __name__ == '__main__':
    main()
