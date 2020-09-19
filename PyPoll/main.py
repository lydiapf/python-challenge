import os
import csv

election_data = os.path.join('Resources', 'election_data.csv')

total_votes = 0
candidates = []
votes = []
percent_votes = []

with open(election_data, 'r') as elections:
    reader = csv.reader(elections, delimiter= ',')
    
    header = next(reader)
    print(header)

    for row in elections:
        total_votes += 1

        if row[2]not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            votes.append(1)
        else:
            index = candidates.index(row[2])
            votes[index] += 1
    
    for votes in votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percent_votes.append(percentage)

    winner = max(votes)
    index = votes.index(winner)
    winning_candidate = candidates[index]

print("Election Results")
print("-------------------")
print(f'Total Votes: {total_votes}')





total_votes = len(election_data)

candidates = election_data["Candidate"].value_counts()