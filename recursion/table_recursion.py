def table(n,i):
    if i == 11:
        return 
    print(i * n)
    return table(n , i + 1)
table(3,1)