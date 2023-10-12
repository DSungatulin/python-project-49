from random import randint


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def choose_number():
    return randint(0, 10)


def is_prime(number):
    i = 0
    if number <= 1:
        return False
    else:
        for k in range(2, number // 2 + 1):
            if (number % k == 0):
                i += 1
        if (i == 0):
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
