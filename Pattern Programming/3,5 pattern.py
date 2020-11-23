n=int(input('Enter a number : '))
for i in range(n+1):
	a=3 # even-row start value
	b=5 # odd-row start value
	for j in range(i):
		if i%2==0:
			print(a,end=' ')
			a+=3
		else:
			print(b,end=' ')
			b+=5
	print()
