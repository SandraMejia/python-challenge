# PyBank

# Sandra Mejia Avendaño

# ------------------------------------------------------------------------------------

import csv
import os

count = 0                # Counter for number of votes
candidates = []          # List to store all candidates
votes = []               # List to store number of votes
percentage =[]           # List to store percentage of votes   

poll_csvpath = os.path.join('Resources', 'election_data.csv')

with open(poll_csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    
    for row in csvreader:
        count += 1 
        i = 0                            # Counter for number of candidates
        if row[2] not in candidates:     # Add names of new candidates to list
            candidates.append(row[2])
            votes.append(1)
        elif row[2] in candidates:       # If candidate is already in list, add one vote
            while i < len(candidates):
                if candidates[i] == row[2]:
                    votes[i] += 1
                i += 1 
   
for j in range(len(votes)):              # Calculate percentage of votes for each candidate
    percentage.append(round((100*votes[j]/count), 3))

maxindex = votes.index(max(votes))       # Find the index for the Winner
winner = candidates[maxindex]            # Find the winner


print("\n")
print("Election Results")
print("-------------------------")
print(f"Total Votes: {count}")
print("-------------------------")
for i in range(len(candidates)):
    print(candidates[i] + ": " + str(percentage[i]) + "% (" + str(votes[i]) + ")")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
print("\n")
    

output_path = 'summary_election.csv'

with open(output_path, 'w', newline='') as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Parameter", "Value"])
    csvwriter.writerow(["Total Votes", count])
    csvwriter.writerow(["Candidate", "Percentage of Votes", "Number of Votes Received"])
    for i in range(len(candidates)):
        csvwriter.writerow([candidates[i], percentage[i], votes[i]])
    csvwriter.writerow(["Winner", winner])
