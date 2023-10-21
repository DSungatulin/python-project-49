from random import randint


RULES = 'What number is missing in the progression?'
MIN_NUMBER = 0
MAX_NUMBER = 100
MIN_PROGRESSION_STEP = 1
MAX_PROGRESSION_STEP = 5
MIN_PROGRESSION_LENGTH = 5
MAX_PROGRESSION_LENGTH = 10


def choose_first_number():
    return randint(MIN_NUMBER, MAX_NUMBER)


def choose_progression_step():
    return randint(MIN_PROGRESSION_STEP, MAX_PROGRESSION_STEP)


def choose_progression_length():
    return randint(MIN_PROGRESSION_LENGTH, MAX_PROGRESSION_LENGTH)


def generate_progression():
    first_number = choose_first_number()
    step = choose_progression_step()
    last_index = choose_progression_length() + 1
    progression = [first_number]
    current_index = len(progression) - 1
    while len(progression) < last_index:
        progression.append(progression[current_index] + step)
        current_index += 1
    return progression


def replace_random_element(sequence):
    sequence = sequence[:]
    last_index = len(sequence) - 1
    random_index = randint(0, last_index)
    exluded_element = sequence.pop(random_index)
    sequence.insert(random_index, '..')
    return (sequence, exluded_element)


def make_task():
    missing_element = ' '
    progression = generate_progression()
    edited_progression_and_answer = replace_random_element(progression)
    edited_progression = edited_progression_and_answer[0]
    question = missing_element.join(map(str, edited_progression))
    answer = edited_progression_and_answer[1]
    return (question, answer)
