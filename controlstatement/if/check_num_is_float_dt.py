# WAP to check wether the given number is Float data type or not.
num = eval(input("Enter Any Data Type  :"))
if type(num) == float:
    print("The Number is Float Data Type",type(num)) #type() check datatype
else:
    print("The Number is Not Float Data Type",type(num)) 