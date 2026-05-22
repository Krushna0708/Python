# count  odd number in list

odd = [1,2,3,4,5,6,7,8,9,10]
count = 0
for i in odd:
    if i % 2 != 0:
        count = count + 1
        print(count)