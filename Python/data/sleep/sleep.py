import pandas
import matplotlib
import matplotlib.pyplot as plt
import ast
import numpy

#Read the CSV file
data2 = pandas.read_csv('sleep.csv') 

#Extract every 3 rows from the original data set
data2 = data2.set_index('Time') 

rgb = ['(212,175,55)']*len(data2.index)
data2['RGB'] = rgb

rgb_list = list(data2['RGB'].values)
for i in range(len(rgb_list)):
	rgb_list[i] = ast.literal_eval(rgb_list[i])

print list(300-300/data2['Percent of Students'].max()*numpy.array(data2['Percent of Students'].values)), rgb_list
data2['Percent of Students'].to_csv('sleep_final.csv')
