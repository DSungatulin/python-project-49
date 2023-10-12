from random import randint


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def choose_number():
    return randint(0, 10)


def is_prime(number):
    n = 0
    if number <= 1:
        return False

    for i in range(2, number // 2 + 1):
        if (number % i == 0):
            n += 1
    if (n == 0):
        return True
    else:
        return False


def make_task():
    number = choose_number()
    question = number
    answer = get_correct_answer(number)
    return (question, answer)


def get_correct_answer(number):
    if is_prime(number):
        return "yes"
    else:
        return "no"
