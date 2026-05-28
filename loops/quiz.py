office_supplies = ["pen", "paper", "stapler"]
kitchen_supplies = ["fork", "knife", "spoon"]
combined_list =  kitchen_supplies + office_supplies
print(combined_list)
print(combined_list[2: 4])


animals = ["cat", "dog", "rabbit", "wolf"]
#animals.remove("lion")

if(animals.count("lion")>0):
    animals.remove("lion")


prices = [300, 50, 1200, 10]
sorted(prices)
print(prices)
print(prices[2])

prices.sort()
print(prices)
print(prices[2])


age = 17
if age >= 30:
    print("Adult")
elif age > 18 and age < 30:
    print("Young adult")
else:
    print("Minor")

for i in range(2,10):
    if i%5==0:
        break
    print(i)


fruits = ["apple", "banana", "cherry", "date"]
print("__sizeof__")
print(fruits.__sizeof__())

fruits.append("orange")

for i in range(4):
    print(i)

print("Last")
lst = [1, [2, 3], 4, [5, [6, 7]]]
print(lst)
print(lst[2])
print(lst[3])
print(lst)

print(lst[3][1][1])