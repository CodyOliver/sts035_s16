import pandas
import matplotlib
import matplotlib.pyplot as plt

#Set the style of the graph
matplotlib.style.use('ggplot') 

#Read the CSV file
data = pandas.read_csv('student_faculty_ratio.csv') 

#Extract every 3 rows from the original data set
data2 = data.iloc[::3,:]
data2 = data2.set_index('Year') 

data2.to_csv('student_to_faculty_ratio.csv')


#Plot the graph by setting the x axis to the 'Year' column and y axes to 'Student-Faculty Ratio'
plt.figure()
data2.plot(x = data2.index, y = 'Student-Faculty Ratio') 
plt.show()


#Extract last 100 years (rows_ from the original data set
data3 = data.iloc[-100:,:] 

#Extract every other row from last 100 years
data3 = data3.iloc[::2,:]


#Plot the graph by setting the x axis to the 'Year' column and y axes to 'Student-Faculty Ratio'
plt.figure()
data3.plot(x = 'Year', y = 'Student-Faculty Ratio') 
plt.show()

