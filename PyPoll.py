##Data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. THe percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

#add our dependencies
import csv
from pathlib import Path
#assign variable for the file to load and the path
path = Path().cwd() / 'resources' / 'election_results.csv'
file_to_load = 'resources/election_results.csv'
#open the election results and read the file
with open(file_to_load, 'r') as election_data:
#read and analyze data here
    file_reader = csv.reader(election_data)
    #Print each row in the CSV file --> goes through data
    #print header row
    headers = next(file_reader)
    print(headers)
    for row in file_reader:
        print(row)
        
#create a filename variable to a direct or indirect path to the file
file_to_save = Path().cwd() / 'analysis' / 'election_analysis.txt'
#using the with statement open file as a text file
with open(file_to_save, 'w') as outfile:
    #write three counties
    outfile.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")
