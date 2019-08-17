def dtob(n):
	s=""
	while(n>0):
		r=n%2
		s=str(r)+s
		n=n//2
	return (s)
a=int(input("enter a decimal number"))
z=dtob(a)
print(z)
