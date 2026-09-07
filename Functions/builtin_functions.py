def calculate_total(expenses_list):
    """
    Calculate the total of a list of expenses.

    Args:
        expenses_list (list): A list of expense values.

    Returns:
        int: The total of all expenses.
    """
    total = 0
    for expense in expenses_list:
        total += expense
    return total

expences = [30, 45, 70, 90]
total_expenses = sum(expences)

# Now using built-in functions to calculate total, max, and min expenses
total_expenses = sum(expences)
print(f"Total expenses: {total_expenses}")

max_expense = max(expences)
print(f"Maximum expense: {max_expense}")

min_expense = min(expences)
print(f"Minimum expense: {min_expense}")


# Now using math module to calculate square root of a number
import math
total= math.sqrt(16)
print("square root of 16 is", total)