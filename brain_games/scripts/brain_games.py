#!/usr/bin/env python
def main():
    print("Welcome to the Brain Games!")

    if __name__ == '__main__':
        main()

import brain_games.cli
from brain_games.cli import welcome_user
welcome_user()
