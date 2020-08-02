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
#create and set up total_votes
total_votes = 0
#create an empty dictionary  so that we can count votes for candidates
candidate_votes = {}

#open the election results and read the file
with open(file_to_load, 'r') as election_data:
#read and analyze data here
    file_reader = csv.reader(election_data)
    #Print each row in the CSV file --> goes through data
    #print header row and will also skip the header in the analysis
    headers = next(file_reader)
    #print each row in the CSV file
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        #add unique candidate's name to the list with append
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0
        #add votes to candidate counts
        candidate_votes[candidate_name] += 1
        
# print(total_votes)
# print(candidate_votes.keys())
# print(candidate_votes)

winning_vote_count = 0
winner = 'no one'
winning_vote_percentage = 0

#need to get percentage of votes for each candidate
for name, vote_count in candidate_votes.items():
    vote_percentage = vote_count / total_votes * 100
    #print(f'{name}: {vote_percentage:.1f}% ({vote_count:,})\n')

    if vote_count > winning_vote_count:
        winning_vote_count = vote_count
        winning_vote_percentage = vote_percentage
        winner = name
# print((
#     f'{winner} is the winner with {winning_vote_count} total'
#     f' votes and {winning_vote_percentage:.1f}% of the votes.'
# ))

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"Winning Vote Count: {winning_vote_count:,}\n"
    f"Winning Percentage: {winning_vote_percentage:.1f}%\n"
    f"-------------------------\n")
# print(winning_candidate_summary)

#create a filename variable to a direct or indirect path to the file
file_to_save = Path().cwd() / 'analysis' / 'election_results.txt'
#using the with statement open file as a text file
with open(file_to_save, 'w') as text_file:
    #write three counties
    text_file.write((
        'Election Results\n'
        '-------------------------\n'
        f'Total Votes: {total_votes:,}\n'
        '-------------------------\n'))
    for name, vote_count in candidate_votes.items():
        vote_percentage = vote_count / total_votes * 100
        text_file.write(f'{name}: {vote_percentage:.1f}% ({vote_count:,})\n')
    text_file.write(winning_candidate_summary)
