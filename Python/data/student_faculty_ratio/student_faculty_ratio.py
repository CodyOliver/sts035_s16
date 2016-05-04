import pandas
import matplotlib
import matplotlib.pyplot as plt
import ast
import numpy

#Set the style of the graph
matplotlib.style.use('ggplot') 

#Read the CSV file
data = pandas.read_csv('student_faculty_ratio.csv') 

#Extract every 3 rows from the original data set
data2 = data.iloc[::3,:]
data2 = data2.set_index('Year') 

rgb = ['(0,0,255)']*len(data2.index)
data2['RGB'] = rgb
#data2.loc[data2.index == 1943, 'RGB'] = '(255,0,0)'
#data2.loc[data2.index == 1946, 'RGB'] = '(255,0,0)'

rgb_list = list(data2['RGB'].values)
for i in range(len(rgb_list)):
	rgb_list[i] = ast.literal_eval(rgb_list[i])

print list(data2.index), list(300-3*numpy.array(data2['Student-Faculty Ratio'].values)), rgb_list
data2['Student-Faculty Ratio'].to_csv('student_faculty_final.csv')

#data2.to_csv('student_to_faculty_ratio.csv')

'''
#Plot the graph by setting the x axis to the 'Year' column and y axes to 'Student-Faculty Ratio'
plt.figure()
data2.plot(x = data2.index, y = 'Student-Faculty Ratio') 
plt.show()
'''

#Extract last 100 years (rows_ from the original data set
data3 = data.iloc[-100:,:] 

#Extract every other row from last 100 years
data3 = data3.iloc[::2,:]

'''
#Plot the graph by setting the x axis to the 'Year' column and y axes to 'Student-Faculty Ratio'
plt.figure()
data3.plot(x = 'Year', y = 'Student-Faculty Ratio') 
plt.show()
'''
