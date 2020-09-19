import os
import csv

election_data = os.path.join('Resources', 'budget_data.csv')

total_votes = len(election_data)
total_votes

total_votes = 0
candidates = []
votes = []
percent_votes = []

with open(election_data, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter= ',')
    
    header = next(reader)
    
    print(header)



total_votes = len(election_data)
total_votes = 

candidate_count = election_data["Candidate"].value_counts()