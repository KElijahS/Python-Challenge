# import dependencies
import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

# Define Variables
months = 0
net_profit = 0
net_change_profits = 0
initial_profit = 0
profit = []
monthly_change = []
date = []

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # Run through data
    for row in csvreader:

      # Track number of months
      months = months + 1 

      # collect data and puts them in the lists
      date.append(row[0])
      profit.append(row[1])

      # sums all the profits up
      net_profit = net_profit + int(row[1])

      # find the average change in profits
      final_profit = int(row[1])
      monthly_change_profits = final_profit - initial_profit

      # Store changes for the months
      monthly_change.append(monthly_change_profits)

      net_change_profits = net_change_profits + monthly_change_profits
      initial_profit = final_profit

      # Find avergae change in profits
      mean_change_profits = (net_change_profits/months)

      #define min and max change variables and for dates
      max_profit_change = max(monthly_change)
      min_profit_change = min(monthly_change)
      increase_date = date[monthly_change.index(max_profit_change)]
      decrease_date = date[monthly_change.index(min_profit_change)]

    # Print everything
    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(months))
    print("Total Profits: " + "$" + str(net_profit))
    print("Average Change: " + "$" + str(int(mean_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(max_profit_change) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(min_profit_change)+ ")")
    print("----------------------------------------------------------")

with open('Financial_Analysis.txt', 'w') as text:
    text.write("---------------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("---------------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(months) + "\n")
    text.write("    Total Profits: " + "$" + str(net_profit) +"\n")
    text.write("    Average Change: " + '$' + str(int(mean_change_profits)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(max_profit_change) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(min_profit_change) + ")\n")
    text.write("---------------------------------------------------------------\n")
