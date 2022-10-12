

num=int(input("Enter a number: "))
revnum=0
while num>0:
    last=num%10
    revnum=revnum*10+last
    num=num//10
print(revnum)

