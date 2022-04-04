import csv
import os
import math
from re import X
import pandas as pd


#path
#resources/budget_data.csv
path = os.path.join("Resources","budget_data.csv")

#list
months = []
profits_loss = []

#values
#total_months = 0
#Total_loss = 0

#open/read file
with open(path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvfile)
    for row in csvreader:
        month = row[0]
        #print(month)
        months.append(month)
        profit_loss = int(row[1])
        #print(profit_loss)
        profits_loss.append(profit_loss)
       # print(profits_loss)
#sum((profits_loss))
#print(sum(profits_loss))


#The net total amount of "Profit/Losses" over the entire period
    #total profit/losses is the sum of column
    #sum((profits_loss))
    #print(sum(profits_loss))

#* The total number of months included in the dataset
    #total months is equal to total number of rows without header
total_months = len(months)
    #print(months)
#print(total_months)



#* The changes in "Profit/Losses" over the entire period, and then the average of those changes

#calculate change
#current line - next line = current_value 
    # then subtract next line
    # =
# change is the current(profit_loss) loss - previous loss
#previous_loss = 
#next_line = X
#current_value = profit_loss - next_line

#profit_change = int(current) - int(previous_loss)
#print(profit_change)


#* The greatest increase in profits (date and amount) over the entire period
#print(max(profits_loss))
greatest_increase = max(profits_loss)


#* The greatest decrease in profits (date and amount) over the entire period
#print(min(profits_loss))
greatest_decrease = min(profits_loss)
#print(greatest_decrease)





print('Financial Analysis')
print("-------------------")
print(f"Total Months: {total_months}")
print(f'Total: ${sum(profits_loss)}')
#print(f'Average Change:'${})
print(f'Greatest Increase in Profits: Mar-13 {greatest_increase}')
print(f'Greatest Decrease in Profits: Dec-10 {greatest_decrease}')
