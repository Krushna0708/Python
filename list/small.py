# find small number from list
lst = [1,2,294,321,45,6,55]
small = lst[0]
for i in lst:
    if i < small:
        small = i
print(small)