#If we want to represent a group of individual objects as a single entity where insertion order preserved and duplicates are allowed, then we should go for List. ֍ insertion order preserved. 
# duplicate objects are allowed. 
# heterogeneous objects are allowed. 
# List is dynamic because based on our requirement we can increase the size and decrease the size. 
# In List the elements will be placed within square brackets and with comma seperator. 
# We can differentiate duplicate elements by using index and we can preserve insertion order by using index.
# Hence index will play very important role. ֍ Python supports both positive and negative indexes. 
# +ve index means from left to right where as negative index means right to left. [10,"A","B",20, 30, 10]
# List objects are mutable.i.e we can change the content.
#
#
#
list=[] 
print(list)
print(type(list))

# 3) With Dynamic Input:
list2=eval(input("Enter List:"))
print(list2) 
print(type(list2))

#With list() Function:

l=list(range(0,10,2)) 
print(l) 
print(type(l))