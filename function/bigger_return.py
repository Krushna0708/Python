def bigger(a,b):
    if a > b:
        return a
    else:
        return b
    
a = int(input("Enter The Value Of A :"))
b = int(input("Enter The Value Of B:"))

ans = bigger(a,b)
print("Bigger Number is =",ans)