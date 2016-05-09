import pandas
import matplotlib
import matplotlib.pyplot as plt
import ast
import numpy

#Set the style of the graph
matplotlib.style.use('ggplot') 

#Read the CSV file
data = pandas.read_csv('mit_pop.csv') 

#Extract every 3 rows from the original data set
data2 = data.iloc[::3,:]
data2 = data2[-50:]
data2 = data2.set_index('Year') 

rgb = ['(0,0,255)']*len(data2.index)
data2['RGB'] = rgb
#data2.loc[data2.index == 1943, 'RGB'] = '(255,0,0)'
#data2.loc[data2.index == 1946, 'RGB'] = '(255,0,0)'

data2['Total'] = data2.sum(axis=1)
data2['Total2'] = (data2['Total']/data2['Total'].max()*100)

rgb_list = list(data2['RGB'].values)
for i in range(len(rgb_list)):
	rgb_list[i] = ast.literal_eval(rgb_list[i])

print list(300-3*numpy.array(data2['Total2'].values)), rgb_list
data2['Total'].to_csv('mit_pop_final.csv')
