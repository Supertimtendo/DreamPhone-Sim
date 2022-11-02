#dreamphone simulator alpha 1.7

import webbrowser #required for webbrowser.open('dreamphone.jpg')
import random #required for "random.shuffle()"
import os #required for "os.linesep"
import time #required for time delay "time.sleep(.5)" in dial function
# import winsound

boy_names = ['dave', 'george','dale','alan','james','phil','bruce','tyler','jamal','gary','dan','spencer','mark','jason','steve',
            'john','paul','tony','wayne','mike','scott','bob','carlos','matt']

boy_nums = ['5551111', '5551233','5554566','5557899','5552588','5553333','5553699','5551477','5559877','5553211','5557777','5556544','5558522','5557411','5559999',
            '5559633','5555515','5552442','5553535','5552226','5555599','5554884','5556668','5557557']

all_clues = ['crosstown_mall','snack_shop','reel_movies','woodland_park','high_tide_beach','jims_gym','baseball','skateboarding','volleyball','surfing','basketball',
             'tennis','ice_cream','cookies','hot_dogs','pizza','candy','popcorn','hat','tie','blue_jeans','jacket','glasses','anything_yellow']

neg_grammar_table = ["isn't at", "doesn't like", "doesn't eat","doesn't wear"]
pos_grammar_table = ["is at", "likes", "eats","wears"]

clue_flag = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

                                 #  |0-23 count clues.  
crosstown_mall = [0,1,2,3]       #0 |The list for each contains a reference number
snack_shop = [4,5,6,7]           #1 |for the boys that the variable pertains to.
reel_movies = [8,9,10,11]        #2
woodland_park = [12,13,14,15]    #3
high_tide_beach = [16,17,18,19]  #4
jims_gym = [20,21,22,23]         #5
baseball = [12,13]               #6    
skateboarding = [14,15]          #7
volleyball = [16,17]             #8
surfing = [18,19]                #9
basketball = [20,21]             #10
tennis = [22,23]                 #11
ice_cream = [1,2]                #12
cookies = [0,3]                  #13
hot_dogs = [4,7]                 #14
pizza = [5,6]                    #15
candy = [8,10]                   #16
popcorn = [9,11]                 #17
hat = [12,17,19,22]              #18
tie = [1,3,6,8]                  #19
blue_jeans = [0,7,9,10]          #20
jacket = [2,4,11,14]             #21
glasses = [5,13,21,23]           #22
anything_yellow = [15,16,18,20]  #23

def choose_boy():
    shuffleboy = boy_names[:]
    random.shuffle(shuffleboy)
    your_crush = shuffleboy[0]
    crush_num = boy_names.index(shuffleboy[0])
    return (crush_num, shuffleboy, your_crush)

def assign_clues(crush_num):
    #print ("validating crush num:",crush_num)
    if crush_num in crosstown_mall: clue_flag[0] = 1
    else: clue_flag[0] = 0
    if crush_num in snack_shop: clue_flag[1] = 1
    else: clue_flag[1] = 0
    if crush_num in reel_movies: clue_flag[2] = 1
    else: clue_flag[2] = 0
    if crush_num in woodland_park: clue_flag[3] = 1
    else: clue_flag[3] = 0
    if crush_num in high_tide_beach: clue_flag[4] = 1
    else: clue_flag[4] = 0
    if crush_num in jims_gym: clue_flag[5] = 1
    else: clue_flag[5] = 0
    if crush_num in baseball: clue_flag[6] = 1
    else: clue_flag[6] = 0
    if crush_num in skateboarding: clue_flag[7] = 1
    else: clue_flag[7] = 0
    if crush_num in volleyball: clue_flag[8] = 1
    else: clue_flag[8] = 0
    if crush_num in surfing: clue_flag[9] = 1
    else: clue_flag[9] = 0
    if crush_num in basketball: clue_flag[10] = 1
    else: clue_flag[10] = 0
    if crush_num in tennis: clue_flag[11] = 1
    else: clue_flag[11] = 0
    if crush_num in ice_cream: clue_flag[12] = 1
    else: clue_flag[12] = 0
    if crush_num in cookies: clue_flag[13] = 1
    else: clue_flag[13] = 0
    if crush_num in hot_dogs: clue_flag[14] = 1
    else: clue_flag[14] = 0
    if crush_num in pizza: clue_flag[15] = 1
    else: clue_flag[15] = 0
    if crush_num in popcorn: clue_flag[16] = 1
    else: clue_flag[16] = 0
    if crush_num in candy: clue_flag[17] = 1
    else: clue_flag[17] = 0
    if crush_num in hat: clue_flag[18] = 1
    else: clue_flag[18] = 0
    if crush_num in tie: clue_flag[19] = 1
    else: clue_flag[19] = 0
    if crush_num in blue_jeans: clue_flag[20] = 1
    else: clue_flag[20] = 0
    if crush_num in jacket: clue_flag[21] = 1
    else: clue_flag[21] = 0
    if crush_num in glasses: clue_flag[22] = 1
    else: clue_flag[22] = 0
    if crush_num in anything_yellow: clue_flag[23] = 1
    else: clue_flag[23] = 0

def print_boylist():
    print(os.linesep)
    print("Written inside your trapper keeper is a serial-killer level of details of every potential mate in your school. You turn to the phone numbers page.")
    print(os.linesep)
    for x in range (0,24):
        print(boy_names[x],'-',boy_nums[x])
    print(os.linesep)
    
def phonenum_to_boy():
    print("Please enter the phone number you want to dial. Example: 5551111.")
    print ("You can also type 'back' to hang up and go to the previous menu.")

    phonenumloop = 1
    validated_number = 0
    back = 0
    correct_num = 0

    while phonenumloop == 1:
        phonenum = input()
        if phonenum == 'back':
            phonenumloop = 0
            back = 1      #sets back flag to 1 for num_dial to know if you have a valid number or not
        for x in range (0,24):
            if phonenum == (boy_nums[x]):
                validated_number = x
                phonenumloop = 0
                correct_num = 1
                print ("You hastily punch the digits into your phone...")
                break
        if phonenum != 'back' and correct_num == 0: print("Please enter a valid number.")
    return [validated_number, back]
     
def clues_print(crush_num,your_crush):
    print ('Your Crush is',your_crush)
    print ("Crush Number on Boys List:", crush_num,os.linesep)  

    for x in range (0,24):
        if clue_flag[x] == 1:
            if x in range(0,6): pos_gram_num = 0
            if x in range(6,12): pos_gram_num = 1
            if x in range(12,18): pos_gram_num = 2
            if x in range(18,24): pos_gram_num = 3
            print ("your crush",pos_grammar_table[pos_gram_num],all_clues[x])
    print(os.linesep)

def num_dial(shuffleboy): #this one is with boys phone numbers as inputs
    dialed_boy = 0
    dialed_boy_num = 0
    leave_dial = 0
    madeacall = 0
    validated_number = [0,0]
    
    print ("Type 'dial' to pick up the phone to enter a number.")
    print ("You can also type 'guess' to make make a guess at who your crush is.")
    print ("You can also type 'phonebook' to see the names and numbers of the boys.")
    
    dialed = input()
    if dialed == 'dial':
        validated_number = phonenum_to_boy() #returns validated_number as validated_number[0], and back as validated_number[1]
        madeacall = 1
        
    if validated_number[1] == 1:
        print("You hang up the phone and think about your life.")

    if madeacall == 1 and validated_number[1] == 0:
        dialed = boy_names[validated_number[0]]
        for x in range (0,3):
            print ("*ring*")
            time.sleep(.5)

        for x in range(0, 24):
            if dialed == shuffleboy[x]:
                dialed_boy = shuffleboy[x]
                dialed_boy_num = x
                print ("You hear",dialed_boy,"on the line.")
                leave_dial= "reveal_clue"
                break

        #print ("validating dialed_boy_num:",dialed_boy_num)

    if dialed != 'guess' and dialed != dialed_boy and dialed != 'phonebook': print ("Wrong number!",os.linesep)
    if dialed == 'guess': leave_dial = "solve"
    if dialed == 'phonebook': print_boylist()


    return dialed_boy,dialed_boy_num,leave_dial


def reveal_clue(dialed_boy, dialed_boy_num):
    print (dialed_boy, "says: so you want to know about your crush?")

    time.sleep(2)

    if dialed_boy_num in range(0,6): neg_gram_num = 0
    if dialed_boy_num in range(6,12): neg_gram_num = 1
    if dialed_boy_num in range(12,18): neg_gram_num = 2
    if dialed_boy_num in range(18,24): neg_gram_num = 3
    
    if clue_flag[dialed_boy_num] == 0:
        print ("your crush",neg_grammar_table[neg_gram_num],all_clues[dialed_boy_num],os.linesep)
        time.sleep(1)

    if clue_flag[dialed_boy_num] != 0:
        print ("Ha Ha! I'm not Telling!")

def solve(your_crush):
    valid_answer = 0

    print ("Okay, who do you think wants to make sweet love to you? You can type 'back' to chicken out.")
    
    while valid_answer == 0:
        dialed = input()

        if dialed == 'back':
            print (os.linesep)
            print ("You like to play hard to get, eh? Keep playing to gather more clues.",os.linesep)
            valid_answer = 1

        if dialed != your_crush and dialed not in boy_names[:] and dialed != 'back':
            print ("You didn't enter a valid choice. Please try again.")

        if dialed in boy_names[:]: valid_answer = 1

    if dialed in boy_names[:] and dialed != your_crush:
        print ("Sorry, that is not who has a crush on you. Keep playing to gather more clues.",os.linesep)

    if dialed == your_crush:
        print ("You did it! Now get to fuckin'!")
        print ("type 'reset' to play a new game")
        print ("Elsewise, type 'exit' to leave the program")
        x = input()
        if x == "reset": reset_or_exit = "reset"
        if x == "exit": reset_or_exit = "exit"
        if x != "reset" and  x != "exit": print ("type 'reset' to play a new game, or 'exit' to leave the program.")
        return reset_or_exit

def dreamphone_simulator():
    program = 1
    while program == 1:
        # winsound.PlaySound("intro.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)
        crush_num, shuffleboy, your_crush = choose_boy()
        assign_clues(crush_num)
        #clues_print(crush_num,your_crush)   #this is cheating
        gameloop = 1
        while gameloop == 1:
            reset_or_exit = 0
            dialed_boy, dialed_boy_num, leave_dial = num_dial(shuffleboy)
            if leave_dial == "solve": reset_or_exit = solve(your_crush)
            if leave_dial == "reveal_clue": reveal_clue(dialed_boy, dialed_boy_num)
            if reset_or_exit == "exit": program = 0
            if reset_or_exit == "reset": gameloop = 0
            
webbrowser.open('dreamphone.jpg')
dreamphone_simulator()


# old code scraps
#def dial(shuffleboy): #this version relies on names... trying to convert to numbers as inputs
#    dialed_boy = 0
#    dialed_boy_num = 0
#    leave_dial = 0
#    print ("Who do you dial?")
#    print ("You can also type 'guess' to make make a guess at who your crush is.")
#    dialed = input()
#
#    for x in range (0,3):
#        print ("*ring*")
#        time.sleep(.5)
#
#    for x in range(0, 24):
#        if dialed == shuffleboy[x]:
#            dialed_boy = shuffleboy[x]
#            dialed_boy_num = x
#            print ("you called",dialed_boy)
#            leave_dial= "reveal_clue"
#            #print ("validating dialed_boy_num:",dialed_boy_num)
#        
#    if dialed != 'guess' and dialed != dialed_boy: print ("Wrong number!",os.linesep)
#    if dialed == 'guess': leave_dial = "solve"
#        
#    return dialed_boy,dialed_boy_num,leave_dial



        
