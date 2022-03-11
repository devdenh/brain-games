import prompt
import math

def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


def user_name(name):
    real_name = name
    return real_name

def somef():
    for x in range(50, 0, -1):
        print(x)
somef()
