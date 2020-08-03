#Data we need to retrieve
#Initial Analysis
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
#Challenge Analysis
# 6. Voter turnout for each county
# 7. The percentage of votes from each county out of the total count
# 8. The county with the highest turnout

#add our dependencies
import csv
from pathlib import Path
#assign variable for the file to load and the path for it and the file to save
file_to_load = Path().cwd() / 'resources' / 'election_results.csv'
file_to_save = Path().cwd() / 'analysis' / 'election_results_challenge.txt'
CANDIDATE_NAME_COL = 2
COUNTY_NAME_COL = 1

#create and set up total_votes
total_votes = 0
#create an empty dictionary  so that we can count votes for candidates
candidate_votes = {}
county_votes = {}
#create an empty dictionary for county list and county votes

#read the csv and convert it into a list of dictionaries
with open(file_to_load, 'r') as election_data:
    file_reader = csv.reader(election_data)

    #print header row and will also skip the header in the analysis
    headers = next(file_reader)
    #print each row in the CSV file

    for row in file_reader:
        total_votes += 1
        candidate_name = row[CANDIDATE_NAME_COL]
        #add unique candidate's name to the list with append
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0
        #add votes to candidate counts
        candidate_votes[candidate_name] += 1
        
        county_name = row[COUNTY_NAME_COL]
        if county_name not in county_votes:
            county_votes[county_name] = 0
        county_votes[county_name] += 1

winning_candidate_vote_count = 0
winning_candidate_name = 'no candidate'
winning_candidate_vote_percentage = 0

winning_county_vote_count = 0
winning_county_name = 'no county'
winning_county_vote_percentage = 0

#need to get percentage of votes for each candidate
for name, vote_count in candidate_votes.items():
    vote_percentage = vote_count / total_votes * 100

    if vote_count > winning_candidate_vote_count:
        winning_candidate_vote_count = vote_count
        winning_candidate_vote_percentage = vote_percentage
        winning_candidate_name = name

#percentage of votes etc for county
for name, vote_count in county_votes.items():
    vote_percentage = vote_count / total_votes * 100

    if vote_count > winning_county_vote_count:
        winning_county_vote_count = vote_count
        winning_county_vote_percentage = vote_percentage
        winning_county_name = name

part3_output = (
    "-------------------------\n"
    f"Winner: {winning_candidate_name}\n"
    f"Winning Vote Count: {winning_candidate_vote_count:,}\n"
    f"Winning Percentage: {winning_candidate_vote_percentage:.1f}%\n"
    "-------------------------"
)

part1_output = (
    'Election Results\n'
    '-------------------------\n'
    f'Total Votes: {total_votes:,}\n'
    '-------------------------\n'
    '\n'
    'County Votes:\n'
)

for name, vote_count in county_votes.items():
    vote_percentage = vote_count / total_votes * 100
    part1_output += f'{name}: {vote_percentage:.1f}% ({vote_count:,})\n'

part1_output += (
    '\n'
    "-------------------------\n"
    f'Largest County Turnout: {winning_county_name}\n'
    "-------------------------\n"
)

candidate_name_strings = []
for name, vote_count in candidate_votes.items():
    vote_percentage = vote_count / total_votes * 100
    candidate_name_strings.append(f'{name}: {vote_percentage:.1f}% ({vote_count:,})\n')

part2_output = '\n' + '\n'.join(candidate_name_strings) + '\n'

print(part1_output + part2_output + part3_output)

#using the with statement open file as a text file
with open(file_to_save, 'w') as text_file:
    #write three counties
    part2_output = ''.join(candidate_name_strings)
    text_file.write('\n' + part1_output + part2_output + part3_output)
