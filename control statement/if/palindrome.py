# WAP to check given string is palindrome or not.
 
name  = str(input("Enter Any String or Name :"))
rev = name[::-1] #this line check string is palindrome or not.
if name == rev:
    print("The Given String is Palindrome ")
else:
    print("The Given string is Not Palindrome")