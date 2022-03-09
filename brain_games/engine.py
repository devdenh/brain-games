import prompt


def run_game(games):
    print(games.get_annotation())
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))

