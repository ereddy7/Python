for i in range(1,11):
    print(i)

# ODD NUMBER

for i in range(1,11):
    if(i%2 != 0):
        print(i)


for i in range(1,11):
    if(i%2 == 0):
        continue
    else:
        print(i)

# create 3 arrays with products, sales and regions

products = ["Apple", "Samsung", "BMW"]
regions = ["NewYork", "California", "Chicago"]

sales = [1500, 2000, 2500, 3000, 4000, 5000, 6000, 7000, 8000,]

i =0

for product in products:
    for region in regions:
        rev = sales[i]
        i = i + 1
        print(f"{product} {region} and revenue is {rev}")

