try:
    a,b =  map(int,input("Enter a & b value :").split(','))
    print(a/b)
except ZeroDivisionError:
    print("Division Not Possible By Zero ")
else:
    print("Done")
finally:
    print("Success")