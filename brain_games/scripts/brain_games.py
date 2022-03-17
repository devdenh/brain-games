<<<<<<< HEAD
from brain_games.engine import run_game
from brain_games.games import brain_game_game


def main():
    return run_game(brain_game_game)

#!/usr/bin/env python
from brain_games.cli import welcome_user


def main():
    print('Welcome to the Brain Games!')
    welcome_user()



if __name__ == '__main__':
    main()
