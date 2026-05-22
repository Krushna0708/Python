def show(n):
    if n == 1:
        return 1
    return n + show(n - 2)
print(show(11))

def show(n):
    if n > 11:
        return 0
    return n + show(n + 2)
print(show(1))