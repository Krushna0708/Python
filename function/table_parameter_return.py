def table(n):
    result = "" 

    for i in range(1,11):
        result = result + str(n) + "x" + str(i) + "=" + str(n*i) + "\n"
    
    return result
    
ans = table(2)
print(ans)