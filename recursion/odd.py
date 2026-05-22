def odd(n):
    if n > 20:
        return
    print(n)
    odd(n + 2)
odd(1)