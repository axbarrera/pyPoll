import os
import csv
import itertools 

Mycsvfile = os.path.join('', 'Resources', 'election_data.csv')

with open(Mycsvfile, 'r') as csvfile:

# with open('~/Users/alexbarrera/Desktop/PyBank/budget_data.csv', newline = '') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
# Files to load (Remember to change these)

    # use of next to skip first title row in csv file
    next(reader) 
    record_count = 0
    candidates = {
        "Khan":0, 
  "Correy": 0,
  "Li": 0,
  "O'Tooley": 0
    }
    

    for row in reader:

        # print(row[2])
        # print(candidates[row[2]][1])
        candidates[row[2]] += 1
        record_count += 1

        # print(candidates[row[2]])
        # candidates[row[2]][1] += 1


    # for k, v in candidates.items():
        # print(k, v)


    print("Election Results")
    print("-----------------------------------")
    print("Total Votes:" + str(record_count))

    for k, v in candidates.items():
        percent_candidate = (v/record_count)

        print("Candidate" + str(k) + " : " + str(v) + " votes, " + str(percent_candidate) + " percent" )
        
       