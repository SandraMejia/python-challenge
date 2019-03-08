# PyBank

# Sandra Mejia Avendaño

# ------------------------------------------------------------------------------------

import csv
import os

count = 0            # Counter for number of months
net_total = 0        # Net total amount of Profit/Losses
changes = []         # List of the changes in Profit/Losses
change = 0           # Punctual change - in every iteration
add_to_list = False  # Boolean to ensure that Changes[] start with row[2] - row[1]
minchange = 0        # Greatest increase in Profits
maxchange = 0        # Greatest decrease in Losses

budget_csvpath = os.path.join('Resources', 'budget_data.csv')

with open(budget_csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    
    for row in csvreader:
        if add_to_list == True:
            change = int(row[1]) - prev  # Append to list of changes
            changes.append(change)
        if change < minchange:           # Find minimum change
            minchange = change
            mindate = row[0]
        elif change > maxchange:         # Find maximum change
            maxchange = change
            maxdate = row [0]    
        count += 1                       # Count number of months
        net_total += int(row[1])         # Add to Total Net Profit/Loss
        prev = int(row[1])               # Store change for next comparisson
        add_to_list = True

avg = sum(changes)/len(changes)          # Find average change
avg = round(avg,2)      

print("\n")
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {count}")
print(f"Total: ${net_total}")
print(f"Average Change: {avg}")
print(f"Greatest Increase in Profits: {maxdate} (${maxchange})")
print(f"Greatest Decrease in Profits: {mindate} (${minchange})")
print("\n") 

#-------

output_path = 'summary_budget.csv'

with open(output_path, 'w', newline='') as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(["Parameter", "Value"])
    csvwriter.writerow(["Total Months", count])
    csvwriter.writerow(["Net Total", net_total])
    csvwriter.writerow(["Average Change", avg])
    csvwriter.writerow(["Greatest Increase", maxchange])
    csvwriter.writerow(["Greatest Increase Date", maxdate])
    csvwriter.writerow(["Greatest Decrease", minchange])
    csvwriter.writerow(["Greatest Decrease Date", mindate])

output_path = "summary_budget.txt"

