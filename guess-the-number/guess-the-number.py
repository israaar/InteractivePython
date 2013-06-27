# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simplegui
import math

# initialize global variables used in your code
'''
global variable which stores the number that needs to be guessed
'''
number_to_guess = 0

'''
global variable which stores teh total number of allowed attempts
'''

total_allowed_attempts = 0

'''
global variable to remember whether player is playing 100 game or 1000 game. 
Same range game will start if maximum number of attempts are met
'''
game100 = 0

# define event handlers for control panel

# method with logic of range (0,100]
    
def range100():
    # button that changes range to range [0,100) and restarts
    global number_to_guess
    global total_allowed_attempts
    global game100
    number_to_guess = random.randrange(0,100)
    print "################################"
    print "Guess a number between 0 and 100.Enter your choice in text box."
    total_allowed_attempts = math.ceil((math.log(100)) / (math.log(2)))
    print " Total allowed attempts %s" %total_allowed_attempts
    print "################################" 
    game100 = 1
    
    
# method with logic of range (0,1000]
def range1000():
    # button that changes range to range [0,1000) and restarts
    global number_to_guess
    global total_allowed_attempts
    global game100
    number_to_guess = random.randrange(0,1000)
    print "################################"
    print "Guess a number between 0 and 1000.Enter your choice in text box"
    total_allowed_attempts = math.ceil((math.log(1000)) / (math.log(2)))
    print " Total allowed attempts %s" %total_allowed_attempts
    print "################################" 
    game100 = 2

# handler which processes the input string ("the guess")

def get_input(guess):
    # main game logic goes here	
    global total_allowed_attempts
    if (int(guess) > number_to_guess):
        print "guess lower"
        total_allowed_attempts = total_allowed_attempts - 1
        print " you have only %s attempts left" %total_allowed_attempts
        
    elif (int(guess) < number_to_guess):
        print "guess higher"
        total_allowed_attempts = total_allowed_attempts - 1
        print " you have only %s attempts left" %total_allowed_attempts
    else:
        print "######################################################"
        print "You WON!!!"
        print "Game RESTARTING"
        print "######################################################"
        if(game100 == 1):
            range100()
        elif(game100 == 2):
            range1000()         
    if(total_allowed_attempts == 0):
        
        print "######################################################"
        print "Sorry, you have run out the maximum number of attempts"
        print "You LOSE!!!"
        print "Game RESTARTING !!!"
        print "######################################################"
        if(game100 == 1):
            range100()
        elif(game100 == 2):
            range1000()

    
# create frame
frame = simplegui.create_frame("Guess The Number", 350, 350)
# add buttons
button100 = frame.add_button("Start game 0-100", range100,200)
button1000 = frame.add_button("Start game 0-1000", range1000,200)
# add input text box
inp = frame.add_input("Guess the Number", get_input, 100)

# start frame
frame.start()
# call range100 to start the game in (0,100] mode. 
range100()

# always remember to check your completed program against the grading rubric
