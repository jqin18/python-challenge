# Dependencies
import os
import csv

#read the data csv file
csvpath = os.path.join ('.', 'Resources', 'budget_data.csv')

#set the initial value
total_revenue = 0
pl= []
revenue_change = []
months = []

#open csv with no header
with open(csvpath) as csvfile:
    budget = csv.reader(csvfile, delimiter=',')
    header = next(budget)
    
#ggetting the total month and total revenue
    for row in budget:
        month = row[0]
        months.append(row[0])
        total_month = len(months)
        total_revenue = total_revenue + int(row[1])
        pl.append(int(row[1]))
        
#getting the average change        
for i in range(len(pl)-1):
        revenue_change.append(int(pl[i+1]) - int(pl[i]))
        total_change = sum(revenue_change)
average = total_change/85

#Greatest incraese
for n in range(len(revenue_change)):
    greatest_increase = max(revenue_change)

#Greatest incraese month
month_gc = months[revenue_change.index(max(revenue_change))+1]


#Greatest decrease
for n in range(len(revenue_change)):
    greatest_decrease = min(revenue_change)

#Greatest decrease month
month_gd = months[revenue_change.index(min(revenue_change))+1]


#print the analysis result
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_month}")
print(f"Total: ${total_revenue}")
print(f"Average change: ${round(average,2)}")
print(f"Greatest increase in profit : ${greatest_increase} ({month_gc})")
print(f"Greatest decrease in profit : ${greatest_decrease} ({month_gd})")

#output in another csv file
output_path = os.path.join(".", "Analysis", "Analysis.csv")
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([f"Total Months: {total_month}"])
    csvwriter.writerow([f"Total: ${total_revenue}"])
    csvwriter.writerow([f"Average change: ${round(average,2)}"])
    csvwriter.writerow([f"Greatest increase in profit : ${greatest_increase} ({month_gc})"])
    csvwriter.writerow([f"Greatest decrease in profit : ${greatest_decrease} ({month_gd})"])