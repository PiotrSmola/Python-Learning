def newton(n, k):
    if k==n or k==0:
        return 1
    else:
        return newton(n-1,k-1)+newton(n-1,k)

print(newton(5,3))
