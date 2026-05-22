def even(n):
    if n > 20:
        return
    print(n)
    even(n + 2)
even(2)