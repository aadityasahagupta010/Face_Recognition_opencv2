n=int(input())
n1=int((n/2)+1)
print(n1)
n2=n1-1
print(n2)
m=1
for i in range (1,n1+1):
    for j in range(i,n1):
        print(end=" ")
    for k in range(m):
        print("*",end="")
    print()
    m=m+2

m=m-4
for i in range (1,n2+1):
    for j in range(i):
        print(end=" ")
    for k in range(m):
        print("*",end="")
    print()
    m=m-2
