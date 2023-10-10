from random import randint, choice


RULES = 'What is the result of the expression?'
OPERATORS = ("+", "-", "*")


def choose_number():
    random_number = randint(0, 100)
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
