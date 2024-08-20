import datetime

# Get today's date
todaydate = datetime.date.today()

# Define questions list
questions = [
    "How was your day in Pie Infocomm?",
    "Which kind of work or task did you accomplish today?",
    "Did you face any obstacles or challenges today?",
    "What is something you learned today?",
    "What is one thing you would like to improve or work on tomorrow?"
]

# Function to add a question to the list
def add_question(msg):
    questions.append(msg)

# Add another question via add_question
add_question("What did you have for breakfast?")

try:
    # Collect answers via list comprehension
    answers = [input(f"\n{question}\n") for question in questions]
except Exception as e:
    print(f"An error occurred while collecting answers: {e}")
    # catching error in case any error like IOError occurs

try:
    # Write questions and answers to file
    with open(f'{todaydate}.txt', 'w') as file:
        for question, answer in zip(questions, answers):
            file.write(f"{question}\n{answer}\n\n")
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")

# Function to view the journal, displaying the output at the terminal
def view_journal():
    try:
        for question, answer in zip(questions, answers):
            print(f"{question}\n{answer}\n\n")
    except Exception as e:
        print(f"An error occurred while viewing the journal: {e}")

try:
    # let user decide whether they want view the journal
    flag = int(input("Do you want to view your journal? Press 1 for Yes, 0 for No\n"))

    if flag == 1:
        view_journal()
    elif flag == 0:
        print("THANK YOU")
except ValueError:
    print("Invalid input. Please enter 1 or 0.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
