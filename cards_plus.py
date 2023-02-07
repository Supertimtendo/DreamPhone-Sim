import random
import copy
import time
from prettytable import PrettyTable    #this helps build BOY ATTRIBUTE TABLE
import colorama #fixes windows shell color bugs
from colorama import Fore, Back, Style #gives us come color options

colorama.init() #turns on windows shell fix

class Player:  #class Player constructor
    def __init__(self, playernumber, cardsinhand, current_turn, playername, collected_clues, dialed_this_turn):
        self.playernumber = playernumber    #Class Player gets a "playernumber" attribute
        self.cardsinhand = cardsinhand      #Class Player gets a "cardsinhand" attribute
        self.current_turn = current_turn      #gives a boolean flag for if the player is currently playing or not
        self.playername = playername        #gives players a name attribute in the class
        self.collected_clues = collected_clues #where the information goes that the player collects
        self.dialed_this_turn = dialed_this_turn #a flag for limiting 1 move per turn

player1 = Player(1,[],False,"",[],False)
player2 = Player(2,[],False,"",[],False)
player3 = Player(3,[],False,"",[],False)
player4 = Player(4,[],False,"",[],False)

all_player_list=[player1,player2,player3,player4]
player_list=[]

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
c0 = Cards("Dave","5551111","Crosstown Mall","null","Cookies","Blue Jeans","",True)
c1 = Cards("George","5551233","Crosstown Mall","null","Ice Cream","Tie","",True)
c2 = Cards("Dale","5554566","Crosstown Mall","null","Ice Cream","Jacket","",True)
c3 = Cards("Alan","5557899","Crosstown Mall","null","Cookies","Tie","",True)
c4 = Cards("James","5552588","E.A.T.S. Snack Shop","null","Hot Dogs","Jacket","",True)
c5 = Cards("Phil","5553333","E.A.T.S. Snack Shop","null","Pizza","Glasses","",True)
c6 = Cards("Bruce","5553699","E.A.T.S. Snack Shop","null","Pizza","Tie","",True)
c7 = Cards("Tyler","5551477","E.A.T.S. Snack Shop","null","Hot Dogs","Blue Jeans","",True)
c8 = Cards("Jamal","5559877","Reel Movies","null","Candy","Tie","",True)
c9 = Cards("Gary","5553211","Reel Movies","null","Popcorn","Blue Jeans","",True)
c10 = Cards("Dan","5557777","Reel Movies","null","Candy","Blue Jeans","",True)
c11 = Cards("Spencer","5556544","Reel Movies","null","Popcorn","Jacket","",True)
c12 = Cards("Mark","5558522","Woodland Park","Baseball","null","Hat","",True)
c13 = Cards("Jason","5557411","Woodland Park","Baseball","null","Glasses","",True)
c14 = Cards("Steve","5559999","Woodland Park","Skateboarding","null","Jacket","",True)
c15 = Cards("John","5559633","Woodland Park","Skateboarding","null","Anything Yellow","",True)
c16 = Cards("Paul","5555515","High Tide Beach","Volleyball","null","Anything Yellow","",True)
c17 = Cards("Tony","5552442","High Tide Beach","Volleyball","null","Hat","",True)
c18 = Cards("Wayne","5553535","High Tide Beach","Surfing","null","Anything Yellow","",True)
c19 = Cards("Mike","5552226","High Tide Beach","Surfing","null","Hat","",True)
c20 = Cards("Scott","5555599","Jim's Gym","Basketball","null","Anything Yellow","",True)
c21 = Cards("Bob","5554884","Jim's Gym","Basketball","null","Glasses","",True)
c22 = Cards("Carlos","5556668","Jim's Gym","Tennis","null","Hat","",True)
c23 = Cards("Matt","5557557","Jim's Gym","Tennis","null","Glasses","",True)

##global stuff##
card_list = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20,c21,c22,c23]
# this is the master list of cards in the deck. a way to reference a var list containing all card object names.
# tried to find a less brute force way to do this but so far no luck.

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
def red_out(text): #red_out is how i am crossing out entries in the BAT
    return Back.RED + Fore.WHITE + text + Style.RESET_ALL
def white_out(text): #red_out is how i am crossing out entries in the BAT
    return Back.WHITE + Fore.BLACK + text + Style.RESET_ALL

def boy_attribute_table():   #this is an automated notepad of the clues you have crossed off the list. player specific
    b_a_t = PrettyTable(["Called?", "Hangout", "Sport \ Food", "Clothing", "Secret Admirer?"]) # Specify the Column Names while initializing the Table
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
        b_a_t.add_row([name,hangout, sport+food, clothing, listname])   #adds rows qeued up for printing
    b_a_t.align="l"   #aligns the table to the left
    print(b_a_t)  #prints BAT
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
    for i in range (3):
        for f in player_list:
            f.cardsinhand.append(game_deck.pop(0))
    if len(player_list) == 1: print()
    print("All Players have drawn 3 cards from the deck.")

def whos_turn():
    for i in player_list:
        if i.current_turn == True:
            current_player = i
            return current_player

def print_whos_turn():
    for i in player_list:
        if i.current_turn == True:
            current_player = i
            print(f"\nIt is {current_player.playername}'s turn (Player {current_player.playernumber}).")
            return current_player

def set_number_of_players():
    print("How many players would like to play (1 - 4)?")
    while True:
        num = input()
        if num == "1" or "2" or "3" or "4":
            print(f"you have selected {num} players.")
            number_of_players = int(num)
            for i in range(number_of_players):
                player_list.append(all_player_list[i])
                print
            return number_of_players
    else: print("Invalid choice.")
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

def call_number(choice):
    current_player = whos_turn()
    print(current_player.playername,"testing dialed this turn filter")
    print(current_player.dialed_this_turn, "testing dialed this turn filter")

    if current_player.dialed_this_turn == False:
        valid_call = ()   #initalizes valid call var
        for i in current_player.cardsinhand:   #this checks if dial "boyname" or dial "phonenum" was entered
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

            if valid_call is True:
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
        print(f"Hello? This is {last_dialed_boy.name}. You want to know about your crush?")
        long_delay()
    if last_dialed_boy.first_call == False:   #if not first time, increase snark
        print("You again? I already told you...")
        long_delay()
    #loud repsonses, everyone hears
    if response == "hangout_reveal": print("I know where he hangs out,")
    if response == "sport_reveal": print("He is very athletic,")
    if response == "food_reveal": print("He eats a lot of food,")
    if response == "clothing_reveal": print("He looks good in whatever he wears,")
    long_delay()


    #quiet response, only player hears
    grammar = ""
    if last_dialed_boy.clue_to_reveal == "Hat" or "Jacket" or "Tie": grammar = "a"
    else: grammar = ""

    if response == "hangout_reveal": print(white_out(f"but he doesn't hang out at {last_dialed_boy.clue_to_reveal}."))
    if response == "sport_reveal": print(white_out(f"but he doesn't like {last_dialed_boy.clue_to_reveal.lower()}."))
    if response == "food_reveal": print(white_out(f"but he hates the taste of {last_dialed_boy.clue_to_reveal.lower()}."))
    if response == "clothing_reveal": print(white_out(f"but he doesn't wear {grammar} {last_dialed_boy.clue_to_reveal.lower()}."))
    whos_turn().collected_clues.append(last_dialed_boy)
    last_dialed_boy.first_call = False  #this is where redial snark is set
    choice = "dial"
    long_delay()
    return choice

def dialed_discard(last_dialed_boy):
    if current_player.dialed_this_turn == True:
        i = whos_turn().cardsinhand.index(last_dialed_boy)
        print(f"{last_dialed_boy.name} from your hand has been discarded.")
        discard_pile.append(whos_turn().cardsinhand.pop(i))  # adds card to discard pile based on in_hand index num

def dialed_draw():
    whos_turn().cardsinhand.append(game_deck.pop(0))
    print(whos_turn().playername, "drew a card.")

def end_turn(number_of_players):
    current_player = whos_turn()
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
        current_player.dialed_this_turn = False #allows this player to dial again next turn
        print("next player up:",player_list[next_player_num].playername)
        delay()
        player_list[next_player_num].current_turn = True    #turns on next player turn flag

        for i in card_list:     #Reset redial flag when players swap
            i.first_call = True

def shuffle():  # shuffles the game deck
    random.shuffle(game_deck)
    print("\nCards in the game deck have been shuffled. \n")
    delay()

def reshuffle():
    if len(discard_pile) == 0: # check that discard pile is not empty
        print("There's nothing in the discard pile to shuffle back into the deck.")
    else:
        for i in range(len(discard_pile)): #does an i loop based on the number of items in the discard pile
            game_deck.append(discard_pile.pop(0)) #adds the discard pile back into the game deck
        random.shuffle(game_deck)
        print("The discard pile has been shuffled back to the draw pile.\n")

# now on to the main loop. it simply checks for inputs to run the outlined functions. nothing too crazy

def game_loop():
    valid_choices=["bat","redial","dial","end","look","shuffle","draw","discard","discard choice","reshuffle","count","show","count deck","count hand","count discard","show deck","show hand","show discard","more"]
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
        print (Back.WHITE + Fore.BLACK + "Commands: ('dial') - ('bat') - ('end') - ('more')" + Style.RESET_ALL)
        choice = input().lower()

        if 'dial' in choice:
            last_dialed_boy = call_number(choice)
            choice = clue_reveal(last_dialed_boy)
            dialed_discard(last_dialed_boy)
            dialed_draw()
            #end_turn(number_of_players)


        if choice not in valid_choices:
            print("Not a valid choice.\n")

        else:
            if choice == 'draw':
                print("how many cards would you like to draw?")
                num_count = ask_for_num()
                if num_count == "back" or 0:
                    continue
                else:
                    draw(num_count)

            if choice == 'discard':
                print("how many cards would you like to discard?")
                num_count = ask_for_num()
                if num_count == 'back' or num_count == '0':
                    continue
                else:
                    discard(num_count)

            if choice == 'discard choice':
                discard_choice()

            if choice == 'count':
                count_deck()
                count_hand()
                count_discard()

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
            if choice == 'bat': boy_attribute_table()
            if choice == 'reshuffle': reshuffle()
            if choice == 'shuffle': shuffle()
            if choice == 'count deck': count_deck()
            if choice == 'count hand': count_hand()
            if choice == 'count discard': count_discard()
            if choice == 'show deck': show_deck()
            if choice == 'show hand': show_hand()
            if choice == 'show discard': show_discard()
            if choice == 'look': look()
            if choice == 'end': end_turn()

            if choice == 'more':
                print("More commands: ('shuffle') - ('draw') - ('discard') - ('end') - ('discard choice') - ('reshuffle') - You can type 'show' or 'count' to show or count your hand, draw pile and discard pile. Using 'show' or 'count' plus 'hand', 'deck' or 'discard' will display or count the individual respective stacks.")

crush = new_game_crush()
game_loop()
#boy_attribute_table()

# I need to figure out how I want to do loud / quiet stuff with the text parser - might not be possible? focus on single player? / make pico dreamphone? I think i should
# at least program the effect -"this part is quiet", "this part is loud" to practice the logic before i get sound involved. need to take recordings of dreamphone repsonses - maybe move project
# to a website to act as phone (use a cellphone) and use real feelie cards /etc... i dunno hitting a logistical wall

###moving outdated functions down here###
#the following stuff is just to give some text feedback in the test program, not too interesting.
def call_number(choice):
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

        if valid_call is True:
            return last_dialed_boy

        if valid_call is not True:
            print("Wrong number. Try another number or dial ('leave') to exit.")
def count():
    #print("====Status====\nDraw Deck:",len(game_deck),"\nHand:",len(in_hand),"\nDiscard:",len(discard_pile),"\n")
    print(f"\n====Status====")
    short_delay()
    print(f"Draw Deck: {len(game_deck)}")
    short_delay()
    print(f"{whos_turn().playername}'s Hand: {len(whos_turn().cardsinhand)}")
    short_delay()
    print(f"Discard: {len(discard_pile)}")
    short_delay()
def look():
    if len(whos_turn().cardsinhand) == 0:
        print("There are no cards in your hand.\n")
    else:
        print(whos_turn().playername,"looks closely at the cards in their hand.")
        for i in whos_turn().cardsinhand:
            print(str(i.name),"- Phone#:",(i.phonenum))
            short_delay()
    delay
def show_deck():
    if len(game_deck) == 0:
        print ("There are no cards in the draw deck.\n")
    else:
        print("The cards in the deck are:")
        for i in game_deck: print(i.name)
def count_deck():
    if len(game_deck) == 0:
        print ("There are no cards in the draw deck.\n")
    else:
        print("The number of cards in the draw deck are:", len(game_deck))
def show_hand():
    if len(whos_turn().cardsinhand) == 0:
        print("There are no cards in your hand.\n")
    else:
        print("Cards in", whos_turn().playername, "'s hand are:")
        for i in whos_turn().cardsinhand:
            print (i.name)
            short_delay()
    for i in whos_turn().collected_clues:
        print ("clues you got:", i.name)
def show_discard():
    if len(discard_pile) == 0:
        print ("There are no cards in the discard pile.\n")
    else:
        print("The cards in the discard pile are:")
        for i in discard_pile: print(i.name)
def count_hand():
    if len(whos_turn().cardsinhand) == 0:
        print ("There are no cards in your hand.\n")
    else:
        print("number of cards in your hand are:", len(whos_turn().cardsinhand))
def count_discard():
    if len(discard_pile) == 0:
        print ("There are no cards in the discard pile.\n")
        delay()
    else:
        print("number of cards in the discard pile:", len(discard_pile))
        delay()
def discard_choice():
    loop = 1
    while loop == 1:
        if len(whos_turn().cardsinhand) == 0:  # check that your hand is not empty
            print("you have no cards to discard.")
            delay()
            break
        else:
            show_hand()
            print("Please choose the card you wish to discard, or type 'back' to leave.")
            card_choice = input().lower() #which card do you want to discard?
            if card_choice == 'back': #gives a way to back out of the discard choice loop
                print("Exiting discard choice...")
                break #leaves discard choice loop
            else:
                for i in range(len(whos_turn().cardsinhand)):  #runs through the list count of in_hand
                    if card_choice == (whos_turn().cardsinhand[i].name.lower()): #checks if choice is in your hand
                        print(whos_turn().cardsinhand[i].name,"from your hand has been discarded.")
                        discard_pile.append(whos_turn().cardsinhand.pop(i)) #adds card to discard pile based on in_hand index num
                        loop = 0
                        delay()
                        break
                else: #if not 0 cards and if not a in_hand[i].name, incorrect choice
                    print ("Incorrect choice.")
def draw(num_count):  # function to move cards from the game deck into your hand
    if len(game_deck) == 0: #checks for an empty draw deck and displays an error if you draw from it
        print("Cannot draw any cards, the deck is empty.\n")
    else:
        if int(len(game_deck)) < num_count: #checks that you aren't trying to draw more cards than exist in the deck
            print("You can't draw more cards than the deck contains.\n")
        else:
            print(whos_turn().playername, "drew", num_count, "cards.")
            for i in range(num_count):  # I counts the number of draw_count specified
                whos_turn().cardsinhand.append(game_deck.pop(0))
    show_hand()
def discard(num_count):
    if len(whos_turn().cardsinhand) == 0:  # check that your hand is not empty
        print("you have no cards to discard.")
        delay()
    else:
        if int(len(whos_turn().cardsinhand)) < num_count: #checks that you aren't trying to discard more cards than are in your hand
            print("You cannot discard more cards than you have in hand.")
        else:
            print("You are discarding", num_count, "cards.")
            for i in range(num_count):  # i counts the number of discard_count specified
                discard_pile.append(whos_turn().cardsinhand.pop(i)) #moves in hand card to discard pile
def ask_for_num():
    print("Type 'back' or '0' to leave.")
    while True: #starts the loop
        i = input() #asks for player input
        if i: #this is a trick to validate against null entires (accidentally hitting enter)
            if i == 'back': #gives a way out
                print("No cards selected.")
                return i #returns i to the main program as 'back'
            if i.isdigit() == True: #checks if the user input is a number
                if i == 0: #checks for 0 entry
                    print("No cards selected.")
                else:
                    return int(i)  # returns either valid number or 0
            if i.isdigit() == False:
                print("Incorrect entry. Please enter a number, or type 'back' or '0' to leave.")

        else: #if not i, then print error instead of passing junk
            print("Incorrect entry. Please enter a number, or type 'back' or '0' to leave.")