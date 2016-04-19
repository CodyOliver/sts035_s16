import pandas
import matplotlib
import matplotlib.pyplot as plt

#Set the style of the graph
matplotlib.style.use('ggplot') 

#Read the CSV file
data = pandas.read_csv('mit_women.csv') 

#Extract last 100 years (rows_ from the original data set
data2 = data.iloc[-100:,:] 

#Extract every other row from last 100 years
data2 = data2.iloc[::2,:]

#Plot the graph by setting the x axis to the 'Year' column and y axes to 'Percentage of Women at MIT'
plt.figure()
data2.plot(x = 'Year', y = 'Percentage of Women at MIT') 
plt.show()

