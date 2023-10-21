from random import randint, choice


RULES = 'What is the result of the expression?'
OPERATORS = ("+", "-", "*")
MIN_NUMBER = 0
MAX_NUMBER = 100


def choose_number():
    random_number = randint(MIN_NUMBER, MAX_NUMBER)
    return random_number


def calculate_expression(first_number, second_number, operator):
    match operator:
        case "+":
            return first_number + second_number
        case "-":
            return first_number - second_number
        case "*":
            return first_number * second_number


def make_task():
    first_number = choose_number()
    second_number = choose_number()
    operator = choice(OPERATORS)
    answer = calculate_expression(first_number, second_number, operator)
    question = f'{first_number} {operator} {second_number}'
    return (question, answer)
