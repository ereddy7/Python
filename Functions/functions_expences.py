expence_person1 =[30,45,70,90]
expence_person2 =[40,23,10,86]

total_expences_person1=0

for expence in expence_person1:
    total_expences_person1 =total_expences_person1+expence

print(total_expences_person1)

print("total_expences_person1",total_expences_person1)

total_expences_person2=0

for expence in expence_person2:
    total_expences_person2 +=expence


print(total_expences_person2)
print("total_expences_person2",total_expences_person2)


# Now convert this code to Functions to reuse

def find_total(expences):
    """
    Calculate the total of a list of expenses.
    
    Args:
        expences (list): A list of expense values.
    
    Returns:
        int: The total of all expenses.
    """
    total=0
    for expence in expences:
        total +=expence
    return total


print("total_expences_person1 using functions",find_total(expence_person1))
print("total_expences_person2 using functions",find_total(expence_person2))

print(help(find_total))


