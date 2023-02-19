import random
import copy
import time
from prettytable import PrettyTable    #this helps build BOY ATTRIBUTE TABLE
import colorama #fixes windows shell color bugs
from colorama import Fore, Back, Style #gives us come color options
### installing colorama: pip install colorama
### installing prettytable: python -m pip install -U prettytable
import click # Import click library for good screen clearing function
colorama.init() #turns on windows shell fix

class Player:  #class Player constructor
    def __init__(self, playernumber, cardsinhand, current_turn, playername, collected_clues, dialed_this_turn, guessed_this_turn, pvp_in_hand, pvp_this_turn):
        self.playernumber = playernumber    #Class Player gets a "playernumber" attribute
        self.cardsinhand = cardsinhand      #Class Player gets a "cardsinhand" attribute
        self.current_turn = current_turn      #gives a boolean flag for if the player is currently playing or not
        self.playername = playername        #gives players a name attribute in the class
        self.collected_clues = collected_clues #where the information goes that the player collects
        self.dialed_this_turn = dialed_this_turn #a flag for limiting 1 dial per turn
        self.guessed_this_turn = guessed_this_turn #only one guess per turn flag
        self.pvp_in_hand = pvp_in_hand
        self.pvp_this_turn = pvp_this_turn

player1 = Player(1,[],False,"",[],False,False,[],False)
player2 = Player(2,[],False,"",[],False,False,[],False)
player3 = Player(3,[],False,"",[],False,False,[],False)
player4 = Player(4,[],False,"",[],False,False,[],False)

all_player_list=[player1,player2,player3,player4]  #all possible players in the game
player_list=[]  #a list built out by the player's choice of player num
crush=0  #initalizes game crush global var

class Cards:  #class Cards constructor
    def __init__(self, name, phonenum, hangout, sport, food, clothing, clue_to_reveal, first_call, curse_bucket):
        self.name = name    #Class Cards gets a "name" attribute
        self.phonenum = phonenum  #Card objects have stuff
        self.hangout = hangout
        self.sport = sport
        self.food = food
        self.clothing = clothing
        self.clue_to_reveal = clue_to_reveal #this is where the clues that are revealed in the game assoicate with cards to dial
        self.first_call = first_call #a flag to show if the card has been dialed before
        self.curse_bucket = curse_bucket #where pvp cards can haunt boy cards

#building Cards objects:
c0 = Cards("Dave","555-1111","Crosstown Mall","null","Cookies","Blue Jeans","",True,[])
c1 = Cards("George","555-1233","Crosstown Mall","null","Ice Cream","Tie","",True,[])
c2 = Cards("Dale","555-4566","Crosstown Mall","null","Ice Cream","Jacket","",True,[])
c3 = Cards("Alan","555-7899","Crosstown Mall","null","Cookies","Tie","",True,[])
c4 = Cards("James","555-2588","E.A.T.S. Snack Shop","null","Hot Dogs","Jacket","",True,[])
c5 = Cards("Phil","555-3333","E.A.T.S. Snack Shop","null","Pizza","Glasses","",True,[])
c6 = Cards("Bruce","555-3699","E.A.T.S. Snack Shop","null","Pizza","Tie","",True,[])
c7 = Cards("Tyler","555-1477","E.A.T.S. Snack Shop","null","Hot Dogs","Blue Jeans","",True,[])
c8 = Cards("Jamal","555-9877","Reel Movies","null","Candy","Tie","",True,[])
c9 = Cards("Gary","555-3211","Reel Movies","null","Popcorn","Blue Jeans","",True,[])
c10 = Cards("Dan","555-7777","Reel Movies","null","Candy","Blue Jeans","",True,[])
c11 = Cards("Spencer","555-6544","Reel Movies","null","Popcorn","Jacket","",True,[])
c12 = Cards("Mark","555-8522","Woodland Park","Baseball","null","Hat","",True,[])
c13 = Cards("Jason","555-7411","Woodland Park","Baseball","null","Glasses","",True,[])
c14 = Cards("Steve","555-9999","Woodland Park","Skateboarding","null","Jacket","",True,[])
c15 = Cards("John","555-9633","Woodland Park","Skateboarding","null","Anything Yellow","",True,[])
c16 = Cards("Paul","555-5515","High Tide Beach","Volleyball","null","Anything Yellow","",True,[])
c17 = Cards("Tony","555-2442","High Tide Beach","Volleyball","null","Hat","",True,[])
c18 = Cards("Wayne","555-3535","High Tide Beach","Surfing","null","Anything Yellow","",True,[])
c19 = Cards("Mike","555-2226","High Tide Beach","Surfing","null","Hat","",True,[])
c20 = Cards("Scott","555-5599","Jim's Gym","Basketball","null","Anything Yellow","",True,[])
c21 = Cards("Bob","555-4884","Jim's Gym","Basketball","null","Glasses","",True,[])
c22 = Cards("Carlos","555-6668","Jim's Gym","Tennis","null","Hat","",True,[])
c23 = Cards("Matt","555-7557","Jim's Gym","Tennis","null","Glasses","",True,[])

##global stuff##
card_list = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20,c21,c22,c23]
# this is the master list of cards in the deck. a way to reference a var list containing all card object names.
# tried to find a less brute force way to do this but so far no luck.

class Pvp_Cards:  #builds Pvp_Cards class
    def __init__(self, type, player_owner, used_on, long_name):
        self.type = type    #Mom says hang up. share a secret, speakerphone.
        self.player_owner = player_owner  #who played the card
        self.used_on = used_on #what Card the Pvp_Card was used on
        self.long_name = long_name #a way to not have to type shit every time

pvp0 = Pvp_Cards("hangup",player1,[],"Mom Says Hang up!")
pvp1 = Pvp_Cards("hangup",player2,[],"Mom Says Hang up!")
pvp2 = Pvp_Cards("hangup",player3,[],"Mom Says Hang up!")
pvp3 = Pvp_Cards("hangup",player4,[],"Mom Says Hang up!")
pvp4 = Pvp_Cards("share_secret",player1,[],"Share a Secret")
pvp5 = Pvp_Cards("share_secret",player2,[],"Share a Secret")
pvp6 = Pvp_Cards("share_secret",player3,[],"Share a Secret")
pvp7 = Pvp_Cards("share_secret",player4,[],"Share a Secret")
pvp8 = Pvp_Cards("speakerphone",player1,[],"Speakerphone")
pvp9 = Pvp_Cards("speakerphone",player2,[],"Speakerphone")
pvp10 = Pvp_Cards("speakerphone",player3,[],"Speakerphone")
pvp11 = Pvp_Cards("speakerphone",player4,[],"Speakerphone")

pvp_list = [pvp0,pvp1,pvp2,pvp3,pvp4,pvp5,pvp6,pvp7,pvp8,pvp9,pvp10,pvp11]

game_deck = copy.copy(card_list)  # this clones from the master list for the "in game" deck. Use game_deck when moving stuff around, use card_list as universal master ref)
in_hand = []  # initializes player hand as empty
discard_pile = []  # initializes discard pile as empty

#functions
def clear_screen():
    # Clear screen using click.clear() function
    click.clear()

#Text Speed Delay Settings
def delay():
    time.sleep(1)
def short_delay():
    time.sleep(.5)
def long_delay():
    time.sleep(2)

#Some TEXT STYLE stuff
def blue_out(text): #red_out is how i am crossing out entries in the notepad
    return Back.LIGHTBLACK_EX + Fore.BLUE + text + Style.RESET_ALL
def red_out(text): #red_out is how i am crossing out entries in the notepad
    return Back.RED + Fore.WHITE + text + Style.RESET_ALL
def white_out(text): #red_out is how i am crossing out entries in the notepad
    return Back.WHITE + Fore.BLACK + text + Style.RESET_ALL

def boy_attribute_table():   #this is an automated notepad of the clues you have crossed off the list. player specific
    notepad = PrettyTable(["Called?", "Hangout", "Sport \ Food", "Clothing", "Secret Admirer?"]) # Specify the Column Names while initializing the Table
    for i in card_list:   #iterates over all cards
        hangout = i.hangout
        sport = i.sport
        food = i.food
        clothing = i.clothing
        name = i.name
        listname = i.name
        if i in whos_turn().collected_clues: name = red_out(i.name) #reds out a name you have dialed already in the "dialed" list
        for x in whos_turn().collected_clues: #iterates over all the clues the player has heard so far
            if x.clue_to_reveal == i.sport: sport = red_out(i.sport)
            if x.clue_to_reveal == i.hangout: hangout = red_out(i.hangout)
            if x.clue_to_reveal == i.food: food = red_out(i.food)
            if x.clue_to_reveal == i.clothing: clothing = red_out(i.clothing)   #if any of the clues collected fit in the category, it gets redded out
        if i.sport == "null": sport = ""
        if i.food == "null": food = ""   #removing null entries for food sport weirdness
        notepad.add_row([name,hangout, sport+food, clothing, listname])   #adds rows qeued up for printing
    notepad.align="l"   #aligns the table to the left
    clear_screen()
    print(notepad)  #prints notepad
    input("Press Enter to continue...")
    clear_screen()

def new_game_crush():
    clue_list = []  # makes bucket to hold all valid clues in
    crush = random.randint(0, int(len(card_list)-1)) #rng a boy from the card list to be the crush, adjusting len from starting at 1 while list index starts at 0
    for i in range (len(card_list)):   #creates a list of all possible clues in clue_list, removing "null" entries for foodsport wierdness
        if card_list[i].hangout != "null": clue_list.append(card_list[i].hangout)
        if card_list[i].sport != "null": clue_list.append(card_list[i].sport)
        if card_list[i].food != "null": clue_list.append(card_list[i].food)
        if card_list[i].clothing != "null": clue_list.append(card_list[i].clothing)

    clue_list = list(set(clue_list)) #removes all duplicate entries from the list
    random.shuffle(clue_list)  #shuffles clue list

    for i in range(len(clue_list)):   #distributes all clues to all cards' "clue to reveal" player object attribute
        card_list[i].clue_to_reveal = clue_list[i]
    return crush

def starting_deal():
    for i in range (3): #gives players 3 deck cards
        for f in player_list:
            f.cardsinhand.append(game_deck.pop(0))
    if len(player_list) == 1: print("Single Player Mode. PvP Cards Disabled.\nYou have drawn 3 cards from the deck.")
    if len(player_list) > 1:
        for p in pvp_list:  #gives players pvp cards
            if p.player_owner == player1: player1.pvp_in_hand.append(p)
            if p.player_owner == player2: player2.pvp_in_hand.append(p)
            if p.player_owner == player3: player3.pvp_in_hand.append(p)
            if p.player_owner == player4: player4.pvp_in_hand.append(p)
        print("All Players have drawn 3 boy cards from the deck,\nand have 3 PvP cards in hand.")
        print("Starting Game...")
        delay()
        delay()
        clear_screen()

def check_decks():
    if len(game_deck) == 0: reshuffle()

def whos_turn():
    for i in player_list:
        if i.current_turn == True:
            current_player = i
            return current_player

def print_whos_turn():
    for i in player_list:
        if i.current_turn == True:
            current_player = i
            print(f"\n{Back.LIGHTBLACK_EX + Fore.BLUE}It is {current_player.playername}'s turn (Player {current_player.playernumber}).{Style.RESET_ALL}\n")
            return current_player

def set_number_of_players():
    print("How many players would like to play (1 - 4)?")
    while True:
        try:
            num = int(input())
            if num == 1:
                print("\nYou have selected 1 player.")
                delay()
            if num in range(2,4):
                print(f"\nYou have selected {num} players.")  # grammar motherfuckers!
                delay()
            number_of_players = int(num)
            for i in range(number_of_players):
                player_list.append(all_player_list[i])
            return number_of_players
        except: print("Please enter ('1','2','3' or '4') to select number of players.")

def name_players():
    for i in player_list:
        print(f"\nPlease give Player {i.playernumber} a name.")
        name = input()
        i.playername = name

    print("\nThe names you have chosen are:")
    short_delay()
    for i in player_list:
        print(f"Player {i.playernumber}, {i.playername}")
        short_delay()

def starting_player():
    if len(player_list) == 1:  #checks for one player mode
        for i in player_list:
            i.current_turn = True
            break
        return
    while True:
        print(f"\nPlease choose the starting player by entering their player number.")
        choice = input()
        if choice:
            if choice.lower() == "one": choice = 1
            if choice.lower() == "two": choice = 2
            if choice.lower() == "three": choice = 3
            if choice.lower() == "four": choice = 4
            if choice.isdigit() == True:
                for i in player_list:
                    if int(choice) == i.playernumber:
                        i.current_turn = True
                        print(f"Player {i.playernumber} will go first.")
                        short_delay()
                break
        else: print("Not a valid choice.")

def print_current_player_hand():
    print(whos_turn().playername,"'s current hand is:")
    for i in whos_turn().cardsinhand:
        print(str(i.name), "- Phone#:", (i.phonenum))
        short_delay()
    print("PvP:",end=" ")
    for i in whos_turn().pvp_in_hand:
        print(f"|{i.long_name}|",end=" ")
    print(end="\n")
    #print_current_curses()  testing routine, disabled for now

def print_current_curses():
    for i in whos_turn().cardsinhand:
        if len(i.curse_bucket) > 0:
            for c in i.curse_bucket:
                print(f"Your {i.name} card is cursed, curse applied by {c.player_owner.playername} with '{c.long_name}'")

def check_for_curse(last_dialed_boy):
    if len(last_dialed_boy.curse_bucket) > 0:
        for i in last_dialed_boy.curse_bucket:
            if i.type == "hangup":
                return mom_says_hang_up(last_dialed_boy) #end current turn and remove card, add message to players turn
            if i.type == "share_secret":
                return share_a_secret(last_dialed_boy) # continue to clue reveal but apply clue to both players, add message to player who applied curse, card goes into hand of cursed player
            if i.type == "speakerphone":
                return speakerphone(last_dialed_boy) #reveal to all, add message to other players, burn card
    else: return "no_curse"

def share_a_secret(last_dialed_boy):
    print(f"\nOh no! {last_dialed_boy.curse_bucket[0].player_owner.playername} "
          f" (Player {last_dialed_boy.curse_bucket[0].player_owner.playernumber}) has cursed your {last_dialed_boy.name} card with |Share a Secret|!\n")
    long_delay()
    print(Back.RED + Fore.WHITE,"Your revealed clue from",last_dialed_boy.name,\
    "will also be added to their notepad. However, you will gain possession of their expended |Share a Secret| PvP card.", Style.RESET_ALL, "\n")
    long_delay()
    long_delay()
    return "secret"

def mom_says_hang_up(last_dialed_boy):
    print(f"\nOh no! {last_dialed_boy.curse_bucket[0].player_owner.playername} "
          f" (Player {last_dialed_boy.curse_bucket[0].player_owner.playernumber}) has cursed your {last_dialed_boy.name}card with |Mom Says Hang Up|!\n")
    long_delay()
    print(Back.RED + Fore.WHITE,"You must discard your",last_dialed_boy.name,"and lose a turn.",Style.RESET_ALL,"\n")
    long_delay()
    long_delay()
    return "hangup"
def speakerphone(last_dialed_boy):
    print(f"Oh no! {last_dialed_boy.curse_bucket[0].player_owner.playername} "
          f"(Player {last_dialed_boy.curse_bucket[0].player_owner.playernumber}) has cursed your {last_dialed_boy.name} card with |Speakerphone|!")
    print(Back.RED + Fore.WHITE,"Your revealed clue from",last_dialed_boy.name,"will also be added to every player's notepad.",Style.RESET_ALL,"\n")
    long_delay()
    long_delay()
    return "speaker"

def use_pvp():   #this one is crazy
    opponent_list = copy.copy(player_list)
    opponent_list.remove(whos_turn())   #we need a list of players that doesn't include current player
    op_player_nums = []
    for i in opponent_list: op_player_nums.append(int(i.playernumber))  # making a bucket of all valid opponent player numbers
    op_player_names = []
    for i in opponent_list: op_player_names.append(i.playername)  # making a bucket of all valid opp player names
    op_player_names = [element.lower() for element in op_player_names]

    ###checks that the player can use PVP###
    if len(player_list) == 1: # halt unless at least a 2 player game
        print("You cannot use PvP Cards in a 1 player game.")
        return

    if whos_turn().pvp_this_turn == True: #halt if you have used a pvp card already this turn
        print("Cannot use more than one PvP card per turn.")
        return

    if whos_turn().pvp_this_turn == False:
        if len(whos_turn().pvp_in_hand) != 0:  #checks that hand is not empty
            print("Please select a PvP card to use (number input), or ('exit') to leave.")
        else:
            print("You have no PvP Cards to use.")
            return

    ###chosing a pvp card###
    for i in whos_turn().pvp_in_hand: print(f"{whos_turn().pvp_in_hand.index(i)} - |{i.long_name}|")   #prints out all the available pvp cards in hand

    valid_choice = False
    while valid_choice == False:  #loop that only breaks when valid choice in made
        choice = input()
        if choice == 'exit':   #leaves pvp
            print("\nExiting PvP.")
            return
        if choice.isdigit() == True:   #filters for num input
            if int(choice) not in range(int(len(whos_turn().pvp_in_hand))):  #if it's a num but not a possible correct one
                print("Entered number not in range of valid choices, try again.")   #print error
            for i in whos_turn().pvp_in_hand:   #iterate over your pvp hand
                if int(choice) == int(whos_turn().pvp_in_hand.index(i)):   #checks input against pvp cards
                    selected_pvp = whos_turn().pvp_in_hand[int(choice)]   #sets choice as var selected_pvp
                    print(f"\nYou chose |{selected_pvp.long_name}|\n")
                    valid_choice = True
                    break
        else: print("Please enter selection as a number. Try again.")

    ###chosing a player to use card on###
    print(f"Choose a player to curse with {selected_pvp.long_name}. Type name or number, or ('exit') to leave.")
    for i in opponent_list: print(i.playernumber,"-",i.playername)  #prints opponents

    valid_choice = False  #setting up a big loop defined of two little loops, number check and name check
    while valid_choice == False:  #do this until good name or num return
        choice = input()

        if choice == 'exit':
            print("\nExiting PvP.")
            return

        if choice.isdigit() == True:   #filters for input being a number
            if int(choice) not in op_player_nums:  # checks choice against valid player numbers
                print("Entered number not in range of valid choices, try again.")  # if not, throw an error
        if choice.isdigit() == False:
            if choice.lower() not in op_player_names:  # run choice against all possible opponent player names
                print("Invalid player name, try again.")  # if not, throw an error

        for i in opponent_list:   #look through opponent list
            if choice.isdigit() == True:   #if player enters a number
                if int(choice) == int(i.playernumber):  #if num entry is a valid opponent number
                    opponent_player = i #sets opponent_player as the number you selected from list
                    valid_choice = True #sets flag to leave big loop
                    break   #leaves opponent list loop
            else:   #if not a digit, then name
                if choice.lower() == i.playername.lower():  #seeing if you typed the player name instead of player number
                    opponent_player = i #sets opponent_player as the name player typed from list
                    valid_choice = True  #sets flag to leave big loop
                    break #leaves opponent list loop

    print(f"You have selected {opponent_player.playername}.\n")

    ###chosing which of your opponents cards to curse###

    op_player_card_names = []   #bucket for opponent player card names
    op_player_card_nums = []   #same for card numbers based on list index

    for i in opponent_player.cardsinhand: op_player_card_names.append(i.name)   #filling op_player_card_names bucket
    op_player_card_names = [element.lower() for element in op_player_card_names]   #making cardnames lowercase

    for i in opponent_player.cardsinhand: op_player_card_nums.append(opponent_player.cardsinhand.index(i)) #filling op_player_card_nums bucket

    print(f"Select a card of {opponent_player.playername}'s to curse. Type name or number, or ('exit') to leave.")
    for i in opponent_player.cardsinhand: print(f"{opponent_player.cardsinhand.index(i)} - |{i.name}|")  #list's the selected player's hand

    valid_choice = False
    while valid_choice == False:
        choice = input()
        if choice == 'exit': return

        if choice.isdigit() == True:
            if int(choice) not in op_player_card_nums:  # run choice against all possible opponent card nums
                print("Invalid Opponent Card number, try again.")  # if not, throw an error

        if choice.isdigit() == False:
            if choice.lower() not in op_player_card_names:
                print("Invalid Opponent Card name, try again.")

        for i in opponent_player.cardsinhand:
            if choice.isdigit() == True:
                if int(choice) == int(opponent_player.cardsinhand.index(i)):
                    selected_card = i  # sets var selected_card based on cards in hand index number
                    valid_choice = True
                    break
            else:
                if choice.lower() == str(i.name.lower()):  #seeing if you typed the player name instead of player number
                    selected_card = i
                    valid_choice = True
                    break
        if len(selected_card.curse_bucket) > 0:   #only allows one curse per card
            print("Sorry, this card is already cursed. Try again on another selection.")
            return

    whos_turn().pvp_this_turn = True   #makes it so players can only use once per turn, resets on end sequence
    print(f"\nYou have cursed {opponent_player.playername}'s '{selected_card.name}' Boy card with {selected_pvp.long_name}.")
    long_delay()
    selected_pvp.used_on.append(opponent_player)  # copying opponent player to pvp card attribute bucket "used on"...might not be helpful
    selected_card.curse_bucket.append(selected_pvp) #adds selected PVP to the opponent's card curse bucket
    whos_turn().pvp_in_hand.remove(selected_pvp) #removes pvp card from current hand
    print("The spent PvP card has been removed from your hand.")
    long_delay()

def call_number(choice):
    if whos_turn().dialed_this_turn == False:
        valid_call = False   #initalizes valid call var
        for i in whos_turn().cardsinhand:   #this checks if dial "boyname" or dial "phonenum" was entered
            if "dial" in choice and str(i.phonenum) in choice or "dial" in choice and str(i.name).lower() in choice:
                last_dialed_boy = i
                for x in range(0, 3):
                    print("*ring*")
                    short_delay()
                return last_dialed_boy

        print("You pick up the phone to make a call. Please enter a number (or name).")  #get message if dial + nothing useful is entered

        while True:
            dialed_number=input()   #prompts a second input loop to get a valid person to call
            if dialed_number == "leave":
                break

            for i in whos_turn().cardsinhand:
                if dialed_number == i.phonenum or dialed_number.lower() == i.name.lower():   #added name dial for Clarissa <3
                    for x in range(0,3):
                        print("*ring*")
                        short_delay()
                    delay()
                    last_dialed_boy = i
                    valid_call = True

            if valid_call is True and len(player_list) > 1:
                return last_dialed_boy

            if valid_call is not True:
                print("Wrong number. Try another number or dial ('leave') to exit.")
    else: print("Cannot dial twice in a single turn.")
def clue_reveal(last_dialed_boy):
    try:
        last_dialed_boy
    except NameError:
        last_dialed_boy = None
    if last_dialed_boy == None: return
    #rejection check:
    if last_dialed_boy.clue_to_reveal == card_list[crush].hangout\
    or last_dialed_boy.clue_to_reveal == card_list[crush].sport\
    or last_dialed_boy.clue_to_reveal == card_list[crush].food\
    or last_dialed_boy.clue_to_reveal == card_list[crush].clothing: #if the clue would reveal the crush's hangout, food etc
        response = "no_reveal"                                    #we do not give that information to the player

    #type of reveal check:
    no_crush_list = copy.copy(card_list)   #we need to look through all clues except for the crush's 'positive' clues
    remove_it = card_list[crush]           # so I copy the master card list and remove the crush entry from it
    no_crush_list.remove(remove_it)
    for i in no_crush_list:   #iterate through the whole no crush list, checking against what kind of clue it is
        if last_dialed_boy.clue_to_reveal == i.hangout: response = "hangout_reveal"   #and set the type of response
        if last_dialed_boy.clue_to_reveal == i.sport: response = "sport_reveal"
        if last_dialed_boy.clue_to_reveal == i.food: response = "food_reveal"
        if last_dialed_boy.clue_to_reveal == i.clothing: response = "clothing_reveal"

#### player vs player effects when dialed ####

    curse_mod = check_for_curse(last_dialed_boy)

    #if curse_mod == "speaker":
    if curse_mod == "hangup":
        last_dialed_boy.curse_bucket.remove(last_dialed_boy.curse_bucket[0])   #deletes the curse from the game
        dialed_discard(last_dialed_boy)   #runs the discard script and skips clue reveal
        return #nreaks out of current routine

    if last_dialed_boy.first_call == True:   #checks if this is your first time calling them
        print(blue_out(f"Hello? This is {last_dialed_boy.name}. You want to know about your crush?"))
        long_delay()
    if last_dialed_boy.first_call == False:   #if not first time, increase snark
        print(blue_out("You again? I already told you..."))
        long_delay()
    #loud repsonses, everyone hears
    if response == "hangout_reveal": print(blue_out("I know where he hangs out,"))
    if response == "sport_reveal": print(blue_out("He is very athletic,"))
    if response == "food_reveal": print(blue_out("He eats a lot of food,"))
    if response == "clothing_reveal": print(blue_out("He looks good in whatever he wears,"))
    long_delay()

    #quiet response, only player hears
    grammar = ""
    if last_dialed_boy.clue_to_reveal == "Hat" or "Jacket" or "Tie": grammar = "a"
    else: grammar = ""

    if response == "hangout_reveal": print(red_out(f"but he doesn't hang out at {last_dialed_boy.clue_to_reveal}."), "\n")
    if response == "sport_reveal": print(red_out(f"but he doesn't like {last_dialed_boy.clue_to_reveal.lower()}."), "\n")
    if response == "food_reveal": print(red_out(f"but he hates the taste of {last_dialed_boy.clue_to_reveal.lower()}."), "\n")
    if response == "clothing_reveal": print(red_out(f"but he doesn't wear {grammar} {last_dialed_boy.clue_to_reveal.lower()}."), "\n")

    whos_turn().collected_clues.append(last_dialed_boy)   #add clue to notepad

    if curse_mod == "secret":
        also_give_clue = last_dialed_boy.curse_bucket[0].player_owner
        also_give_clue.collected_clues.append(last_dialed_boy) #player who used curse card gets clue
        whos_turn().pvp_in_hand.append(last_dialed_boy.curse_bucket[0])   #copy pvp card to whosturn
        last_dialed_boy.curse_bucket.remove(last_dialed_boy.curse_bucket[0])  #remove curse card from boy card
        for i in whos_turn().pvp_in_hand:
            i.player_owner = whos_turn()   #brute force changes the owner flag of the pvp cards in who's turn hand

    if curse_mod == "speaker":
        for i in player_list:
            i.collected_clues.append(last_dialed_boy)   #give clue to all players in the game
        last_dialed_boy.curse_bucket.remove(last_dialed_boy.curse_bucket[0])   #delete the speakerphone card from the game

        #pvp card changes hand and owner assignment
    last_dialed_boy.first_call = False  #this is where redial snark is set

    choice = "null"
    long_delay()
    return choice

def dialed_discard(last_dialed_boy):
    if whos_turn().dialed_this_turn == False:
        i = whos_turn().cardsinhand.index(last_dialed_boy)
        print(f"{last_dialed_boy.name} from your hand has been discarded.")
        discard_pile.append(whos_turn().cardsinhand.pop(i))  # adds card to discard pile based on in_hand index num
        if len(player_list) > 1: whos_turn().dialed_this_turn = True

def dialed_draw():
    if len(whos_turn().cardsinhand) < 3:
        whos_turn().cardsinhand.append(game_deck.pop(0))
        print(whos_turn().playername, "drew a card.")
        choice = "null"
        return choice

def end_turn(number_of_players):
    former_player = whos_turn()  #once whos_turn().current_turn is false, it breaks function call, need to get the iteration
                                # of the player cuurrently to make dialed this turn and guess this turn work
    if number_of_players > 1:
        for i in range(len(player_list)):   #iterates over all index numbers in player list var
            if player_list[i] == whos_turn():   #if i is the index number of the item matching current player:
                current_player_num = i  #sets var current_player_num to correct index number
        if current_player_num == len(player_list) - 1: #checks if player rotation has reached end of list
            next_player_num = 0 #sets the next player to start at list beginning
        else:
            next_player_num = current_player_num + 1    #not at end of the list, set next player num to advance by 1
        print("Ending", whos_turn().playername, "'s turn.")
        delay()
        whos_turn().current_turn = False    #turns off current player turn flag
        former_player.dialed_this_turn = False #allows this player to dial again next turn
        former_player.guessed_this_turn = False #allows player ending turn to guess next turn
        former_player.pvp_this_turn = False #resets ability to use PvP again
        print("next player up:",player_list[next_player_num].playername)
        delay()
        player_list[next_player_num].current_turn = True    #turns on next player turn flag

        for i in card_list:     #Reset redial flag when players swap
            i.first_call = True
        clear_screen()

def count():
    print(f"\n====Status====")
    short_delay()
    print(f"Draw Pile: {len(game_deck)}")
    short_delay()
    print(f"{whos_turn().playername}'s Hand: {len(whos_turn().cardsinhand)}")
    short_delay()
    print(f"Discard Pile: {len(discard_pile)}")
    short_delay()

def solve(crush, number_of_players):
    if whos_turn().guessed_this_turn == True:
        print("You cannot guess more than once per turn.")
        return
    print("You think you know who your crush is, huh?\nType your guess to check (name or phone#).\nYou can also look at your notebook by entering ('notebook').")
    crush_object = card_list[crush]
    valid_solve_input = False
    while True:
        solve_choice = input().lower()
        for i in card_list:
            if solve_choice == crush_object.phonenum or solve_choice == crush_object.name.lower():
                result = "crush"
                break
            if solve_choice == i.phonenum or solve_choice == i.name.lower():
                result = "valid"
                break
            else: result = "invalid"
        if result == "invalid": print("invalid input. Try again.")
        if result == "crush":
            long_delay()
            print(f"{crush_object.name} is your crush!\n")
            print(f"Congratulations! {whos_turn().playername} (Player {whos_turn().playernumber}) has won the game.")
            long_delay()
            print("Game Over!")
            print("Thank you for playing! I hope you had fun. \n                                  - Old Kid")
            long_delay()
            long_delay()
            if number_of_players > 1: whos_turn().guessed_this_turn = True
            return
        if result == "valid":
            print("Wrong boy, try again!")
            if number_of_players > 1: whos_turn().guessed_this_turn = True
            return

def shuffle():  # shuffles the game deck
    random.shuffle(game_deck)
    print("\nCards in the game deck have been shuffled.")
    delay()

def reshuffle():
    if len(discard_pile) == 0: # check that discard pile is not empty
        print("There's nothing in the discard pile to shuffle back into the deck.")
    else:
        for i in range(len(discard_pile)): #does an i loop based on the number of items in the discard pile
            game_deck.append(discard_pile.pop(0)) #adds the discard pile back into the game deck
        random.shuffle(game_deck)
        print("/n",blue_out("The discard pile has been shuffled back to the draw pile."),"\n")

# now on to the main loop. it simply checks for inputs to run the outlined functions. nothing too crazy

def game_loop():
    crush = new_game_crush()
    valid_choices=["null","notepad","dial","end","count","redial","solve", "pvp"] # commands that work at start
    print("\nWelcome to Dream Phone Simulator Version 0.1, a computer simulation of the 1991 board game 'Dreamphone'. \
          \nPlease see included dp_instructions.txt for more information.\n")
    delay()
    number_of_players = set_number_of_players()
    name_players()
    delay()
    starting_player()
    shuffle()
    starting_deal()
    while True:
        print_whos_turn()
        print_current_player_hand()
        check_decks()
        print (white_out("Commands: ('dial') - ('notepad') - ('pvp') - ('solve') - ('redial') - ('end')"),"\n")
        choice = input().lower()

        if 'dial' in choice and choice != 'redial':
            last_dialed_boy = call_number(choice)
            clue_reveal(last_dialed_boy)
            dialed_discard(last_dialed_boy)
            dialed_draw()
            choice = "null"

        if choice not in valid_choices:
            print("Not a valid choice.")

        else:
            if choice == 'solve': solve(crush, number_of_players)
            if choice == 'count':count()
            if choice == 'pvp': use_pvp()
            if choice == 'show':
                show_deck()
                show_hand()
                show_discard()
            if choice == 'redial':
                try: last_dialed_boy
                except NameError: last_dialed_boy = None
                if last_dialed_boy == None: print("no call made yet")
                if last_dialed_boy != None:
                    print(f"The last boy you called was {last_dialed_boy.name}. His number was {last_dialed_boy.phonenum}.")
                    clue_reveal(last_dialed_boy)
            if choice == 'notepad': boy_attribute_table()
            if choice == 'end': end_turn(number_of_players)

game_loop()
