import sys
def btod(a):#for integer value of a
    a=int(a)
    c=1
    s=0
    while(a>0):
        r=a%10
        s=s+(r*c)
        a=a//10
        c=c*2
    return(s)
def btof(a):#for float value of a
    a=a[::-1]#reverding the input value
    c=0.5
    s=0
    a=int(a)
    while(a>0):
        r=a%10
        s=s+(r*c)
        a=a//10
        c=c/2
    return(s)
c=0
a,b=input("enter a binary number").split(".")
for i in a:
    if(i!='1' and i!='0'):
        c=c+1
for i in b:
    if(i!='1' and i!='0'):
        c=c+1
if(c!=0):
    print("tne number is not binary")
    sys.exit()
c=btod(a)
d=btof(b)
c=c+d
print(c)


        
