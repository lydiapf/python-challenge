import os
import csv

budget_data = os.path.join('Resources', 'budget_data.csv')

total_months = 0
total_profit = 0
net_change = 0
net_change_list = []
previous_profit = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999]


with open(budget_data, 'r') as budget:
    reader = csv.reader(budget, delimiter= ',')

    header = next(reader)
    print(header)

    first_row = next(reader)

    total_months = total_months + 1

    total_profit += int(first_row[1])

    previous_profit = int(first_row[1])




    for row in reader:
        total_months = total_months + 1

        total_profit += int(row[1])
        
        net_change = int(row[1])-previous_profit

        previous_profit = int(row[1])

        net_change_list += [net_change]

        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

monthly_average = round((sum(net_change_list) / len(net_change_list)), 2)

print("Financial Analysis")
print("---------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${total_profit}')
print(f'Average Change: ${monthly_average}')
print(f'Greatest Increase in Profits: {greatest_increase[0]} {greatest_increase[1]}')
print(f'Greatest Decrease in Profits: {greatest_decrease[0]} {greatest_decrease[1]}')

with open('PyBank.txt', 'w') as text_file:
    print(f'Financial Analysis', file=text_file)
    print("---------------------", file=text_file)
    print(f'Total Months: {total_months}', file=text_file)
    print(f'Total: ${total_profit}', file=text_file)
    print(f'Average Change: ${monthly_average}', file=text_file)
    print(f'Greatest Increase in Profits: {greatest_increase[0]} {greatest_increase[1]}', file=text_file)
    print(f'Greatest Decrease in Profits: {greatest_decrease[0]} {greatest_decrease[1]}', file=text_file)