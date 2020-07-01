import pandas as pd 
import csv


# comma separated files, it is easy data transport
# CSV file and then import that into a spreadsheet to analyze the data, 
# generate graphs for a presentation, or prepare a report for publication.

with open('Hrdata.csv') as csv_read:
	csv_reader=csv.DictReader(csv_read,delimiter=',')
	line_count=0
	for row in csv_reader:
		if(line_count==0):
			print(f'Column names are {",".join(row)}')
			line_count+=1

		else:
			print(f'{row[0]} works at {row[1]} and born is {row[2]}')
			line_count+=1;
	print(f'procssed in {line_count}')





# #reading the csv file
# df=pd.read_csv('Hrdata.csv') 
# print(df)
