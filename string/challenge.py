# This is logic based problem
s = 'education'
count = 0
for i in s:
    if i in 'a,e,i,o,u':
        count = count + 1
print(count)