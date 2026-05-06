#WAP to check the given number is single, double or three digit number.

num = int(input('Enter any digit number :'))
if num <= 9:
    print("The Given Number is Single Digit Number")
elif num <= 99:
    print("The Given Number is Double Digit Number ")
elif num <= 999:
    print("The Given Number is Three Digit Number")
else:
    print("The Given Number is More Than Three Digit Number")