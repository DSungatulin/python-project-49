import prompt


ROUNDS = 3


def report_incorrect_answer(user_answer, correct_answer, user_name):
    report_incor_ans = f'"{user_answer}" is wrong answer ;(.' \
        f'Correct answer was "{correct_answer}".' \
        f'\nLet\'s try again, {user_name}!'
    print(report_incor_ans)


def run_game_engine(game):
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}')
    print(game.RULES)
    for _ in range(ROUNDS):
        question, correct_answer = game.make_task()
        print(f'Question: {question}')
        user_answer = prompt.string("Your answer: ")

        if user_answer.lower() != str(correct_answer):

            report_incorrect_answer(user_answer, correct_answer, user_name)
            return
        print('Correct!')
    print(f'Congratulations, {user_name}!')
