import sys
def add(a,b):
    result=''
    carry=0
    for i in range(len(a)-1,-1,-1):
        r=carry
        if(b[i]=='1'):
            r=r+1
        if(a[i]=='1'):
            r=r+1
        if(r%2==1):
            result='1'+result
        else:
            result='0'+result
        if(r<2):
            carry=0
        else:
            carry=1
    if(carry==1):
        result='1'+result
    return (result)
a,b=input("enter two binary numbers").split(" ")
c=0
for i in a:
    if(i!='1' and i!='0'):
        c=c+1
for i in b:
    if(i!='1' and i!='0'):
        c=c+1
if(c!=0):
    print("the entered numbers are not binary")
    sys.exit()
while(len(a)<len(b)):
    a='0'+a
while(len(b)<len(a)):
    b='0'+b
s=add(a,b)
print(s)

