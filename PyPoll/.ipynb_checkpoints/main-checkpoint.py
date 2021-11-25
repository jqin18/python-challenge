csvpath = os.path.join ('.', 'Resources', 'election_data.csv')

#set initial value
vote = 0
candidate = []
#open csv 
with open(csvpath) as csvfile:
    election = csv.reader(csvfile, delimiter=',')
    header = next(election)

#find total votes    
    for row in election:
        vote += 1
        candidate.append(row[2])
        
#total count each candidate recived + making a dictionary
candidate_count = {}.fromkeys(candidate, 0)
for candidate in candidate:
    candidate_count[candidate] += 1

#percentage of each candidate    
for candidate in candidate_count:
    percentage = round(float(candidate_count[candidate])/float(vote),2)*100
    print(f'{candidate}: {percentage}% ({candidate_count[candidate]})')


#winner winner chicken dinner
winner = candidate_count    
max_key = max(winner, key=winner.get)

#print the analysis result
#print("Election Results")
#print("----------------------------")
#print(f"Total Votes: {vote}")
#print("----------------------------")
#print(f"{final}")
#print("----------------------------")
#print(f"Winner: {max_key}")
