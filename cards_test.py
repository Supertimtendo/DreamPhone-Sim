import random
import copy

class Cards:  #class Cards constructor
    def __init__(self, name, detail):
        self.name = name    #Class Cards gets a "name" attribute
        self.detail = detail #Class Cards gets a "detail" attribute

#building Cards objects:
c0 = Cards("Bob","555-5551")
c1 = Cards("Charlie","555-5552")
c2 = Cards("Tom","555-5553")
c3 = Cards("Kyle","555-5554")
c4 = Cards("Mike","555-5557")

##global stuff##

card_list = [c0,c1,c2,c3,c4]  # this is the master list of cards in the deck. Can be user assignable.


game_deck = copy.copy(card_list)  # this clones from the master list for the "in game" deck
in_hand = []  # initializes player hand as empty
discard_pile = []  # initializes discard pile as empty

#functions

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
            print("You drew", num_count, "cards.")
            for i in range(num_count):  # I counts the number of draw_count specified
                in_hand.append(game_deck.pop(0))  # moves top card from game_deck list and adds it to in_hand
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
    if len(in_hand) == 0:  # check that your hand is not empty
        print("you have no cards to discard.\n")
    else:
        if int(len(in_hand)) < num_count: #checks that you aren't trying to discard more cards than are in your hand
            print("You cannot discard more cards than you have in hand.")
        else:
            print("You are discarding", num_count, "cards.")
            for i in range(num_count):  # i counts the number of discard_count specified
                discard_pile.append(in_hand.pop(0)) #moves in hand card to discard pile
        count_discard()

def discard_choice():
    loop = 1
    while loop == 1:
        if len(in_hand) == 0:  # check that your hand is not empty
            print("you have no cards to discard.")
            break
        else:
            show_hand()
            print("Please choose the card you wish to discard, or type 'back' to leave.")
            card_choice = input().lower() #which card do you want to discard?
            if card_choice == 'back': #gives a way to back out of the discard choice loop
                print("Exiting discard choice...")
                break #leaves discard choice loop
            else:
                for i in range(len(in_hand)):  #runs through the list count of in_hand
                    if card_choice == (in_hand[i].name).lower(): #checks if choice is in your hand
                        print(in_hand[i].name,"from your hand has been discarded.")
                        discard_pile.append(in_hand.pop(i)) #adds card to discard pile based on in_hand index num
                        loop = 0
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
    else:
        print("number of cards in the discard pile:", len(discard_pile))

def show_discard():
    if len(discard_pile) == 0:
        print ("There are no cards in the discard pile.\n")
    else:
        print("The cards in the discard pile are:")
        for i in discard_pile: print(i.name)

def count_hand():
    if len(in_hand) == 0:
        print ("There are no cards in your hand.\n")
    else:
        print("number of cards in your hand are:", len(in_hand))

def show_hand():
    if len(in_hand) == 0:
        print("There are no cards in your hand.\n")
    else:
        print("cards in your current hand are:")
        for i in in_hand: print(i.name)

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
    if len(in_hand) == 0:
        print("There are no cards in your hand.\n")
    else:
        print("You look closely at the cards in your hand.")
        for i in in_hand:
            print(str(i.name),"- Phone#:",(i.detail))

def count():
    #print("====Status====\nDraw Deck:",len(game_deck),"\nHand:",len(in_hand),"\nDiscard:",len(discard_pile),"\n")
    print(f"====Status====\nDraw Deck: {len(game_deck)}\nHand: {len(in_hand)}\nDiscard: {len(discard_pile)}\n")

# now on to the main loop. it simply checks for inputs to run the outlined functions. nothing too crazy

def game_loop():
    valid_choices=["look","shuffle","draw","discard","discard choice","reshuffle","count","show","count deck","count hand","count discard","show deck","show hand","show discard","more"]
    print("\nWelcome to deck game. This is a test routine for cards moving around in Python lists.\n")
    while True:
        count()
        print ("Type a command to play. You can shuffle the deck ('shuffle'), draw a card ('draw'), and discard ('discard') from your hand.\nType 'look' to view the cards in your hand. You can choose a specific card to discard with ('discard choice'). The command ('reshuffle') will add the discard pile back into the draw deck.\nType 'more' for other commands.")
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

            if choice == 'more':
                print("You can type 'show' or 'count' to show or count your hand, draw pile and discard pile. Using 'show' or 'count' plus 'hand', 'deck' or 'discard' will display or count the individual respective stacks.")

game_loop()
