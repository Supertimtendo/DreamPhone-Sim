import random
import copy
import time
from prettytable import PrettyTable    #this helps build BOY ATTRIBUTE TABLE
import colorama #fixes windows shell color bugs
from colorama import Fore, Back, Style #gives us come color options
### installing colorama: pip install colorama
### installing prettytable: python -m pip install -U prettytable

colorama.init() #turns on windows shell fix

class Player:  #class Player constructor
    def __init__(self, playernumber, cardsinhand, current_turn, playername, collected_clues, dialed_this_turn, guessed_this_turn, pvp_in_hand):
        self.playernumber = playernumber    #Class Player gets a "playernumber" attribute
        self.cardsinhand = cardsinhand      #Class Player gets a "cardsinhand" attribute
        self.current_turn = current_turn      #gives a boolean flag for if the player is currently playing or not
        self.playername = playername        #gives players a name attribute in the class
        self.collected_clues = collected_clues #where the information goes that the player collects
        self.dialed_this_turn = dialed_this_turn #a flag for limiting 1 dial per turn
        self.guessed_this_turn = guessed_this_turn #only one guess per turn flag
        self.pvp_in_hand = pvp_in_hand

player1 = Player(1,[],False,"",[],False,False,[])
player2 = Player(2,[],False,"",[],False,False,[])
player3 = Player(3,[],False,"",[],False,False,[])
player4 = Player(4,[],False,"",[],False,False,[])

all_player_list=[player1,player2,player3,player4]  #all possible players in the game
player_list=[]  #a list built out by the player's choice of player num
crush=0  #initalizes game crush global var

class Cards:  #class Cards constructor
    def __init__(self, name, phonenum, hangout, sport, food, clothing, clue_to_reveal, first_call):
        self.name = name    #Class Cards gets a "name" attribute
        self.phonenum = phonenum  #Card objects have stuff
        self.hangout = hangout
        self.sport = sport
        self.food = food
        self.clothing = clothing
        self.clue_to_reveal = clue_to_reveal #this is where the clues that are revealed in the game assoicate with cards to dial
        self.first_call = first_call #a flag to show if the card has been dialed before

#building Cards objects:
c0 = Cards("Dave","555-1111","Crosstown Mall","null","Cookies","Blue Jeans","",True)
c1 = Cards("George","555-1233","Crosstown Mall","null","Ice Cream","Tie","",True)
c2 = Cards("Dale","555-4566","Crosstown Mall","null","Ice Cream","Jacket","",True)
c3 = Cards("Alan","555-7899","Crosstown Mall","null","Cookies","Tie","",True)
c4 = Cards("James","555-2588","E.A.T.S. Snack Shop","null","Hot Dogs","Jacket","",True)
c5 = Cards("Phil","555-3333","E.A.T.S. Snack Shop","null","Pizza","Glasses","",True)
c6 = Cards("Bruce","555-3699","E.A.T.S. Snack Shop","null","Pizza","Tie","",True)
c7 = Cards("Tyler","555-1477","E.A.T.S. Snack Shop","null","Hot Dogs","Blue Jeans","",True)
c8 = Cards("Jamal","555-9877","Reel Movies","null","Candy","Tie","",True)
c9 = Cards("Gary","555-3211","Reel Movies","null","Popcorn","Blue Jeans","",True)
c10 = Cards("Dan","555-7777","Reel Movies","null","Candy","Blue Jeans","",True)
c11 = Cards("Spencer","555-6544","Reel Movies","null","Popcorn","Jacket","",True)
c12 = Cards("Mark","555-8522","Woodland Park","Baseball","null","Hat","",True)
c13 = Cards("Jason","555-7411","Woodland Park","Baseball","null","Glasses","",True)
c14 = Cards("Steve","555-9999","Woodland Park","Skateboarding","null","Jacket","",True)
c15 = Cards("John","555-9633","Woodland Park","Skateboarding","null","Anything Yellow","",True)
c16 = Cards("Paul","555-5515","High Tide Beach","Volleyball","null","Anything Yellow","",True)
c17 = Cards("Tony","555-2442","High Tide Beach","Volleyball","null","Hat","",True)
c18 = Cards("Wayne","555-3535","High Tide Beach","Surfing","null","Anything Yellow","",True)
c19 = Cards("Mike","555-2226","High Tide Beach","Surfing","null","Hat","",True)
c20 = Cards("Scott","555-5599","Jim's Gym","Basketball","null","Anything Yellow","",True)
c21 = Cards("Bob","555-4884","Jim's Gym","Basketball","null","Glasses","",True)
c22 = Cards("Carlos","555-6668","Jim's Gym","Tennis","null","Hat","",True)
c23 = Cards("Matt","555-7557","Jim's Gym","Tennis","null","Glasses","",True)

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

#Text Speed Delay Settings
def delay():
    time.sleep(.5)
def short_delay():
    time.sleep(.2)
def long_delay():
    time.sleep(1)

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
    print(notepad)  #prints notepad
    input("Press Enter to continue...")

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
            print(f"\nIt is {current_player.playername}'s turn (Player {current_player.playernumber}).\n")
            return current_player

def set_number_of_players():
    print("How many players would like to play (1 - 4)?")
    while True:
        try:
            num = int(input())
            if num == 1: print("You have selected 1 player.")
            if num in range(2,4): print(f"You have selected {num} players.")  # grammar motherfuckers!
            number_of_players = int(num)
            for i in range(number_of_players):
                player_list.append(all_player_list[i])
            return number_of_players
        except: print("Please enter ('1','2','3' or '4') to select number of players.")




def name_players():
    for i in player_list:
        print(f"Please give Player {i.playernumber} a name.")
        name = input()
        i.playername = name

    print("The names you have chosen are:")
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
        print(f"Choose which player wants to start 1 to {len(player_list)}?")
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

def use_pvp():
    if len(player_list) > 1:   #checks for 2 or more player game
        if len(whos_turn().pvp_in_hand) != 0:  #checks that hand is not empty
            print("Please select a PvP card to use.")
            for i in whos_turn().pvp_in_hand:
                print(f"{whos_turn().pvp_in_hand.index(i)} - {i.long_name}")

            while True:
                try:
                    choice = int(input())
                    for i in whos_turn().pvp_in_hand:
                        if choice == int(whos_turn().pvp_in_hand.index(i)):
                            selected_pvp = whos_turn().pvp_in_hand[choice]
                            print("You chose",selected_pvp.long_name,"\n")
                    break
                except: print("Invalid choice.")

        print(f"Choose a player to curse with {selected_pvp.long_name}.")
        opponent_list = copy.copy(player_list)
        opponent_list.remove(whos_turn())
        for i in opponent_list: print(i.playernumber,"-",i.playername)

        for i in opponent_list:
            while True:
                try:
                    choice = input()
                    if choice.isnumeric() == True:
                        if int(choice) == int(i.playernumber):
                            selected_player = i
                            break
                        else: print("Invalid Number.")
                    else:
                        if choice.lower() == str(i.playername.lower()):
                            selected_player = i
                            break
                        else: print("Invalid name.")
                except: print("Not a valid player choice.")

        print(f"You have selected {selected_player.playername}.")
        print(f"Select a card of {selected_player.playername}'s to curse.")
        for i in selected_player.cardsinhand:
            print (selected_player.cardsinhand.index(i), i.name)



def call_number(choice):
    if whos_turn().dialed_this_turn == False:
        valid_call = ()   #initalizes valid call var
        for i in whos_turn().cardsinhand:   #this checks if dial "boyname" or dial "phonenum" was entered
            if "dial" in choice and str(i.phonenum) in choice or "dial" in choice and str(i.name).lower() in choice:
                last_dialed_boy = i
                return last_dialed_boy

        print("You pick up the phone to make a call. Please enter a number (or name).")  #get message if dial + nothing useful is entered

        while True:
            dialed_number=input()   #prompts a second input loop to get a valid person to call
            if dialed_number == "leave":
                break

            for i in whos_turn().cardsinhand:
                if dialed_number == i.phonenum or dialed_number.lower() == i.name.lower():   #added name dial for Clarissa <3
                    for x in range(0,3):
                        print("ring")
                        short_delay()
                    delay()
                    last_dialed_boy = i
                    valid_call = True

            if valid_call is True and len(player_list) > 1:
                whos_turn().dialed_this_turn = True
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
    #redial modifier in card class

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
    whos_turn().collected_clues.append(last_dialed_boy)
    last_dialed_boy.first_call = False  #this is where redial snark is set
    choice = "null"
    long_delay()
    return choice

def dialed_discard(last_dialed_boy):
    if whos_turn().dialed_this_turn == False:
        i = whos_turn().cardsinhand.index(last_dialed_boy)
        print(f"{last_dialed_boy.name} from your hand has been discarded.\nHis clue information has been added to your Notepad.\n")
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
        print("next player up:",player_list[next_player_num].playername)
        delay()
        player_list[next_player_num].current_turn = True    #turns on next player turn flag

        for i in card_list:     #Reset redial flag when players swap
            i.first_call = True

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
            long_delay()
            print("Game over! but not really i'm still working on the program.")
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
    print("\nCards in the game deck have been shuffled. ")
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
    print("\nWelcome to Dream Phone Simulator. This is incomplete but getting better!\n")
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
        print (white_out("Commands: ('dial') - ('notepad') - ('pvp') - ('solve') - ('redial) - ('end')"),"\n")
        choice = input().lower()

        if 'dial' in choice and choice != 'redial':
            last_dialed_boy = call_number(choice)
            choice = clue_reveal(last_dialed_boy)
            dialed_discard(last_dialed_boy)
            choice = dialed_draw()

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
