from random import randint
from math import gcd


RULES = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 0
MAX_NUMBER = 100


def choose_number():
    return randint(MIN_NUMBER, MAX_NUMBER)


def make_task():
    first_number = choose_number()
    second_number = choose_number()
    numbers = f'{first_number} {second_number}'
    question = numbers
    answer = get_correct_answer(first_number, second_number)
    return (question, answer)


def get_correct_answer(first_number, second_number):
    return gcd(first_number, second_number)
