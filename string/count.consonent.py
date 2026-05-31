# count how many consonant present in string
s = 'python learning'
count = 0
for i in s :
    if i not in 'aeiou':
        count += 1
print(count)