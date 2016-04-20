import pandas
import matplotlib
import matplotlib.pyplot as plt
import numpy

#Set the style of the graph
matplotlib.style.use('ggplot') 

#Read the CSV file
data = pandas.read_csv('mit_women.csv') 

#Extract last 100 years (rows_ from the original data set
data2 = data[['Year','Percentage of Women at MIT']].iloc[-100:,:]
data2 = data2.set_index('Year')

#Extract every other row from last 100 years
data3 = data2.iloc[::2,:]

women_data = 3*(100-2*numpy.array(data2['Percentage of Women at MIT']))
data3.to_csv('women_at_mit.csv')

#Plot the graph by setting the x axis to the 'Year' column and y axes to 'Percentage of Women at MIT'
plt.figure()
data3.plot(x = data3.index, y = 'Percentage of Women at MIT') 
plt.show()

