'Multiply without using * operator'
def mul(n,i):
    if i == 0:
        return 0
    return n + mul(n , i - 1)
ans = mul(5,6)
print(ans)