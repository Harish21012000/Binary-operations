def dtob(n):
	s=""
	while(n>0):
		r=n%2
		s=str(r)+s
		n=n//2
	return (s)


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


def sub(a,b):
    b=twoscomple(b)
    return(add(a,b))


A=""
a,b=map(int,input("enter two numbers to multiply").split(" "))
if(a<b):
    (M,Q)=(a,b)
else:
    (Q,M)=(a,b)
if(Q<0):
    Q=-Q
    Q=dtob(Q)
    while(len(Q)<32):
        Q='0'+Q
    Q=twoscomple(Q)
else:
    Q=dtob(Q)
    while(len(Q)<32):
        Q='0'+Q
if(M<0):
    M=-M
    M=dtob(M)
    while(len(M)<len(Q)):
        M='0'+M
    M=twoscomple(M)
else:
    M=dtob(M)
    while(len(M)<len(Q)):
        M='0'+M
for i in range(0,len(Q)):
    A='0'+A
q=0
c=len(Q)
print("\t\t\t\t M \t\t\t\t\t A \t\t\t\t Q\t\t    Q(-1)    C")
while(c!=0):
    if(Q[-1]=='0' and q==1):
        A=add(A,M)
        print("Q(0)= 0  and Q(-1)=1")
        print("performing a=a+m      ",end=" ")
        print(M+"  "+A+"  "+Q+"  ",q,"    ",c)
    if(Q[-1]=='1' and q==0):
        A=sub(A,M)
        print("Q(0)=1  and Q(-1)=0")
        print("performing a=a-m      ",end=" ")
        print(M+"  "+A+"  "+Q+"  ",q,"    ",c)
    q=Q[-1]
    Q=int(Q)
    Q=Q//10
    Q=str(Q)
    while(len(Q)<31):
        Q='0'+Q
    Q=A[-1]+Q
    A=int(A)
    A=A//10
    A=str(A)
    if(len(A)==31):
        A='1'+A
    else:
        while(len(A)<32):
            A='0'+A
    print("performing right shift",end=" ")
    print(M+"  "+A+"  "+Q+"  ",q,"    ",c)
    q=int(q)
    c=c-1
p=A+Q
if(a<0 and b>0):
    print("-"+twoscomple(p))
elif(a>0 and b<0):
    print("-"+twoscomple(p))
else:
    print(p)
