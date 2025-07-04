class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

def question_solver(prompt_list):
    total_questions = len(prompt_list)
    correct = 0
    for question in prompt_list:
        if question.answer == "(a)" or question.answer == "a":
            index1 = question.prompt.find("(a)")
            index2 = question.prompt.find("(b)")
            ans_full = question.prompt[index1:index2].replace("\n", "")
        elif question.answer == "(b)" or question.answer == "b":
            index1 = question.prompt.find("(b)")
            index2 = question.prompt.find("(c)")
            ans_full = question.prompt[index1:index2].replace("\n", "")
        else:
            index1 = question.prompt.find("(c)")
            ans_full = question.prompt[index1:].replace("\n", "")
        valid_option = False
        answer = ""
        while not valid_option:
            answer = input(question.prompt).lower()
            if answer not in ["a", "b", "c", "(a)", "(b)", "(c)"]:
                print("Options are either 'a', 'b' or 'c'")
            else:
                valid_option = True
        if answer == question.answer or answer == question.answer.replace("(", "").replace(")", ""):
            correct += 1
            print(f"Correct, The answer was {ans_full}!")
        else:
            print(f"Incorrect, The answer was {ans_full}")
    print(f"Sadly you did not get any of the {total_questions} questions correct" if correct == 0 else f"Good effort, you got {correct} out of {total_questions} questions correct" if correct < total_questions/2 else f"{"Congratulations, you got all" if correct == total_questions else "Valiant effort, you got"} {correct} out of {total_questions} questions correct!")

def question_maker():
    finished = False
    prompt_list = []
    questions_list = []
    question_num = 0
    while not finished:
        same_questions = False
        while not same_questions:
            question = input(f"Enter the{'' if not prompt_list else ' next'} question\n")
            question = f"{question}" if question.endswith('?') else f"{question}?"
            is_duplicate = False
            if question_num > 0:
                for i in range(question_num):
                    if question.lower() == questions_list[i].lower():
                        print(f"You have entered the same question previously in Question Number {i + 1}, please enter a different question")
                        is_duplicate = True
                        break
                if not is_duplicate:
                    questions_list.append(f"{question}")
                    same_questions = True
            elif question_num == 0:
                questions_list.append(f"{question}")
                same_questions = True
        same_options = False
        option_a = option_b = option_c = ""
        while not same_options:
            option_a = input("Enter option a\n")
            option_b = input("Enter option b\n")
            option_c = input("Enter option c\n")
            if option_a == option_b or option_a == option_c or option_b == option_c:
                print(f"The options cannot be the same, enter them again")
            else:
                same_options = True
        valid_option = False
        answer = ""
        while not valid_option:
            answer = input("Enter the correct option\n(a/b/c)\n").lower()
            if answer not in ["a", "b", "c", "(a)", "(b)", "(c)"]:
                print("Option are either 'a', 'b' or 'c', enter again")
            else:
                valid_option = True
        prompt_list.append(Question(f"Q{question_num + 1}){questions_list[question_num]}\n(a) {option_a}\n(b) {option_b}\n(c) {option_c}\n\n", answer))
        next_question = input("Do you want to add more questions?\n(y/n)\n")
        if next_question == "y":
            question_num += 1
        elif next_question == "n":
            finished = True
    return prompt_list