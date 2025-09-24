class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer


def question_solver(prompt_list):
    total_questions = len(prompt_list)
    correct = 0

    for question in prompt_list:
        print(question.prompt)
        for opt in question.options:
            print(opt)
        while True:
            try:
                user_ans = int(input("Enter your answer (option number): "))
                if 1 <= user_ans <= len(question.options):
                    break
                else:
                    print(f"Please enter a number between 1 and {len(question.options)}.")
            except ValueError:
                print("Please enter a valid integer.")
        if user_ans == question.answer:
            correct += 1
            print(f"Correct! The answer was {question.options[question.answer - 1]}\n")
        else:
            print(f"Incorrect! The correct answer was {question.options[question.answer - 1]}\n")
    if correct == 0:
        print(f"Sadly, you did not get any of the {total_questions} questions correct.")
    elif correct < total_questions / 2:
        print(f"Good effort, you got {correct} out of {total_questions} correct.")
    elif correct == total_questions:
        print(f"Congratulations! You got all {total_questions} questions correct!")
    else:
        print(f"Nice work! You got {correct} out of {total_questions} correct.")

def question_maker():
    prompt_list = []
    questions_seen = set()
    question_num = 0

    while True:
        while True:
            question = input(f"Enter the{'' if not prompt_list else ' next'} question\n")
            if not question.endswith("?"):
                question += "?"
            if question.lower() in questions_seen:
                print("You already entered this question. Try again.")
            else:
                questions_seen.add(question.lower())
                break
        while True:
            try:
                option_num = int(input("How many options do you want this question to have?\n"))
                if option_num > 0:
                    break
                else:
                    print("The number must be greater than 0.")
            except ValueError:
                print("Please enter a valid integer.")
        options_list = []
        for i in range(option_num):
            while True:
                temp = input(f"Enter option number {i + 1}:\n")
                if temp.strip() == "":
                    print("Option cannot be empty.")
                elif temp.lower() in [opt.lower().split(")", 1)[1] for opt in options_list]:
                    print("You already entered this option. Try again.")
                else:
                    options_list.append(f"{i + 1}) {temp}")
                    break
        while True:
            try:
                answer = int(input(f"Enter the correct option number (1-{option_num}):\n"))
                if 1 <= answer <= option_num:
                    break
                else:
                    print(f"Answer must be between 1 and {option_num}.")
            except ValueError:
                print("Please enter a valid integer.")
        q_text = f"Q{question_num + 1}) {question}\n"
        prompt_list.append(Question(q_text, options_list, answer))
        next_question = input("Do you want to add more questions? (y/n)\n").lower()
        if next_question != "y":
            break
        question_num += 1
    return prompt_list