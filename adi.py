def reverse(n):
    b=int(n)
    r=0
    d=0
    while b > 0:
        d=b%10
        print(d)
        r=(r*10)+d
        n=n/10
    return r



n=int(input())
result = reverse(n)
print(result)
