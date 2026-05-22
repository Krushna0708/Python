# find largest number in list
num = [5,10,15,20]
largest = num[0]
for i  in num:
    if i > largest:
        largest = i
print(largest)
