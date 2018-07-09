import random

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if name == "Rock".lower():
        return (0)
    elif name == "Spock".lower():
        return (1)
    elif name == "Paper".lower():
        return (2)
    elif name == "Lizard".lower():
        return (3)
    elif name == "Scissors".lower():
        return (4)
    else:
        print ("Invalid entry.")

def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if number == 0:
        return ("Rock")
    elif number == 1:
        return ("Spock")
    elif number == 2:
        return ("Paper")
    elif number == 3:
        return ("Lizard")
    elif number == 4:
        return ("Scissors")
    else:
        print ("Invalid entry")

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    
    
    # print a blank line to separate consecutive games
    print ()

    print ("Player chooses", player_choice)
    
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice.lower())
    
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print ("Computer chooses", comp_choice)
    
    if (comp_number + 1) == player_number:
        print ("Player wins!")
    elif (comp_number + 2) == player_number:
        print ("Player wins!")
    elif comp_number == player_number:
        print ("Player and computer tie!")
    else:
        print ("Computer wins!")
    print ()


rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")