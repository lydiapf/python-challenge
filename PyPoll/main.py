import os
import csv

election_data = os.path.join('Resources', 'election_data.csv')

candidate = []
votes = []
unique_name = []

with open(election_data, 'r') as csvfile:

    reader = csv.reader(csvfile, delimiter='r')

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
