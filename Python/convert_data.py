import pandas
import math
import sys

'''
Call this convert_data from the command line with:
	-first argument is convert_data.py
	-second argument is csv or xlsx filename
	-third arguement with number of balls
	-fourth argument type of plot:
		-linear
		-histogram

for example:

	python convert_data.py test.csv 40 linear
	or
	python convert_data.py test.xlsx 50 histogram

'''

#important constants
ball_display_height = 300


#take in arguments
if(len(sys.argv)!=4):
	raise Exception("incorrect number of arguments given")
inputPath = str(sys.argv[1])
num_balls = int(sys.argv[2])
plot_type = str(sys.argv[3])

#read in the csv or xlsx data
if(inputPath.endswith("csv")):
	data = pandas.read_csv(inputPath)
elif(inputPath.endswith("xlsx")):
	data = pandas.read_excel(inputPath)
else:
	raise Exception("incorrect data format")


#convert to display height and number of balls available
ball_positions = [0]*num_balls

lowest_value = data.min()[0]
largest_value = data.max()[0]
data_range = largest_value-lowest_value
#print data_range
height_ratio = ball_display_height/data_range
#print height_ratio

'''
print data.values[2] - dictionary like object
print data.values[2][0]  - first column
print data.values[2][1]  - second column
'''

values = data.values
num_data = len(data.index) #originally it was: max(data.shape)
print 'num_data: ', num_data

data_ratio = float(num_balls)/num_data

while data_ratio < 1.0:
	data = data.groupby(data.index / round(1/data_ratio)).mean()
	data_ratio = float(num_balls)/len(data.index)
	#Average every nth row: http://stackoverflow.com/questions/20180324/bin-pandas-dataframe-by-every-x-rows
	#Select every nth row: http://stackoverflow.com/questions/25055712/pandas-every-nth-row


try: 
	if(plot_type=="histogram"):
		try:
			if(data_ratio>0):
				for i in range(0,num_balls):
					data_index = i/data_ratio
					ball_positions[i] = int((values[data_index][0]-lowest_value)*height_ratio)
		except (IndexError, RuntimeError, TypeError, NameError):
			raise Exception("have not finished coding this data type")

	elif(plot_type=="linear"):
		data_ratio = num_balls/(num_data-1)
		if(data_ratio>0):
			for n in range(0,num_data-1):
				data = values[n][0]
				ball_positions[n*data_ratio] = int((data-lowest_value)*height_ratio)
			
			ball_positions[len(ball_positions)-1] = int((values[num_data-1][0]-lowest_value)*height_ratio)
			
			
			for i in range(1,num_balls):
				if ball_positions[i]==0:
					next_point = (0,0)

					for j in range(i,num_balls):
						if(ball_positions[j]!=0):
							next_point = (j,ball_positions[j])
							break

					x1 = i-1
					x2 = i
					x3 = next_point[0]
					y1 = ball_positions[i-1]
					y3 = next_point[1]

					y2 = (x2-x1)*(y3-y1)/(x3-x1) + y1

					ball_positions[i] = y2		

except (IndexError, RuntimeError, TypeError, NameError):
	raise Exception("have not finished coding this data type")


'''
Invert the data to match computer coordinates
'''

highest_position = max(ball_positions)
lowest_position = min(ball_positions)

for i in range(0,len(ball_positions)):
	ball_positions[i] = highest_position -(ball_positions[i]-lowest_position)


print ball_positions




