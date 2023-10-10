from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def choose_number():
    return randint(0, 100)


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def make_task():
    number = choose_number()
    question = number
    answer = get_correct_answer(number)
    return (question, answer)


def get_correct_answer(number):
    if is_even(number):
        return 'yes'
    return 'no'
