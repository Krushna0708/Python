# WAP to print the square of the number  only if it number is even
a = int(input("Enter any Number :"))
if a % 2 == 0:
    print("The Number is Even and it square is :",a ** a)
else:
    print("The Number is odd")