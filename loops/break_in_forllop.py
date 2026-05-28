

monthly_sales = [ 1100, 200, 250 , 300, 350, 400, 450, 500 ]
months = ["jan", "feb" , "March" ,"april", "May" , "june", "July"]

target=30;

# for month in monthly_sales:
#     if month < target:
#         print(f"Month: {month} is less than target: {target}")
#         break
#     else:
#         print(f"Month: {month} is greater than target: {target}")

for month, sale in zip(months, monthly_sales):
    print(month, sale)
    if sale < target:
        print(f"Month: {month} is greater than target: {target}")
        break
    else:
        print(f"Month: {month} is less than target: {target}")
