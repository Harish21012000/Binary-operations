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
def twoscomple(a):
    s=''
    s1='1'
    for i in a:
        if(i=='1'):
            s=s+'0'
        else:
            s=s+'1'
    while(len(s)>len(s1)):
        s1='0'+s1
    return(add(s,s1))
a=input("enter a binary number")
c=0
for i in a:
    if(i!='1' and i!='0'):
        c=c+1
if(c!=0):
    print("the entered number is not binary")
    sys.exit()
b=twoscomple(a)
print (b)
