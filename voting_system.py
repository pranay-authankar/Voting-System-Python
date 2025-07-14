# Funtion to take input of any type
def input_all(message):
    while True:
        print(message, end="")
        inp = input(" -> ").strip()
        if inp:
            return inp
        else:
            print("\nInvalid Input\nTry Again\n")

# Function to take input of only "alphabets"
def input_alpha(message):
    while True:
        print(message, end="")
        inp = input(" -> ").lower().strip().capitalize()
        if inp and inp.isalpha():
            return inp
        else:
            print("\nInvalid Input\nTry Again\n")

# Function to take input of only "alphabets" or "numeric values"
def input_alphanum(message):
    while True:
        print(message, end="")
        inp = input(" -> ").lower().strip().capitalize()
        if inp and inp.isalnum():
            return inp
        else:
            print("\nInvalid Input\nTry Again\n")

# Function to take input of only "numbers"
def input_num(message):
    while True:
        print(message, end="")
        inp = input(" -> ").strip()
        if inp and inp.isdigit():
            inp = int(inp)
            return inp
        else:
            print("\nInvalid Input\nTry Again\n")

# Function to take input of only "numeric value" between a range
def input_specific_num(start, end, message):
    while True:
        print(message)
        inp = input(f"Enter number [{start} - {end}] -> ")
        if inp and inp.isdigit():
            inp = int(inp)
            if start < inp < end: 
                return inp
            else:
                print("\nInvalid Input\n")
        else:
                print("\nInvalid Input\n")

# Function to take input for "yes" or "no"
def yes_no():
    while True:
        inp = input("\nDo you want to continue ? [y/n] -> ").lower().strip()
        if inp and inp in "yn":
            return inp
        else:
            print("\nInvalid Input\nTry Again with [y/n]\n")

# Function to verify the admin
def admin():

    # password initialising for admin's verification
    password = "admin@1234"
    while True :
        inp = input_all("\nEnter Official Password")
        if inp == password:
            return True                                 # Only return, when the password is correct
        else:
            print("\nInvalid Password\n")

# Essential dictionaries
party_vote = {}
voter_password = {}
voter_voted = []

    
# Function to "Add Party"
def add_party(party_dict):
    while True:
        party = input_alpha("\n[Enter 'stop' if mistakenly chosen to add party]\n\nEnter Party name")
        if party not in party_dict:                                                     # Checks if party name exists in party's dictionary
            if party != "Stop":                                                         # if mistakenly chosen to add party, it will stop adding
                party_dict[party] = {}                                                  
                representative = input_alpha(f"\nEnter {party}'s Representative")
                party_dict[party][representative] = 0                                   # Assign initial value to party_dict[party][representative]

                proceed = yes_no()                                                      # Asks if user wanted to proceed adding further
                match proceed:
                    case "y": continue
                    case "n": print(f"{"x".center(30, "-")}");return party_dict         # Creates a line to show that no more adding after this and 'return' the "party_dict"
            else:
                return party_dict
        else:
            print(f"\nParty {party} already exists\n")
            continue

# Function to "Add Voters"
def add_voter(voter_dict):

    # For taking Age of user
    while True:
        age = input_num("\nType 0 as age, if you want to stop entering\n\nYour Age")
        if 0 < age < 18:
            print(f"\nYou are {18-age} years away from giving vote\nTill then, educate yourself about what to do before giving someone vote\n")
            continue

        if age >= 18:
            name = input_alpha("\n[Enter 'stop' is mistakenly chosen to add voter]\n\nYour Name")

            if name not in voter_dict:                                                                      # if user exist in voter_dict
                if name != "Stop":
                    password = input_all("\nGive the device to the voter\nSet Password [Case sensative]")
                    voter_dict[name] = password
                    print(f"\n{name} Added Successfully\n")

                    proceed = yes_no()

                    match proceed:
                        case "y": continue
                        case "n": print(f"{"x".center(30, "-")}");return voter_dict
                else:
                    return voter_dict
            else:
                print(f"\nVoter {name}, is already exists\nTry with new Voter")
                continue
        if age == 0:
            print(f"\n{"x".center(30, "-")}\n")
            return voter_dict

# Function to "Verify Voters" (while voting)
def verify_voter(voter_dict, voted_list):

    while True:
        name = input_alpha("\nEnter Your Name") # Voter name 
        if name in voter_dict:
            if name not in voted_list:          # Checks if the user voted or not

                # Loop for password
                while True:
                    password = input_all("\nEnter Password")
                    if password == voter_dict[name]:
                        return name
                    else:
                        print("\nwrong Password\nTry Again\n")
                        proceed = yes_no()                      # when user can't recall the password
                        match proceed:
                            case "y": continue
                            case "n": break
                continue
            else:
                print(f"\n{name} Already Voted\nTry with different name\n")
        else:
            print(f"\n{name} not in Voter List\nTry with different name\n")

# Function for "Voting"
def voting(party_dict, voted_list, name):

    # Loop for correct voting input
    while True:
        print("\nList of Party and Their Representatives\n")
        i = 1

        # Displays No. of Parties and Their Representatives
        for party in party_dict:
            for representative in party_dict[party]:
                print(f"{i} -> {party} - {representative}")
                i += 1
                
        # Voting Program
        vote = input_specific_num(0, i+1, "\nYour Vote")    # User enters a number of whom they vote
        party = list(party_dict.keys())[vote-1]             # Stores voted party's name 
        representative = list(party_dict[party].keys())[0]  # Stores voted Representative's name
        if 0 < vote <= len(party_dict):                     # Check the correct input
            party_dict[party][representative] += 1          # Adds one vote at a time to party's representative
            voted_list.append(name)                         # Adds the name of voter in "voters who voted" list
            return
        else:
            print("\nEnter Valid Input\n")

# Function to view "Live Results" (Only for admin)
def live_result(party_dict):
    print("\nLive Results\n")

    i = 1
    for party in party_dict:
        for representative in party_dict[party]:
            print(f"{i} -> {party} - {representative} - {party_dict[party][representative]}")
            i += 1
    print(f"{"x-x-x".center(30,"-")}")

# Function to view the "Winner"
def winner(party_dict):
    vote_list = []                                              # creates a temporary list of votes each party gets

    # Accessing the party_dict to add the votes to the above list
    for party in party_dict:
        for representative in party_dict[party]:
            vote = party_dict[party][representative]
            vote_list.append(vote)
    max_vote = max(vote_list)                                   # Stores value of maximum votes received by a party

    win = {}                                                    # Creates a temporary dictionary to store winner party's and representative's name

    # Accessing the party_dict to evaluate the maximim vote and how many party got max much vote
    for party in party_dict:
        for representative in party_dict[party]:
            if max_vote == party_dict[party][representative]:
                win[party] = representative                     # Adds party and representative name in win{}

    print(f"\n{"Winner".center(30, "-")}\n")

    # if winner is only one
    if len(win) < 2:
        print(f"{party} - {representative}")
    else:                                                       # if more than 1 winner
        for winner in win:
            print(f" - {winner} -> {win[winner]}")
        print("\nThere are more than one winner, so the authority will decide their decision\n")
    print(f"\n{"Congratulations".center(30,"-")}\n\n{"[ Program Ends ]".center(30,"-")}")

# Function for admin to operate (during voting)
def admin_menu(party_dict,):
    print("\nAdmin Menu\n")

    
    while True:
        task = input_num("\n1. View Live Results\n0. STOP\n\n")
        match task:
            case 1: live_result(party_dict); break
            case 0: return
            case _: print("\nEnter either 1 or 0\n"); continue

# Program for Voting System
def voting_system(party_dict, voter_dict, voted_list):
    print("\nWelcome to Voting Managment System\n")
    
    # Verify the admin
    admin()

    # fAt start the control is in admin's hand 
    while True:
        ask = input_num("\nWhat Task to do ?\n1. Add Party\n2. Add Voter\n3. Start Voting\n\n")
        match ask:
            case 1: add_party(party_dict)
            case 2: add_voter(voter_dict)
            case 3: print("\nSetup done, now you can start voting\n"); break
            case _: print("\nInvalid Input\nTry Again\n")
    
    # Voting Begins
    print("\nVoting starts from here\n")
    
    # Loop for smoothly operations during voting
    while True:

        # Checks if all registred voters voted or not
        if len(voted_list) != len(voter_dict):
            ask = input_num("\nWho is having the device\n1. Admin\n2. Voter\n3. STOP the program\n\n")

            # Admin Handle
            if ask == 1:
                admin()
                admin_menu(party_dict)
                continue

            # Voter Handle
            if ask == 2:
                name = verify_voter(voter_dict, voted_list)
                voting(party_dict, voted_list, name)
                continue
            
            # Stops the program before the voting of all registered voters
            if ask == 3:

                # Ensures that all registered voters didn't voted (for double step verification)
                if len(voted_list) != len(voter_dict):

                    # asks if voting continues or get the results
                    ask = input_specific_num(0, 3, "\nNot every registered voter voted\nWant to [1] view Results, or [2] continue voting?\n")
                    match ask:
                        case 1:                 # Admin will declare the results
                            admin()
                            winner(party_dict)
                        case 2: continue        # Continues voting
        else:

            # Checks that all voters voted
            if len(voted_list) == len(voter_dict):
                print("\nHandover the device to admin\n")

                admin()             # Admin will declare the winner
                winner(party_dict)
                break               # Closes the loop, and ends the program

voting_system(party_vote, voter_password, voter_voted)
