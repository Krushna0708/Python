def count(n):
    if n == 0:
        return
    print(n)
    count(n - 1)  # function calling itself
count(10)         # function calling