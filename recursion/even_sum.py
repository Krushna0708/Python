def show(n):
    if n == 0:
        return 0
    return n + show(n - 2)
ans = show(10)
print(ans)
 
def show(n):
    if n > 10: 
        return 0
    return n + show(n + 2)
print(show(2))