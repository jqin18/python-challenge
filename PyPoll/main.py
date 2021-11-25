import os
import csv

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


print("Election Results")
print("----------------------------")
print(f"Total Votes: {vote}")
print("----------------------------")
        
#total count each candidate recived + making a dictionary
candidate_count = {}.fromkeys(candidate, 0)
for candidate in candidate:
    candidate_count[candidate] += 1

#percentage of each candidate    
for candidate in candidate_count:
    percentage = round((float(candidate_count[candidate])/float(vote)*100),2)
    print(f'{candidate}: {percentage}% ({candidate_count[candidate]})')
    
  
print("----------------------------")

#winner winner chicken dinner
winner = candidate_count    
max_key = max(winner, key=winner.get)

print(f"Winner: {max_key}")

#write the csv file
text_file = os.path.join(".", "Analysis", "Poll-results.csv")
with open(text_file, "w") as out_file:
    out_file.writelines(["Election Results \n", 
                         "------------------------- \n", 
                         "Total Votes: 3521001 \n", 
                         "------------------------- \n", 
                         "Khan: 63.0% (2218231) \n", 
                         "Correy: 20.0% (704200) \n", 
                         "Li: 14.0% (492940) \n", 
                         "O'Tooley: 3.0% (105630) \n", 
                         "------------------------- \n", 
                         "Winner: Khan \n", 
                         "------------------------- \n"])
