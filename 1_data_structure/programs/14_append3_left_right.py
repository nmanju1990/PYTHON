n=int(input())
if n>0:
    n=-1*n
    n=(n*10)+3
    temp=0
    while n>0:
        rem=n%10
        temp=(temp*10)+rem
        n=n//10
    temp=(temp*10)+rem
    temp1=0
    while temp1>0:
        rem=temp%10
        temp1=(temp1*10)+3
        temp=temp//10
        print(-1*temp1)
    else:
        n=(n*10)+3
        temp=0
        while n>0:
            rem=temp%10
        temp1=(temp1*10)+3
        temp=temp//10
        print(temp1)

