import os
import csv

election_data = os.path.join('Resources', 'election_data.csv')

candidate = []
votes = []
unique_name = []

with open(election_data, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    header = next(reader)

    for row in reader:
        candidate.append(row[2])

    count_candidates = [[x,candidate.count(x)] for x in set(candidate)]
    
    for row in count_candidates:
        unique_name.append(row[0])
        votes.append(row[1])

    candidate_zip = zip(unique_name, votes)
    candidate_list = list(candidate_zip)

    winner = max(votes)

    for row in candidate_list:
        if row[1] == winner:
            winner_name = row[0]       
            
total_votes = len(candidate)

khan = candidate.count('Khan')
khan_percent = khan / total_votes

correy = candidate.count('Correy')
correy_percent = int(correy) / int(total_votes)

li = candidate.count('Li')
li_percent = li / total_votes

o_tooley = candidate.count("O'Tooley")
o_tooley_percent = o_tooley / total_votes

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