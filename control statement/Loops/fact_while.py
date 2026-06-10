n = int(input("Enter The Number :"))
fact = 1
while n >= 1:
    fact = fact * n
    print(n,"=",fact)
    n -= 1