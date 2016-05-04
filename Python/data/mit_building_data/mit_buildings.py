import pandas
import matplotlib
import matplotlib.pyplot as plt
import numpy
import ast

#Set the style of the graph
matplotlib.style.use('ggplot') 

#Read the CSV file
data = pandas.read_csv('mit_building_data_raw.csv') 

data2 = data[['Cambridge Year','Cambridge Building Count']]

new_index = range(1866,2017)

data3 = data2.groupby(['Cambridge Year']).last()
data3 = data3.reindex(new_index,method='ffill').fillna(0.0).astype(int)

cambridge_data = data3.iloc[::3,:] 

data4 = data[['Boston Year','Boston Building Count']]
data4 = data4.groupby(['Boston Year']).last()
data4 = data4.reindex(new_index,method='ffill').fillna(0.0).astype(int)

boston_data = data4.iloc[::3,:]

mit_data = cambridge_data.join(boston_data)
mit_data = mit_data[-50:]
mit_data['Total'] = mit_data.sum(axis = 1)

mit_data['RGB'] = numpy.where(mit_data['Cambridge Building Count']>mit_data['Boston Building Count'], '(255,0,0)', '(0,255,0)')

rgb_list = list(mit_data['RGB'].values)
for i in range(len(rgb_list)):
	rgb_list[i] = ast.literal_eval(rgb_list[i])


print list(mit_data.index), list(300-2*numpy.array(mit_data['Total'].values)), rgb_list
mit_data = mit_data['Total']
mit_data.to_csv('buildings_final.csv')
