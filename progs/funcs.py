def factorial(n):
    tot=1
    for i in range(1,n):
        tot+=tot*i
    return tot
print(factorial(5))