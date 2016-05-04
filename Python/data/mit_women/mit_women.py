import pandas
import matplotlib
import matplotlib.pyplot as plt
import numpy
import ast

#Set the style of the graph
matplotlib.style.use('ggplot') 

#Read the CSV file
data = pandas.read_csv('mit_women.csv') 

#Extract last 100 years (rows_ from the original data set
data2 = data[['Year','Percentage of Women at MIT']].iloc[-100:,:]
data2 = data2.set_index('Year')

#Extract every other row from last 100 years
data3 = data2.iloc[::2,:]
data3 = data3[-50:]
rgb = ['(0,0,255)']*len(data3.index)
data3['RGB'] = rgb

rgb_list = list(data3['RGB'].values)
for i in range(len(rgb_list)):
	rgb_list[i] = ast.literal_eval(rgb_list[i])


women_data = 3*(100-2*numpy.array(data3['Percentage of Women at MIT']))
print list(women_data), rgb_list
data3['Percentage of Women at MIT'].to_csv('mit_women_final.csv')

#Plot the graph by setting the x axis to the 'Year' column and y axes to 'Percentage of Women at MIT'
#plt.figure()
#data3.plot(x = data3.index, y = 'Percentage of Women at MIT') 
#plt.show()

