import json
import os

def json_questions(questions_data):
    dir = os.path.dirname(os.path.realpath(__file__)) # Gets the absolute path of the current python file
    file_path = os.path.join(dir, questions_data) # Joins the directory path with the json file name

    with open(file_path, "r") as file: # Opens the json file in read mode
        questions_data = json.load(file) 

    return questions_data 


def section_menu():
    print("\nPlease select the quiz you want to take!")
    print("build version 0.2...")
    print("1) Quiz 1")
    print("2) Quiz 2")
    print("3) Quiz 3")
    print("4) Exit")


def user_menu_input():
    while True:
        try:
            user_input = int(input("\nEnter the number of your choice: "))
            if user_input >= 1 and user_input <= 4:
                return user_input
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")


def display_question(questions_data):
    print(questions_data["question"])

    for key, value in questions_data["options"].items(): 
        print(f"{key}. {value}")    
        

def display_answer(questions_data):
    for key, value in questions_data["correct_answer"].items():
        print(f"{key}. {value}")


def take_quiz(questions_data, highest_score):
    score = 0

    for question in questions_data:
        display_question(question)

        while True:
            try:
                user_answer = int(input("\nEnter number(1, 2, 3, or 4): "))
                if user_answer in range(1, 5):  
                    if user_answer == int(question["correct_answer"]):  
                        print("\nCorrect!\n")
                        score += 1
                    else:
                        print("\nIncorrect!\n")
                    break
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Please enter a valid option.")

    print(f"You scored: {score}/{len(questions_data)}")

    # displays highest score   
    if score > highest_score:
        print(f"Congratulations! New highest score: {score}/{len(questions_data)}")
        return score
    else:
        return highest_score


if __name__ == '__main__':
    questions_data = json_questions("questions_data.json")
    highest_score = 0  

    while True:
        section_menu()
        user_input = user_menu_input()

        if user_input == 4:
            print("Goodbye!")
            break

        selected_section = f"section_{user_input}"

        if selected_section in questions_data:
            section_questions = questions_data[selected_section]
            highest_score = take_quiz(section_questions, highest_score)
        else:
            print("Invalid section. Please choose a valid section.")
