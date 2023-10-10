from random import randint


RULES = 'What number is missing in the progression?'


def choose_first_number():
    return randint(0, 100)


def choose_progression_step():
    return randint(1, 5)


def choose_progression_length():
    return randint(5, 10)


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
