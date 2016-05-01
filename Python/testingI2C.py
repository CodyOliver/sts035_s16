import smbus
import sys

bus = smbus.SMBus(1)

address1 = 0x04

linear = 30

def sendToMotorsCmd(values):

    print values
    
    try:
        bus.write_i2c_block_data(address1, linear, values) 
    except IOError as e:
        print e

    return 1


balls = []


if len(sys.argv)<2:
    raise Exception("not enough arguments")

i = int(sys.argv[1])

print "given: " + str(i)

if i == 0:
    balls = [0,0,0,0,0,0,0,0,0,0]
elif i == 1:
    balls = [10,20,30,40,50,60,70,80,90,100]


if len(balls)!=0:
	sendToMotorsCmd(balls)
