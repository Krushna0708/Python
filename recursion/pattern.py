def pattern(n):
    if n == 0:
        return 0
    
    pattern(n - 1)
    print("#" * n)
pattern(6)

