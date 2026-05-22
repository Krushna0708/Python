def show(n):
    if n == 0:
        return 0
    return n + show(n - 1)
print(show(10))