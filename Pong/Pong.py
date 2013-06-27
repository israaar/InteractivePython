import simplegui
import random
 
# initialize global variables related to the paddles and ball. 
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
 
#spawn ball

global paddle1_vel
global paddle2_vel
global w
global s

# if right is True, then spawn the ball to the right, else spawn the ball to the left

def ball_init(right):
    global ball_pos, ball_vel,w1,s1,w2,s2 # these are vectors stored as lists
 
    w1=5
    w2=5
    s1=5
    s2=5
    ball_pos=[WIDTH/2,HEIGHT/2]
 
    if right==True:
        vel=random.randrange(2, 6)
    else:
        vel=random.randrange(2,6)
        vel=-vel
    ball_vel=[vel,-random.randrange(1, 5)]
 
# event handlers
def init():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel 
    global score1, score2 
    global count1,count2
    count1=0
    count2=0
    paddle1_pos=[HALF_PAD_WIDTH,0]
    paddle2_pos=[WIDTH-HALF_PAD_WIDTH,0]
    paddle1_vel=0
    paddle2_vel=0
    ball_init(random.choice([True, False]))
 
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global radius
    global count1,count2
    radius=BALL_RADIUS
    # update paddle's vertical position, keep paddle on the screen. 
    
    paddle1_pos[1]=paddle1_pos[1]+paddle1_vel
    paddle2_pos[1]=paddle2_pos[1]+paddle2_vel

    if paddle1_pos[1]<=0:
       paddle1_pos[1]=0
 
    if paddle1_pos[1]>=HEIGHT-PAD_HEIGHT:
       paddle1_pos[1]=HEIGHT-PAD_HEIGHT
 
    if paddle2_pos[1]<=0:
       paddle2_pos[1]=0
 
    if paddle2_pos[1]>=HEIGHT-PAD_HEIGHT:
       paddle2_pos[1]=HEIGHT-PAD_HEIGHT
 
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
 
    # draw paddles
    c.draw_line([paddle1_pos[0], paddle1_pos[1]],[paddle1_pos[0],paddle1_pos[1]+ PAD_HEIGHT], PAD_WIDTH, "White")
    c.draw_line([paddle2_pos[0], paddle2_pos[1]],[paddle2_pos[0], paddle2_pos[1]+PAD_HEIGHT], PAD_WIDTH, "White")
 
    # update ball
    ball_pos[0]=ball_pos[0]+ball_vel[0]
    ball_pos[1]=ball_pos[1]+ball_vel[1]
    
    # bounce ball off the paddle
    if ball_pos[0]<=paddle1_pos[0]+radius+HALF_PAD_WIDTH and ball_pos[1]>=paddle1_pos[1] and ball_pos[1]<=paddle1_pos[1]+PAD_HEIGHT:
        ball_pos[0]==paddle1_pos[0]
        ball_vel[0]=ball_vel[0]*-1.1
        ball_vel[1]=ball_vel[1]*1.1
    
    # bounce ball off the paddle2
    if ball_pos[0]>=paddle2_pos[0]-radius-HALF_PAD_WIDTH and ball_pos[1]>=paddle2_pos[1] and ball_pos[1]<=paddle2_pos[1]+PAD_HEIGHT:
        ball_pos[0]==paddle2_pos[0]
        ball_vel[0]=ball_vel[0]*-1.1
        ball_vel[1]=ball_vel[1]*1.1
        
    # in case if vertical component of the ball position is <= radius of ball, reset the position. Ensures ball doesn't go out of the screen. 
    if ball_pos[1]<=radius :
       ball_pos[1]=radius
       ball_vel[1]=ball_vel[1]*-1
        
    elif ball_pos[1]>=HEIGHT-radius:
       ball_pos[1]=HEIGHT-radius
       ball_vel[1]=ball_vel[1]*-1
        
    if ball_pos[0]>=WIDTH-radius:
       #update score variable count1. 
       count1=count1+1
       ball_init(False)
        
    if ball_pos[0]<=radius:
       #update score variable count1. 
       count2=count2+1
       ball_init(True)
        
    # draw ball and scores
    c.draw_circle((ball_pos[0], ball_pos[1]),radius,8, "Green")
    c.draw_text(str(count1), [WIDTH/4,HEIGHT/4], 36, "Red")
    c.draw_text(str(count2), [3*WIDTH/4,HEIGHT/4], 36, "Red")

# key down handler
def keydown(key):
    global paddle1_vel, paddle2_vel,w1,s1,w2,s2
    if key==simplegui.KEY_MAP["down"]:
        s1=s1+1
        paddle1_vel=s1
 
    elif key==simplegui.KEY_MAP["s"]:
        s2=s2+1
        paddle2_vel=s2
 
    elif key==simplegui.KEY_MAP["w"]:
        s2=s2+1
        paddle2_vel=-s2
    elif key==simplegui.KEY_MAP["up"]:
        s1=s1+1
        paddle1_vel=-s1

# key up handler
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["down"]:
        s2=w2
        paddle1_vel=0
 
    elif key==simplegui.KEY_MAP["s"]:
        s1=w1
        paddle2_vel=0
 
    elif key==simplegui.KEY_MAP["w"]:
        s2=w2
        paddle2_vel=0
    elif key==simplegui.KEY_MAP["up"]:
        s1=w1
        paddle1_vel=0
    pass

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", init, 100)
 
# start frame
init()
frame.start()
ball_init(0)
