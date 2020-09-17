import os
import csv

election_data = os.path.join('Resources', 'budget_data.csv')

total_votes = len(election_data)
total_votes

candidate_count = election_data["Candidate"].value_counts()