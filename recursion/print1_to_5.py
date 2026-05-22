def show(n):
    if n == 6:
        return
    print(n)
    show(n + 1)
show(1)