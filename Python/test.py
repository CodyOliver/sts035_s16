from graphics import *
import threading
import time

balls_list =[]
radius = 10
num_balls = 40

    
def setupBalls(num,rad):
    ball_list = []
    for i in range(0,num_balls):
        ball_list.append(((i*2*rad)+3*(i+1),10))   
    return ball_list


def showBalls(balls,rad):
    for ball in balls:
        canvas.create_oval(ball[0],ball[1],ball[0]+2*rad,ball[1]+2*rad)
        
    root.mainloop()

def onKeyPress(event):
    character = event.char
    if character == 'r':
        print 'typed r'
        moveBalls()
    if character in ['2','3','4','5','6','7','8','9']:
        moveBallsTo(int(character))

    if character == '0':
        graph0()
    if character == '1':
        graph1()

def moveBalls():
    canvas.delete('all')
    for ball in balls_list:
        ball = (ball[0]+5,ball[1]+20)
        canvas.create_oval(ball[0],ball[1],ball[0]+2*radius,ball[1]+2*radius)

def moveBallsTo(num):
    for i in range(0,10):
        canvas.delete('all')
        for ball in balls_list:
            ball2 = (ball[0]+5,ball[1]+num*10+i*4)
            canvas.create_oval(ball2[0],ball2[1],ball2[0]+2*radius,ball2[1]+2*radius)
        time.sleep(1)

def graph0():
    # graph some data plot 
    thread1 = ballThread(1, "Graph-0", .1,[10,20,30,40,50,60,70,60,50,40,30,20,10,20,30,40,50,60,70,50])
    thread1.start()

def graph1():
    # draw the mit dome - kinda
    thread1 = ballThread(1, "Graph-1", .1,[160,160,160,100,100,100,80,80,60,50,44,44,50,60,80,80,100,100,100,160,160,160])
    thread1.start()

exitFlag = 0
animDelay = 0.015

class ballThread (threading.Thread):
    def __init__(self, threadID, name, index,goal_list):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.index = index
        self.goals = goal_list
    def run(self):

        #time.sleep(0) #initial delay for debugging
        print "Starting " + self.name
        
        done = False
        moved = [1]*len(self.goals)

        while not done:
            #clear current canvas for next frame            
            canvas.delete('all')
            for i in range(0,len(self.goals)):
                ball = balls_list[i]
                if ball[1] > self.goals[i]:
                    balls_list[i] = (ball[0],ball[1]-1)
                    moved[i] = 1
                elif ball[1] < self.goals[i]:
                    balls_list[i] =  (ball[0],ball[1]+1)
                    moved[i] = 1
                else:
                    moved[i] = 0

                ball2 = balls_list[i]
                canvas.create_oval(ball2[0],ball2[1],ball2[0]+2*radius,ball2[1]+2*radius)
                
            #check to see if all balls in goal positions
            if 1 not in moved:  
                done = True #stop while loop -> kill thread
                
            time.sleep(animDelay)
            


        print "Exiting " + self.name


# Create new threads
thread1 = ballThread(1, "Thread-1", .1,[0,10,20,30,40,50])
# Start new Threads
thread1.start()


balls_list = setupBalls(num_balls,radius)  

root = tk.Tk()
w = num_balls*2*(radius+2)+radius
root.geometry(str(w)+'x200')
root.bind('<KeyPress>', onKeyPress)

canvas = tk.Canvas(root,width=w, height=200)
canvas.pack()

showBalls(balls_list,radius)

