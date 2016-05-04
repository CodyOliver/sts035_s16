from graphics import *
from Tkinter import *
import threading
import time
import smbus
import sys
import serial
import struct
import random
import RPi.GPIO as GPIO

pin1 = 10
pin2 = 9
pin3 = 04
pin4 = 17
pin5 = 27
'''
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin1, GPIO.OUT) # set a port/pin as an output
GPIO.setup(pin2, GPIO.OUT)    
GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin4, GPIO.OUT)
GPIO.setup(pin5, GPIO.OUT)
'''

def resetDisplay():
    GPIO.output(pin1, 0)
    GPIO.output(pin2, 0)
    GPIO.output(pin3, 0)
    GPIO.output(pin4, 0)
    GPIO.output(pin5, 0)
    GPIO.cleanup()

    
resetDisplay()
#GPIO.cleanup()

ser = serial.Serial('/dev/ttyACM0',9600)
    
bus = smbus.SMBus(1)

# This is the address we setup in the STM32 Program
address1 = 0x01
address2 = 0x02
address3 = 0x03
address4 = 0x04
address5 = 0x05

led_address = 0x08

# different movement types
linear = 30

balls_list =[]
radius = 10
num_balls = 50
done = True

global selectedIndex
selectedIndex = 0

def packLED(list_of_colors):

    rgb = list_of_colors

    string = ''

    for i in range(len(rgb)):
        string += str(i)
        for value in rgb[i]:
            string = string + ':' + str(value)
        string += ','
    print string
    return string

def sendToLED(value):


    #led_commands = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
    #led_commands = [value]
    led_commands = value

    string = ''

    for i in led_commands:
        string +=struct.pack('!B',i)
        
    ser.write(string)
    ser.write("hello")
    print string
    return 1

def sendToMotorsCmd(values):
    print values

    if len(values)==10:
        send(1,linear,values)

    elif len(values)==50:

        ball_commands1 = values[0:10]
        ball_commands2 = values[10:20]
        ball_commands3 = values[20:30]
        ball_commands4 = values[30:40]
        ball_commands5 = values[40:50]

        send(1,linear,ball_commands1)
        send(2,linear,ball_commands2)
        send(3,linear,ball_commands3)
        send(4,linear,ball_commands4)
        send(5,linear,ball_commands5)

    
    else:
        print "incorrect command size"

    return 1

def send(i,cmd,positions):
    address = 0x00
    if i == 1:
        address = address1
    elif i == 2:
        address = address2
    elif i == 3:
        address = address3
    elif i == 4:
        address = address4
    elif i == 5:
        address = address5
    try:
        bus.write_i2c_block_data(address, cmd, positions) 
    except IOError as e:
        print "ball_commands for "+str(i)+": "+e


def reset():
    values = 50*[0]
    sendToMotorsCmd(values)

def showBalls(num,rad):

    ball_list = []

    #equally space out the balls
    for i in range(0,num_balls):
        initial_x_pos = (i*2*rad)+3*(i+1)
        initial_y_pos = 10
        ball_list.append((initial_x_pos,initial_y_pos))   

    for i in range(0,len(ball_list)):
        ball = ball_list[i]
        ball_list[i] = (canvas.create_oval(ball[0],ball[1],ball[0]+2*rad,ball[1]+2*rad),ball[0],ball[1])

    #setup the first selected ball with red outline
    canvas.itemconfigure(ball_list[selectedIndex][0],outline='red')        

    return ball_list

def moveSelectedBall(num):
    ball = balls_list[selectedIndex]
    canvas.move(ball[0],0,num)
    balls_list[selectedIndex] = (ball[0],ball[1],ball[2]+num)

def changeSelection(current,i):
    #color the previous ball back to black
    canvas.itemconfigure(balls_list[current][0],outline='black')
    #set new index
    newIndex = current+i
    if(newIndex<0):
        newIndex = num_balls-1
    elif(newIndex>=num_balls):
        newIndex = 0

    canvas.itemconfigure(balls_list[newIndex][0],outline='red')
    return newIndex


    
def displayState(i):
    resetDisplay()

    if(i==1):
        GPIO.output(pin2, 1)
    elif(i==2):
        GPIO.output(pin3, 1)
    elif(i==3):
        GPIO.output(pin2, 1)
        GPIO.output(pin3, 1)
    elif(i==4):
        GPIO.output(pin4, 1)
    elif(i==5):
        GPIO.output(pin2, 1)
        GPIO.output(pin4, 1)
    elif(i==6):
        GPIO.output(pin3, 1)
        GPIO.output(pin4, 1)
    elif(i==7):
        GPIO.output(pin2, 1)
        GPIO.output(pin3, 1)
        GPIO.output(pin4, 1)
    '''
    add more states...
    '''
        
def onKeyPress(event):
    global selectedIndex
    character = event.keysym
    print character

    if character =="Escape":
        sys.exit()

    if character =="k":
        sendToLED([1])

    if character == "l":
        sendToLED([0])

    if character == "m":
        ser.write(1234)


    if character == "h":
        #sendToLED([100,20,200])
        #ser.write("0:1:45:556,1:5:67:34,2:677:67:45,3:1:45:556,4:5:67:34,5:677:67:45")
        #ser.write('0:255:192:203,1:255:192:203,2:255:192:203,3:255:192:203,4:255:192:203,5:255:192:203,6:255:192:203,7:255:192:203,8:255:192:203,9:255:192:203,10:255:192:203,11:255:192:203,12:255:192:203,13:255:192:203,14:255:192:203,15:255:192:203,16:255:192:203,17:255:192:203,18:255:192:203,19:255:192:203,20:255:192:203,21:255:192:203,22:255:192:203,23:255:192:203,24:255:192:203,25:255:192:203,26:255:192:203,27:255:192:203,28:255:192:203,29:255:192:203,30:255:192:203,31:255:192:203,32:255:192:203,33:255:192:203,34:255:192:203,35:255:192:203,36:255:192:203,37:255:192:203,38:255:192:203,39:255:192:203,40:255:192:203,41:255:192:203,42:255:192:203,43:255:192:203,44:255:192:203,45:255:192:203,46:255:192:203,47:255:192:203,48:255:192:203,49:255:192:203,')
        #ser.write('0:255:192:203,1:255:192:203,2:255:192:203,3:255:192:203,4:255:192:203,5:255:192:203,6:255:192:203,7:255:192:203,8:255:192:203')
        ser.write("0,102:153:255,255:0:102,1000,400")
    if character == '0':
        #graph0()
        #resetDisplay()
        sendToMotorsCmd([0,0,0,0,0,0,0,0,0,0])
        
    if character == '1':
        #graph1()
        #displayState(1)
        sendToMotorsCmd([40,10,20,250,250,250,250,70,80,250])

    if character == '2':
        graph2()
        displayState(2)

    if character == '3':
        displayState(3)

    if character == '4':
        displayState(4)

    if character == '5':
        displayState(5)

    if character == '6':
        displayState(6)

    if character == 'p':
        student_pop_graph()

    if character == 'f':
        student_faculty_ratio()

    if character == "w":
        women_at_mit()

    if character == 'm':
        mit_buildings()

    if character == 's':
        mit_sports()
        ser.write("0,163:31:52,112:138:154,3300,3300")

    if character == '6':
        reset()

    if character == 'Down':
        moveSelectedBall(10)

    if character == 'Up':
        moveSelectedBall(-10)

    if character == 'Left':
        selectedIndex = changeSelection(selectedIndex,-1)

    if character == 'Right':
        selectedIndex = changeSelection(selectedIndex, 1)

    if character == 'r':
        color(selectedIndex,'red')

    if character == 'b':
        color(selectedIndex,'blue')

    if character == 'g':
        color(selectedIndex,'green')

    if character == 'c':
        color(selectedIndex,(random.randint(0,255),random.randint(0,255),random.randint(0,255)))

def colorAll(color):
    '''Color all balls a specific color'''
    for ball in balls_list:
            canvas.itemconfigure(ball[0],fill=color)

def color(ball_id_number, color):
    '''Set the color of a specific ball to the desired RGB value'''
    if type(color) == tuple:
        tk_rgb = "#%02x%02x%02x" % color
        ball = balls_list[ball_id_number]
        canvas.itemconfigure(ball[0],fill=tk_rgb)
    elif type(color) == str:
        ball = balls_list[ball_id_number]
        canvas.itemconfigure(ball[0],fill=color)

def graph0():
    # graph some data plot 
    thread1 = ballThread(1, "Graph-0",'red', .1,[10,20,30,40,50,60,70,60,50,40,30,20,10,20,30,40,50,60,70,60,50,40])
    thread1.start()

def graph1():
    # draw the mit dome - kinda
    thread1 = ballThread(1, "Graph-1", 'white',.1,[160,160,160,100,100,100,80,80,60,50,44,44,50,60,80,80,100,100,100,160,160,160])
    thread1.start()
    
def graph2():
    thread2 = ballThread(1,"Import-Graph",'green',.1,[300, 293, 286, 279, 272, 264, 256, 248, 240, 232, 224, 216, 208, 200, 193, 186, 179, 172, 164, 156, 148, 140, 132, 124, 116, 108, 100, 93, 86, 79, 72, 64, 56, 48, 40, 32, 24, 16, 8, 0])
    thread2.start()

def student_pop_graph():
    data = [12,32,60,50,44,39,46,53,40,35,46,52,52,28,0,122,123,110,113,124,142,148,151,164,178,189,198,192,196,208,219,229,243,246,251,250,245,247,254,256,257,258,264,270,268,267,270,282,298,300]
    
    for i in range(len(data)):
        data[i] = 300-data[i]

    r = [random.randint(0,255) for i in range(50)]
    g = [random.randint(0,255) for i in range(50)]
    b = [random.randint(0,255) for i in range(50)]

    rgb = [(r[i],g[i],b[i]) for i in range(len(r))]

    thread3 = ballThread(1,"Student-population-graph",rgb,.1,data)
    thread3.start()

def student_faculty_ratio():
    ball_positions = [258.30000000000001, 262.80000000000001, 258.89999999999998, 272.39999999999998, 264.60000000000002, 233.69999999999999, 173.69999999999999, 93.600000000000023, 47.700000000000017, 123.30000000000001, 144.89999999999998, 147.89999999999998, 231.30000000000001, 244.80000000000001, 250.80000000000001, 252.90000000000001, 255.30000000000001, 255.0, 244.19999999999999, 254.69999999999999, 265.19999999999999, 267.30000000000001, 273.60000000000002, 273.30000000000001, 274.80000000000001, 276.60000000000002, 289.5, 272.10000000000002, 279.30000000000001, 279.60000000000002, 281.39999999999998, 284.69999999999999, 285.89999999999998, 287.39999999999998, 286.80000000000001, 285.89999999999998, 285.30000000000001, 285.60000000000002, 286.19999999999999, 286.19999999999999, 286.5, 286.19999999999999, 285.89999999999998, 285.30000000000001, 286.19999999999999, 287.10000000000002, 287.69999999999999, 287.69999999999999, 287.10000000000002, 286.80000000000001] 
    ball_color = [(0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (255, 0, 0), (255, 0, 0), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255)]

    for i in range(len(ball_positions)):
        ball_positions[i] = int(ball_positions[i])

    thread3 = ballThread(1,"Student Faculty Ratio",ball_color,.1,ball_positions)
    thread3.start()

def mit_buildings():
    ball_positions = [298, 298, 298, 298, 298, 298, 298, 298, 296, 296, 292, 292, 282, 282, 282, 282, 274, 272, 270, 268, 262, 260, 258, 256, 246, 246, 246, 238, 228, 222, 214, 210, 174, 156, 144, 136, 128, 116, 104, 100, 100, 96, 92, 92, 90, 78, 70, 68, 60, 58]
    ball_color = [(0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0)]

    for i in range(len(ball_positions)):
        ball_positions[i] = int(ball_positions[i])

    thread3 = ballThread(1,"MIT Buildings",ball_color,.1,ball_positions)
    thread3.start()

def mit_sports():
    ball_positions = [7, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101, 103, 105, 107, 109, 111, 113, 115, 117, 119, 121] [245, 245, 240, 235, 230, 230, 225, 220, 220, 220, 215, 205, 205, 205, 205, 205, 200, 200, 195, 195, 190, 190, 190, 190, 190, 190, 185, 180, 180, 150, 130, 120, 115, 110, 105, 100, 95, 95, 90, 90, 90, 90, 85, 85, 85, 85, 115, 140, 140, 140] 
    ball_color = [(112, 138, 144), (112, 138, 144), (112, 138, 144), (112, 138, 144), (112, 138, 144), (112, 138, 144), (112, 138, 144), (112, 138, 144), (112, 138, 144), (112, 138, 144), (112, 138, 144), (112, 138, 144), (112, 138, 144), (112, 138, 144), (112, 138, 144), (112, 138, 144), (112, 138, 144), (112, 138, 144), (112, 138, 144), (112, 138, 144), (112, 138, 144), (112, 138, 144), (112, 138, 144), (112, 138, 144), (112, 138, 144), (112, 138, 144), (112, 138, 144), (112, 138, 144), (163, 31, 52), (163, 31, 52), (163, 31, 52), (163, 31, 52), (163, 31, 52), (163, 31, 52), (163, 31, 52), (163, 31, 52), (163, 31, 52), (163, 31, 52), (163, 31, 52), (163, 31, 52), (163, 31, 52), (163, 31, 52), (163, 31, 52), (163, 31, 52), (163, 31, 52), (163, 31, 52), (163, 31, 52), (163, 31, 52), (163, 31, 52), (163, 31, 52)]

    for i in range(len(ball_positions)):
        ball_positions[i] = int(ball_positions[i])



    thread3 = ballThread(1,"MIT Sports",ball_color,.1,ball_positions)
    thread3.start()


def women_at_mit():
    
    print canvas.itemconfigure(1)['fill'][4]
    print balls_list[0][0]
    print canvas.itemconfigure(balls_list[0][0],fill='blue')

    
    data = [294, 288, 294, 294, 294, 294, 288, 294, 294, 294, 288, 288, 288,
       288, 276, 294, 294, 294, 288, 288, 288, 288, 288, 282, 276, 270,
       264, 252, 234, 210, 204, 198, 186, 162, 144, 126, 102, 102, 102,
        90,  66,  54,  54,  54,  42,  36,  30,  30,  30,  24]

    rgb = [(255,192,203)]*len(data)

    for i in range(len(data)):
        data[i] = int(data[i])
        

    thread3 = ballThread(1,"Women at MIT",rgb,.1,data)
    thread3.start()
    


exitFlag = 0
animDelay = 0.001
'''
while True:
    sendToMotorsCmd([0,10,20,250,250,250,250,70,80,250])
    time.sleep(1)
'''
class ballThread (threading.Thread):
    def __init__(self, threadID, name, ball_color,index,goal_list):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.index = index
        self.goals = goal_list
        if type(ball_color) == list:
            self.color = ball_color
        else:
            self.color = [ball_color]*len(balls_list)
    def run(self):

        #time.sleep(0) #initial delay for debugging
        print "Starting " + self.name
        done = False

        threadLock.acquire()

        #colorAll(self.color)


        for i in range(0,len(balls_list)):
            if i >= len(self.goals):
                canvas.itemconfigure(balls_list[i][0],fill='')

        self.goals = self.goals + [0]*(len(balls_list)-len(self.goals))
        moved = [1]*len(self.goals)


        sendToMotorsCmd(self.goals)

        #packed = packLED(self.color)
        #ser.write(packed)
        #print type(packed)
        #print packed

        while not done:
            #clear current canvas for next frame            
            #canvas.delete('all')
            for i in range(0,len(self.goals)):
                ball = balls_list[i]

                #print ball
                #print self.goals[i]

                ball_id = ball[0] #ID of the ball
                ball_x = ball[1] #x-position of the ball
                ball_y = ball[2] #y-position of the ball
                
                if ball_y > self.goals[i]:
                    canvas.move(ball_id,0,-1)
                    balls_list[i] = (ball_id,ball_x,ball_y-1)
                    color(i,self.color[i])
                    moved[i] = 1
                elif ball_y < self.goals[i]:
                    canvas.move(ball_id,0,1)
                    balls_list[i] =(ball_id,ball_x,ball_y+1)
                    color(i,self.color[i])
                    moved[i] = 1
                else:
                    color(i,self.color[i])
                    moved[i] = 0

                #time.sleep(1)

                ball2 = balls_list[i]
                #canvas.create_oval(ball2[0],ball2[1],ball2[0]+2*radius,ball2[1]+2*radius,fill='red')
                
            #check to see if all balls in goal positions
            if 1 not in moved:  
                done = True #stop while loop -> kill thread
                threadLock.release()
                
            time.sleep(animDelay)
            

        print "Exiting " + self.name



#Setup and run code:
threadLock = threading.Lock()

root = tk.Tk()
w = num_balls*2*(radius+2)+radius
h = w/3
root.geometry(str(w)+'x' + str(h))
root.bind('<KeyPress>', onKeyPress)

canvas = tk.Canvas(root,width=w, height=h)
canvas.pack()

balls_list = showBalls(num_balls,radius)

root.mainloop()
