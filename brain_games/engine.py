import prompt


def run_game(games):
    print(games.get_description())
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print(games.get_annotation())
    if games.get_description() == '':
        return
    round_counts = 3
    for _ in range(round_counts):
        right_answer, question = games.game_logic()
        print(question)
        player_answer = input('your answer: ')
        if str(player_answer) == str(right_answer) or player_answer == right_answer:
            print('Correct!')
        else:
            return print(f"'{player_answer}' is wrong answer ;(. "
                         f"Correct answer was {right_answer}.")
    print('Congratulations, {}!'.format(name))
