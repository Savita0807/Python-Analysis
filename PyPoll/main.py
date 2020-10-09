# Import OS and collections modules .This will allow us to create file paths across operating systems.
import os
import collections

# Open the output file using "write" mode. 
# If the output file is already present delete the file.
output_path = os.path.join('Analysis', 'output_file.txt')
if os.path.exists(output_path):
  os.remove(output_path)
else:
  print("The file does not exist")

# Open output file in write mode.
file1 = open(output_path, "w") 

# Module for reading CSV files
import csv
csvpath = os.path.join('Resource', 'election_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Variables Intilization
    Total_Votes = 0
    Candidate_list = []
    Poll_data = dict()
    output_queue =[]
    maximum = 0

    # Read each row of data after the header from the input file and calculate total number of votes.
    for row in csvreader:
        Total_Votes = Total_Votes + 1
        Voter_id = row[0]
        Candidate_list.append(row[2])

    #Print the final values and write the results in output file
    print("Election Results") 
    file1.write("Election Results \n") 
    print("-------------------------") 
    file1.write("------------------------- \n")  
    print("Total Votes: " + str(Total_Votes))
    file1.write("Total Votes: " + str(Total_Votes) + "\n")
    print("-------------------------") 
    file1.write("------------------------- \n")   

    Poll_data = collections.Counter(Candidate_list)
    # Loop to calculate the unique number of candidates , their total votes and percentage of votes each candidate
    for Poll_Name,Poll_count in Poll_data.items():
        print(f'{Poll_Name}: {(Poll_count/Total_Votes)*100}% ({Poll_count})')
        output_queue = Poll_Name + ": " + str(Poll_count / Total_Votes *100) + "% " + "(" + str(Poll_count) + ")"
        file1.write(str(output_queue) + "\n") 
        # Get the value of the winner
        maximum = max(Poll_data, key=Poll_data.get)  

    # Write final values to the output files.
    print("-------------------------")
    file1.write("------------------------- \n")
    # print(maximum, Poll_data[maximum])
    print("Winner: " + maximum)
    file1.write("Winner: " + maximum + "\n")
    print("-------------------------")
    file1.write("------------------------- \n")
    
    #Close the output file. 
    file1.close() 