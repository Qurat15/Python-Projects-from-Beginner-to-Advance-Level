# --------- Project: Find Maximum Number from List Using Python -------------
list = [12,13,1,4,15,6,7,8,9,33,45,23,67,45,99,34,56,44,78,21,12,97,45,34]

#assume first number is largest
largest = list[0]
for i in list:
    if i > largest:
        largest = i
print(largest)