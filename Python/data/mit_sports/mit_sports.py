import pandas
import matplotlib
import matplotlib.pyplot as plt
import ast
import numpy

#Set the style of the graph
matplotlib.style.use('ggplot') 

#Read the CSV file
data = pandas.read_csv('mit_sports.csv') 

#Extract every 3 rows from the original data set
data2 = data[-100:]
data2 = data2.iloc[::2,:]
data2 = data2[-50:]
mit_data = data2.set_index('Year') 
mit_data['Total'] = mit_data.sum(axis = 1)

mit_data['RGB'] = numpy.where(mit_data.index>=1972, '(163,31,52)', '(112,138,144)')

print mit_data

rgb_list = list(mit_data['RGB'].values)
for i in range(len(rgb_list)):
	rgb_list[i] = ast.literal_eval(rgb_list[i])

print list(data2.index), list(300-5*numpy.array(mit_data['Total'].values)), rgb_list
mit_data['Total'].to_csv('mit_sports_final.csv')