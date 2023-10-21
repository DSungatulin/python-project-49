from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 0
MAX_NUMBER = 100


def choose_number():
    return randint(MIN_NUMBER, MAX_NUMBER)


def is_even(number):
    return number % 2 == 0


def make_task():
    number = choose_number()
    question = number
    answer = get_correct_answer(number)
    return (question, answer)


def get_correct_answer(number):
    if is_even(number):
        return 'yes'
    return 'no'
