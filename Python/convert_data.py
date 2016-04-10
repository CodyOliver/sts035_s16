import pandas
import sys

'''
Call this convert_data from the command line with the second argument of csv name
for example:

	python convert_data.py test.csv

'''

inputPath = sys.argv[1]

print inputPath

#data = pandas.read_csv('/Users/Chengzhendai/Downloads/Content Data Sets.csv')

data = pandas.read_csv(inputPath)
#data.info()
print data 
