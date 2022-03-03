import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, {user_name}!'.format(user_name=name))
    return name
