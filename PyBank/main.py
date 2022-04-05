import csv
from lib2to3.pgen2.token import LESSEQUAL
import os
import math
from telnetlib import theNULL
from tracemalloc import stop




#path
#resources/budget_data.csv
path = os.path.join("Resources","budget_data.csv")

#list
months = []
profits_loss = []

#initialized value
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



#calculate change
# # find the current, find the next, subtract, save the delta
    # current number
    #print(profits_loss[x])

    # next number

   # profit_loss[x] = profits_loss[x] - 1
    #print(profits_loss)

# for x in range(len(profits_loss)):
#     if x > range(len(int(profits_loss))):
#         print(profits_loss[x+1] - profits_loss[x])
#         current_change = profits_loss[x+1] - profits_loss[x] 
#         # print(sum(current_change) / len(profits_loss))
        


   

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
#print(f'Average Change:${(sum(current_change) / len(profits_loss))}')
print(f'Greatest Increase in Profits: Mar-13 {greatest_increase}')
print(f'Greatest Decrease in Profits: Dec-10 {greatest_decrease}')



# first iteration: profits_loss[0+1] - profits_loss[0]
# second iteration: profits_loss[1+1] - profits_loss[1]

