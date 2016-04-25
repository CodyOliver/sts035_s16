import pandas
import matplotlib
import matplotlib.pyplot as plt

#Set the style of the graph
matplotlib.style.use('ggplot') 

#Read the CSV file
data = pandas.read_csv('mit_building_data_raw.csv') 

data2 = data[['Cambridge Year','Cambridge Building Count']]

new_index = range(1866,2017)

data3 = data2.groupby(['Cambridge Year']).last()

data3 = data3.reindex(new_index,method='ffill').fillna(0.0).astype(int)

cambridge_data = data3.iloc[::3,:] 

cambridge_data.to_csv('buildings_in_cambridge.csv')



data4 = data[['Boston Year','Boston Building Count']]

data4 = data4.groupby(['Boston Year']).last()

data4 = data4.reindex(new_index,method='ffill').fillna(0.0).astype(int)

boston_data = data4.iloc[::3,:]

boston_data.to_csv('buildings_in_boston.csv')