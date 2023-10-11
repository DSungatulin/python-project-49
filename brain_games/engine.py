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
    winstreak = 0
    print('Hello, {}!'.format(user_name))
    print(game.RULES)
    while winstreak < ROUNDS:
        question_and_answer = game.make_task()
        question = question_and_answer[0]
        correct_answer = str(question_and_answer[1])
        print(f'Question: {question}')
        user_answer = prompt.string("Your answer: ")

        if user_answer.lower() == correct_answer:
            print('Correct!')
            winstreak += 1
            if winstreak == 3:
                print(f'Congratulations, {user_name}!')
        else:
            report_incorrect_answer(user_answer, correct_answer, user_name)
            break
