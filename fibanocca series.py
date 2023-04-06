n=int(input("enter the number of terms ="))
a=0
b=1
print(a, b, end=' ')
for i in range(n-2):
    l=a+b
    print(l,end=" ")
    a=b
    b=l
    l=a+b
    
