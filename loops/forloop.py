expenses = [100,
            200,
            300,
            400,
            500]

for exp in expenses:
    print(exp)

total_expence = 0
for exp in expenses:
    total_expence = total_expence + exp

print (total_expence)
print("Range");
print(range(len(expenses)));

#3
total_expence = 0
for i in range(len(expenses)):
    print(f"Expenses: is {expenses[i]} for the month: {i+1}")
    total_expence = total_expence + expenses[i]

print(total_expence)

for i,expenses in enumerate(expenses):
    print(f"Expenses: is {expenses} for the month: {i+1}")
    total_expence = total_expence + expenses

print(total_expence)



