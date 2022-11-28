import random

options = ['Rock', 'Paper', 'Spock', 'Lizard', 'Scissors']


def name_to_number(name):
    if name == 'Rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'Paper':
        return 2
    elif name == 'Lizard':
        return 3
    elif name == 'Scissors':
        return 4
    else:
        return -1


def number_to_name(number):
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        return "False"


while True:
    # ////////////get user input
    userInput = input("Rock, Paper, Scissors, Lizard, Spock? (type exit to quit):\n")
    if userInput == 'exit' or userInput == 'quit':
        break
    elif name_to_number(userInput) == -1:
        print("That's not a valid play. Check your spelling!")
    else:
        player_number = name_to_number(userInput)
        random_element = random.choice(options)
        comp_number = name_to_number(random_element)
        difference = (comp_number - player_number) % 5
        if difference == 1 or difference == 2:
            print("You lost! " + str(userInput) + " loses to " + str(random_element))
        elif difference == 4 or difference == 3:
            print("You won! " + str(userInput) + " triumphs " + str(random_element))
        elif difference == 0:
            print("Player and computer tie!")
