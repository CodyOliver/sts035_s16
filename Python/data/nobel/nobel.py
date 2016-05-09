import pandas
import matplotlib
import matplotlib.pyplot as plt
import ast
import numpy

#Set the style of the graph
matplotlib.style.use('ggplot') 

#Read the CSV file
data2 = pandas.read_csv('nobel.csv') 

#Extract every 3 rows from the original data set
data2 = data2[-50:]
data2 = data2.set_index('Year') 

rgb = ['(212,175,55)']*len(data2.index)
data2['RGB'] = rgb

rgb_list = list(data2['RGB'].values)
for i in range(len(rgb_list)):
	rgb_list[i] = ast.literal_eval(rgb_list[i])

print list(300-300/data2['Nobel'].max()*numpy.array(data2['Nobel'].values)), rgb_list
data2['Nobel'].to_csv('nobel_final.csv')
