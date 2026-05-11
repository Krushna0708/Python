# WAP TO wether the given character is upper or lower case or special character
char = input("Enter any Character : ")
if 'a' <= char <= 'z': 
    print("The Character is Lower case")
elif 'A' <= char <= 'Z':
    print("The Character is Upper case")
else:
    print("The Character is special Character")
