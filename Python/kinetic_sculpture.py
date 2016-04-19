from graphics import *
from Tkinter import *
import threading
import time

balls_list =[]
radius = 10
num_balls = 50
done = True

global selectedIndex
selectedIndex = 0
    

def showBalls(num,rad):

    ball_list = []

    #equally space out the balls
    for i in range(0,num_balls):
        ball_list.append(((i*2*rad)+3*(i+1),10))   

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

def onKeyPress(event):
    global selectedIndex
    character = event.keysym
    print character
    
    if character == '0':
        graph0()
    if character == '1':
        graph1()

    if character == '2':
        graph2()

    if character == 'Down':
        moveSelectedBall(10)

    if character == 'Up':
        moveSelectedBall(-10)

    if character == 'Left':
        selectedIndex = changeSelection(selectedIndex,-1)

    if character == 'Right':
        selectedIndex = changeSelection(selectedIndex, 1)

    if character == 'r':
        colorAll('red')

    if character == 'b':
        colorAll('blue')

    if character == 'g':
        colorAll('green')

def colorAll(color):
    for ball in balls_list:
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


exitFlag = 0
animDelay = 0.015

class ballThread (threading.Thread):
    def __init__(self, threadID, name, color,index,goal_list):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.index = index
        self.goals = goal_list
        self.color = color
    def run(self):

        #time.sleep(0) #initial delay for debugging
        print "Starting " + self.name
        done = False

        threadLock.acquire()

        colorAll(self.color)

        for i in range(0,len(balls_list)):
            if i >= len(self.goals):
                canvas.itemconfigure(balls_list[i][0],fill='')

        self.goals = self.goals + [0]*(len(balls_list)-len(self.goals))
        moved = [1]*len(self.goals)


        while not done:
            #clear current canvas for next frame            
            #canvas.delete('all')
            for i in range(0,len(self.goals)):
                ball = balls_list[i]

                #print ball
                #print self.goals[i]
                
                if ball[2] > self.goals[i]:
                    canvas.move(ball[0],0,-1)
                    balls_list[i] = (ball[0],ball[1],ball[2]-1)
                    moved[i] = 1
                elif ball[2] < self.goals[i]:
                    canvas.move(ball[0],0,1)
                    balls_list[i] =(ball[0],ball[1],ball[2]+1)
                    moved[i] = 1
                else:
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
