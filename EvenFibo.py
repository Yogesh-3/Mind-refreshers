n=int(input())
x,y=2,8
print(x,y,end=" ")
c=4*y+x
while(c<=n):
    print(c,end=" ")
    x,y=y,c
    c=4*y+x
