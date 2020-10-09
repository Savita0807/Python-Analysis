# Import OS and CSV modules.This will allow us to create file paths across operating systems.
import os
import csv

# Open the output file using "write" mode. 
# If the output file is already present delete the file.
output_path = os.path.join('Analysis', 'output_file.txt')
if os.path.exists(output_path):
  os.remove(output_path)
else:
  print("The file does not exist")

# Open output file in write mode.
file1 = open(output_path, "w") 

# Path to collect data from the Resources folder
budget_data = os.path.join('Resource', 'budget_data.csv')

#Read input file 
with open(budget_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
   
    csv_header = next(csvfile)
    Total_Num_months = 0
    Month = 0
    Fin_data = 0
    Bank_data = {}
    # Read through each row of data after the header
    for row in csv_reader:
        Total_Num_months = Total_Num_months + 1
        #print(row)
        Month = row[0]
        Fin_data = row[1]
        Bank_data[Month] = int(Fin_data)

# Intilize variables for  total calaculations.
Temp_Fin_data = 0
Temp_total_amount = 0
Total_amount = 0
Net_total_amount = 0
Average_changes = 0
Total = 0
Greatest_Increase = 0
Greatest_Decrease = 0

#Loop thru dic Bank_data to calaculate total.
for Month,Fin_data in Bank_data.items():
    Total = Fin_data + Total
    if Temp_Fin_data != 0:
       Total_amount = Fin_data - Temp_Fin_data
       Net_total_amount = Total_amount + Temp_total_amount
       if Greatest_Increase > Total_amount:
          Greatest_Increase = Total_amount
          Greatest_Inc_Month = Month
       elif Greatest_Decrease < Total_amount:
           Greatest_Decrease = Total_amount
           Greatest_Dec_Month = Month

        
    Temp_Fin_data = Fin_data
    Temp_total_amount = Net_total_amount    
    Average_changes = float(Temp_total_amount / (Total_Num_months - 1))

#Print the final values.
print("Financial Analysis") 
print("----------------------------")   
print("Total Months: " + str(Total_Num_months))
print("Total: $" + str(Total))
print("Average  Change: $" + str(Average_changes))
print("Greatest Increase in Profits: " + str(Greatest_Dec_Month) + "  " + "($"+str(Greatest_Decrease) + ")")
print("Greatest Decrease in Profits: " + str(Greatest_Inc_Month) + "  " + "($"+str(Greatest_Increase) + ")")

#Write the final values to the output file.
file1.write("Financial Analysis \n")
file1.write("---------------------------- \n")
file1.write("Total Months: " + str(Total_Num_months) + " \n")
file1.write("Total: $" + str(Total) + " \n")
file1.write("Average  Change: $" + str(Average_changes) + " \n")
file1.write("Greatest Increase in Profits: " + str(Greatest_Dec_Month) + "  " + "($"+str(Greatest_Decrease) + ")" + " \n")
file1.write("Greatest Decrease in Profits: " + str(Greatest_Inc_Month) + "  " + "($"+str(Greatest_Increase) + ")" + " \n")

#Close the output file.
file1.close() 