import random
import copy
import time
class Player:  #class Player constructor
    def __init__(self, playernumber, cardsinhand, current_turn, playername):
        self.playernumber = playernumber    #Class Player gets a "playernumber" attribute
        self.cardsinhand = cardsinhand      #Class Player gets a "cardsinhand" attribute
        self.current_turn = current_turn      #gives a boolean flag for if the player is currently playing or not
        self.playername = playername        #gives players a name attribute in the class

class Cards:  #class Cards constructor
    def __init__(self, name, phonenum, hangout, sport, food, clothing, clue_to_reveal):
        self.name = name    #Class Cards gets a "name" attribute
        self.phonenum = phonenum  #Class Cards gets a "detail" attribute
        self.hangout = hangout
        self.sport = sport
        self.food = food
        self.clothing = clothing
        self.clue_to_reveal = clue_to_reveal
    def look(self):
        print(self.name, self.phonenum)

#building Cards objects:
c0 = Cards("Dave","5551111","Crosstown Mall","null","Cookies","Blue Jeans","")
c1 = Cards("George","5551233","Crosstown Mall","null","Ice Cream","Tie","")
c2 = Cards("Dale","5554566","Crosstown Mall","null","Ice Cream","Jacket","")
c3 = Cards("Alan","5557899","Crosstown Mall","null","Cookies","Tie","")
c4 = Cards("James","5552588","E.A.T.S. Snack Shop","null","Hot Dogs","Jacket","")
c5 = Cards("Phil","5553333","E.A.T.S. Snack Shop","null","Pizza","Glasses","")
c6 = Cards("Bruce","5553699","E.A.T.S. Snack Shop","null","Pizza","Tie","")
c7 = Cards("Tyler","5551477","E.A.T.S. Snack Shop","null","Hot Dogs","Blue Jeans","")
c8 = Cards("Jamal","5559877","Reel Movies","null","Candy","Tie","")
c9 = Cards("Gary","5553211","Reel Movies","null","Popcorn","Blue Jeans","")
c10 = Cards("Dan","5557777","Reel Movies","null","Candy","Blue Jeans","")
c11 = Cards("Spencer","5556544","Reel Movies","null","Popcorn","Jacket","")
c12 = Cards("Mark","5558522","Woodland Park","Baseball","null","Hat","")
c13 = Cards("Jason","5557411","Woodland Park","Baseball","null","Glasses","")
c14 = Cards("Steve","5559999","Woodland Park","Skateboarding","null","Jacket","")
c15 = Cards("John","5559633","Woodland Park","Skateboarding","null","Anything Yellow","")
c16 = Cards("Paul","5555515","High Tide Beach","Volleyball","null","Anything Yellow","")
c17 = Cards("Tony","5552442","High Tide Beach","Volleyball","null","Hat","")
c18 = Cards("Wayne","5553535","High Tide Beach","Surfing","null","Anything Yellow","")
c19 = Cards("Mike","5552226","High Tide Beach","Surfing","null","Hat","")
c20 = Cards("Scott","5555599","Jim's Gym","Basketball","null","Anything Yellow","")
c21 = Cards("Bob","5554884","Jim's Gym","Basketball","null","Glasses","")
c22 = Cards("Carlos","5556668","Jim's Gym","Tennis","null","Hat","")
c23 = Cards("Matt","5557557","Jim's Gym","Tennis","null","Glasses","")


player1 = Player(1,[],False,"") #sets player1 with no cards in hand
player2 = Player(2,[],False,"") #sets the variable player2

player_list=[player1,player2]
#player_cycle = itertools.cycle(player_list)

##global stuff##
card_list = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20,c21,c22,c23]
# this is the master list of cards in the deck. a way to reference a var list containing all card object names.
# tried to find a less brute force way to do this but so far no luck.

game_deck = copy.copy(card_list)  # this clones from the master list for the "in game" deck
in_hand = []  # initializes player hand as empty
discard_pile = []  # initializes discard pile as empty
#functions

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
        for i in range (len(player_list)):
            player_list[i].cardsinhand.append(game_deck.pop(0))
    print("All Players have drawn 3 cards from the deck.")

def whos_turn():
    if player1.current_turn == True:
        current_player = player1
        return current_player
    if player2.current_turn == True:
        current_player = player2
        return current_player

def print_whos_turn():
    if player1.current_turn == True:
        current_player = player1
        print("It is",current_player.playername,"'s turn (Player 1).")
        return current_player
    if player2.current_turn == True:
        current_player = player2
        print("It is",current_player.playername,"'s turn (Player 2).")
        return current_player

def name_players():
    print("Please give Player 1 a name.")
    name=input()
    player1.playername=name
    print("Please give Player 2 a name.")
    name = input()
    player2.playername = name
    print("The names you have chosen are:")
    print("Player", player1.playernumber, player1.playername)
    print("Player", player2.playernumber, player2.playername)

def starting_player():
    while True:
        print("Choose which player wants to start, 1 or 2?")
        choice = input()
        if choice:
            if choice.isdigit() == True:
                if int(choice) == 1:
                    player1.current_turn = True
                    print("Player 1 will go first.")
                    time.sleep(1)
                    break
                if int(choice) == 2:
                    player2.current_turn = True
                    print("Player 2 will go first.")
                    time.sleep(1)
                    break
                else: print("Not a valid number.")

            if choice.isdigit() == False:
                if choice.lower() == "one":
                    player1.current_turn=True
                    print("Player One will go first.")
                    break
                if choice.lower() == "two":
                    player2.current_turn = True
                    print("Player Two will go first.")
                    break
                else: print("Not a valid word.")
        else: print("Not a valid choice.")

def end_turn():
    for i in range(len(player_list)):   #iterates over all index numbers in player list var
        if player_list[i] == whos_turn():   #if i is the index number of the item matching current player:
            current_player_num = i  #sets var current_player_num to correct index number
    if current_player_num == len(player_list) - 1: #checks if player rotation has reached end of list
        next_player_num = 0 #sets the next player to start at list beginning
    else:
        next_player_num = current_player_num + 1    #not at end of the list, set next player num to advance by 1
    print("Ending", whos_turn().playername, "'s turn.")
    time.sleep(1)
    whos_turn().current_turn = False    #turns off current player turn flag
    print("next player up:",player_list[next_player_num].playername)
    time.sleep(1)
    player_list[next_player_num].current_turn = True    #turns on next player turn flag

def shuffle():  # shuffles the game deck
    random.shuffle(game_deck)
    print("Cards in the game deck have been shuffled. \n")

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

def discard(num_count):
    if len(whos_turn().cardsinhand) == 0:  # check that your hand is not empty
        print("you have no cards to discard.")
        time.sleep(1)
    else:
        if int(len(whos_turn().cardsinhand)) < num_count: #checks that you aren't trying to discard more cards than are in your hand
            print("You cannot discard more cards than you have in hand.")
        else:
            print("You are discarding", num_count, "cards.")
            for i in range(num_count):  # i counts the number of discard_count specified
                discard_pile.append(whos_turn().cardsinhand.pop(i)) #moves in hand card to discard pile

def discard_choice():
    loop = 1
    while loop == 1:
        if len(whos_turn().cardsinhand) == 0:  # check that your hand is not empty
            print("you have no cards to discard.")
            time.sleep(1)
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
                        time.sleep(1)
                        break

                else: #if not 0 cards and if not a in_hand[i].name, incorrect choice
                    print ("Incorrect choice.")

def reshuffle():
    if len(discard_pile) == 0: # check that discard pile is not empty
        print("There's nothing in the discard pile to shuffle back into the deck.")
    else:
        for i in range(len(discard_pile)): #does an i loop based on the number of items in the discard pile
            game_deck.append(discard_pile.pop(0)) #adds the discard pile back into the game deck
        random.shuffle(game_deck)
        print("The discard pile has been shuffled back to the draw pile.\n")

#the following stuff is just to give some text feedback in the test program, not too interesting.

def count_discard():
    if len(discard_pile) == 0:
        print ("There are no cards in the discard pile.\n")
        time.sleep(1)
    else:
        print("number of cards in the discard pile:", len(discard_pile))
        time.sleep(1)

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

def show_hand():
    if len(whos_turn().cardsinhand) == 0:
        print("There are no cards in your hand.\n")
    else:
        print("Cards in", whos_turn().playername, "'s hand are:")
        for i in whos_turn().cardsinhand:
            print (i.name)
            time.sleep(.5)

def count_deck():
    if len(game_deck) == 0:
        print ("There are no cards in the draw deck.\n")
    else:
        print("The number of cards in the draw deck are:", len(game_deck))

def show_deck():
    if len(game_deck) == 0:
        print ("There are no cards in the draw deck.\n")
    else:
        print("The cards in the deck are:")
        for i in game_deck: print(i.name)

def look():
    if len(whos_turn().cardsinhand) == 0:
        print("There are no cards in your hand.\n")
    else:
        print(whos_turn().playername,"looks closely at the cards in their hand.")
        for i in whos_turn().cardsinhand:
            print(str(i.name),"- Phone#:",(i.phonenum))
            time.sleep(.5)
    time.sleep(1)
def count():
    #print("====Status====\nDraw Deck:",len(game_deck),"\nHand:",len(in_hand),"\nDiscard:",len(discard_pile),"\n")
    print(f"====Status====\nDraw Deck: {len(game_deck)}\n{whos_turn().playername}'s Hand: {len(whos_turn().cardsinhand)}\nDiscard: {len(discard_pile)}\n")
    time.sleep(.5)
# now on to the main loop. it simply checks for inputs to run the outlined functions. nothing too crazy

def game_loop():
    valid_choices=["end","look","shuffle","draw","discard","discard choice","reshuffle","count","show","count deck","count hand","count discard","show deck","show hand","show discard","more"]
    print("\nWelcome to Dream Phone Simulator. This is incomplete but getting better!\n")
    name_players()
    starting_player()
    starting_deal()
    while True:
        count()
        print_whos_turn()
        print ("('look') - ('shuffle') - ('draw') - ('discard') - ('end') - ('discard choice') - ('reshuffle') - ('more')")
        choice = input().lower()
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
                print("You can type 'show' or 'count' to show or count your hand, draw pile and discard pile. Using 'show' or 'count' plus 'hand', 'deck' or 'discard' will display or count the individual respective stacks.")

crush = new_game_crush()
game_loop()


# I need to figure out how I want to do loud / quiet stuff with the text parser - might not be possible? focus on single player? / make pico dreamphone? I think i should
# at least program the effect -"this part is quiet", "this part is loud" to practice the logic before i get sound involved. need to take recordings of dreamphone repsonses - maybe move project
# to a website to act as phone (use a cellphone) and use real feelie cards /etc... i dunno hitting a logistical wall