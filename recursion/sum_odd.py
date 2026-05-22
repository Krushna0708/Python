def odd(n):
    if n > 10:
        return 0
    return n + odd(n + 2)
print(odd(1))
    