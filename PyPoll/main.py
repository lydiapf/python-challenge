#importing the csv file into Python and defining the path 

import os
import csv

election_data = os.path.join('Resources', 'election_data.csv')

# defining variables and lists

candidate = []
votes = []
unique_name = []

# open csv and read, skip the header

with open(election_data, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    header = next(reader)

# add candidates to list

    for row in reader:
        candidate.append(row[2])


# use a list comphrension to count votes for each candidate

    count_candidates = [[x,candidate.count(x)] for x in set(candidate)]
    
    for row in count_candidates:
        unique_name.append(row[0])
        votes.append(row[1])

    candidate_zip = zip(unique_name, votes)
    candidate_list = list(candidate_zip)

# use maximum number of votes to determine the winner
    winner = max(votes)

    for row in candidate_list:
        if row[1] == winner:
            winner_name = row[0]       
            
# calculate the total number of votes

total_votes = len(candidate)

# khan votes calculations

khan = candidate.count('Khan')
khan_percent = khan / total_votes

# correy votes calculations

correy = candidate.count('Correy')
correy_percent = int(correy) / int(total_votes)

# li votes calculations

li = candidate.count('Li')
li_percent = li / total_votes

# o'tooley votes calculations

o_tooley = candidate.count("O'Tooley")
o_tooley_percent = o_tooley / total_votes

# Print Statements

print(f'Election Results')
print(f'-------------------------')
print(f'Total Votes: {total_votes}')
print(f'-------------------------')
print(f'Khan: {khan_percent:.3%} ({khan})')
print(f'Correy: {correy_percent:.3%} ({correy})')
print(f'Li: {li_percent:.3%} ({li})')
print(f"O'Tooley: {o_tooley_percent:.3%} ({o_tooley})")
print(f'-------------------------')
print(f'Winner: {winner_name}')
print(f'-------------------------')

# Get Output results in a txt.file
# I decided to use this method rather than the "\n" since it is easier to copy over from the previous section
# and "print" does not need to be deleted.

with open('PyPoll.txt', 'w') as text_file:
    print(f'Election Results', file=text_file)
    print(f'-------------------------', file=text_file)
    print(f'Total Votes: {total_votes}', file=text_file)
    print(f'-------------------------', file=text_file)
    print(f'Khan: {khan_percent:.3%} ({khan})', file=text_file)
    print(f'Correy: {correy_percent:.3%} ({correy})', file=text_file)
    print(f'Li: {li_percent:.3%} ({li})', file=text_file)
    print(f"O'Tooley: {o_tooley_percent:.3%} ({o_tooley})", file=text_file)
    print(f'-------------------------', file=text_file)
    print(f'Winner: {winner_name}', file=text_file)
    print(f'-------------------------', file=text_file)