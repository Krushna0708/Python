# print sum of odd numbers from list
lit = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for i in lit:
    if i % 2 != 0:
        sum  = sum + i
print(sum)

# list take elements from  user

lst = list(map(int, input("Enter The List Of Elements : ").split()))

sum = 0

for i in lst:
    if i % 2 != 0:
        sum = sum + i

print(sum)