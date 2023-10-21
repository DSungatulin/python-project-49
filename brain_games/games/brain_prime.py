from random import randint


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 0
MAX_NUMBER = 100


def choose_number():
    return randint(MIN_NUMBER, MAX_NUMBER)


def is_prime(number):
    i = 0
    if number <= 1:
        return False

    for k in range(2, number // 2 + 1):
        if (number % k == 0):
            i += 1
    if (i == 0):
        return True


def make_task():
    number = choose_number()
    question = number
    answer = get_correct_answer(number)
    return (question, answer)


def get_correct_answer(number):
    if is_prime(number):
        return 'yes'
    return 'no'
