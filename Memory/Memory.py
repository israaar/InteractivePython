# Memory game assignment
import simplegui
import random
import math
pos = []  # pos holds the position where the numbers will be drawn
x = 15
y = 65
increment = 50
memorydeck =[]
polygoncoord = []
WIDTH = 800
CARD_WIDTH = WIDTH / 16
HEIGHT = 100
opencards = []
state = 0
totturns = 0
#populating pos list with position of numbers 

for i in range(16):
    item = (x,y)
    pos.append(item)
    x = x + increment

exposed = [] # used to figure out if the card at "i"th position needs to be shown or not. 

def init():
    global memorydeck , exposed , state, opencards,totturns
    deck1 = range(8)
    deck2 = range(8)
    memorydeck = deck1 + deck2
    random.shuffle(memorydeck)
    print memorydeck
    
    exposed = ['False' for i in range(16)]  # initializing exposed with False as all cards need to be facing up initially. 
    #print pos
    #  coordinates of the first card.
    x1 = 0
    x2 = CARD_WIDTH
    y1 = 0
    y2 = HEIGHT
    #populate coordinates of the polygons to be used as cards
    for i in range(16):
        tempcoord = [(x1,y1),(x2,y1),(x2,y2),(x1,y2)]
        polygoncoord.append(tempcoord)
        x1 += CARD_WIDTH
        x2 += CARD_WIDTH
        
    #print polygoncoord  
    state = 0
    opencards =[]
    totturns = 0    
    label.set_text("Moves = "+str(totturns)) 

def mouseclick(position):
    global exposed,opencards, state,totturns
    cardnum = math.ceil(position[0] / CARD_WIDTH)
    if (exposed[cardnum - 1] == "False"):
        totturns = totturns + 1
        #print opencards
        exposed[cardnum - 1] = "True"
        if(state == 0):
            state = 1
            opencards.append(cardnum-1)
            #print opencards
        elif(state == 1):
            state = 2
            opencards.append(cardnum-1)
            #print opencards
        elif(state ==2):
            #add logic to compare open cards
            #print opencards
            if(memorydeck[opencards[0]] == memorydeck[opencards[1]]):
                opencards =[]
            else:
                exposed[opencards[0]] = "False"
                exposed[opencards[1]] = "False"
            # add logic to expose or not
            # add logic to update state to 1
            state = 1
            # add logic to clean out openedcards
            #print opencards
            #print exposed
            opencards =[]
            opencards.append(cardnum-1)
            #print opencards
        label.set_text("Moves = "+str(totturns))      
    #print state
    #print totturns

def draw(canvas):
    for i in range(len(memorydeck)):
        if exposed[i] == "True":
            
            canvas.draw_polygon(polygoncoord[i], 5, "White","Black")
            canvas.draw_text(str(memorydeck[i]),pos[i],50,"White")

        else:
            canvas.draw_polygon(polygoncoord[i], 5, "White","Green")
            



# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
label = frame.add_label("Moves = 0")
    
# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()
init()

