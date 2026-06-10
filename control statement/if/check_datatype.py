# WAP TO CHECK GIVEN NUMBER IS SINGLE VALUE DATA TYPE OR NOT.
num = eval(input("Enter Any Data Type :"))

# Using membership operator to solve this program.
if num in [ int , float , complex , bool ]:
    print("The Number of Data Type is Single Value Data Type ")
else:
    print("The Number of Data Type is Not Single Value Data Type , It is ",type(num))