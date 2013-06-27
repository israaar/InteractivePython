import simplegui

timecounter = 0  # global variable to hold information about the time value. 
total_stops = 0  # total stop button presses
total_suc_stops = 0 # total stop button presses which happened at the whole number count. 

#method which increments the timecounter  

def increment_time():
    global timecounter
    timecounter = timecounter + 1

# format method for formatting the timecounter into string value to be shown on the canvas

def format(t):
    '''
    Next, write a helper function format(t) that returns a string of the form A:BC.D 
    where A, B, C and D are digits in the range 0-9. Test this function independent of your project. 
    Note that the string returned by your helper function format should always correctly include leading zeros.
    For example
    format(0) == 0:00.0
    format(11) = 0:01.1
    format(321) = 0:32.1
    format(613) = 1:01.3
    '''
    d = t % 10 
    
    bc = int (t / 10)
    
    a = 0
    
    if (bc >=60):
       a = int (bc / 60)
       bc = bc % 60
    
    if(bc <10):
        bc = str(0)+str(bc)
       
    
    return str(a)+":"+str(bc)+"."+str(d)  

# draw handler

def draw_handler(canvas):
    canvas.draw_text(format(timecounter), (75, 150), 70, "Red")
    string_text = str(total_suc_stops)+"/"+str(total_stops)
    canvas.draw_text(string_text,(255,20),18,"White") 
    

frame = simplegui.create_frame("Stop Watch", 300, 300)    

timer = simplegui.create_timer(100, increment_time)

# start button handler. 

def start_handler():
    timer.start()

# stop button handler. 
def stop_handler():
    global total_stops
    global total_suc_stops
    if (timer.is_running()):
        timer.stop()
        total_stops+=1
        if((timecounter % 10) == 0):
            total_suc_stops+=1
    
# reset button handler. default all global variables to 0. 
def reset_handler():
    global timecounter
    global total_stops
    global total_suc_stops
    timecounter = 0
    total_stops = 0
    total_suc_stops = 0
    if (timer.is_running()):
        timer.stop()
# add three buttons    
start_button = frame.add_button("Start", start_handler, 50)
stop_button = frame.add_button("Stop", stop_handler, 50)
reset_button = frame.add_button("Reset", reset_handler, 50)

frame.set_draw_handler(draw_handler)

frame.start()

