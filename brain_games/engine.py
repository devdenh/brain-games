import prompt


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print(game.get_annotation())
    round_counts = 3
    for _ in range(round_counts):
        right_answer, question = game.get_question_and_answer()
        print(f'Question: {question}')
        player_answer = input('your answer: ')
        if str(player_answer) == str(right_answer) or\
                player_answer == right_answer:
            print('Correct!')
        else:
            return print(f"'{player_answer}' is wrong answer ;(."
                         f" Correct answer was {right_answer}."
                         f"\nLet's try again, {name}!")
    print('Congratulations, {}!'.format(name))
