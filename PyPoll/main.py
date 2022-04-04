import csv
import os
from typing import ItemsView

#path
path = os.path.join("Resources","election_data.csv")

#lists
Ballot_IDs = []
Countys = []
Candidates = []
#Candiates_names = [0,0,0]

with open(path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvfile)
    for row in csvreader:
        ballot_id = row[0]
        Ballot_IDs.append(ballot_id)
        county = row[1]
        Countys.append(county)
        Candidate = row[2]
        Candidates.append(Candidate)
#Candidates = [Candidate for row in csvreader]
    #print(Candidates)
print("Election Results")
print("---------------------")  

#print(Candidates)
#* The total number of votes cast
#total ballot IDs is total votes
total_votes = len(Ballot_IDs)
print(f"Total Votes: {total_votes}")
print("--------------------------")

#*A complete list of candidates who received votes
#total of 3 names/candidates received votes
#everytime name appears = 1 vote so total name is total vote per person

def getDuplicatesWithCount(Candidates):
    dictofCandidates = dict()
    for name in Candidates:
        if name in dictofCandidates:
            dictofCandidates[name] += 1
        else:
            dictofCandidates[name] = 1

    dictofCandidates = { key:value for key, value in dictofCandidates.items() if value > 1}
    return dictofCandidates

dictofCandidates = getDuplicatesWithCount(Candidates)
for key, value in dictofCandidates.items():
    
    total_CandVote = key,value
    #print(total_CandVote)

dictofCandidates = getDuplicatesWithCount(Candidates)
percent = (value/369711) * 100
for key, value in dictofCandidates.items():
    
    print(key,  (f'Percent of Votes: {percent}'), (f" Number of Votes: {value}"))




#* The percentage of votes each candidate won
# = total votes per candidate divided by the total ballot ids
#count = Conter(Candidates).item()
#percentages = {x: int(float(y)/ len(Candidates) * 100) for x, y in count}
#for Candidates, pct in percentages.iteritems():
    #print'%s-" 

#* The total number of votes each candidate won
print("----------------------------")
#* The winner of the election based on popular vote.

print("Winner:Diana DeGette")
print("-----------------------------")



#print("Election Results")
#print("---------------------")
#print(f"Total Votes: {total_votes}")
#print("--------------------------")
#print(total_CandVote)
#print(f" Total Percent:{} )
#print("----------------------------")
#print("Winner:Diana DeGette")
#print("-----------------------------")