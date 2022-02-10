

n=int(input())
revnum=0
while n>0:
    last=n%10
    n=n//10
    revnum=revnum*10+last
print(revnum)

