n=int(input('Enter a number : '))

## 1 value jump
print('First odd and then even',end='')
for i in range(n+1):
	a=2  # even-row start value
	b=1  # even-row start value
	for j in range(i):
		if i%2==0:				## even-row
			print(a,end=' ')
			a=a+2
		else:					## odd-row
			print(b,end=' ')
			b=b+2
	print()

print('\nFirst odd and then even',end='')
for i in range(n+1):
	a=1  # even-row start value
	b=2  # even-row start value
	for j in range(i):
		if i%2==0:				## even-row
			print(a,end=' ')
			a=a+2
		else:					## odd-row
			print(b,end=' ')
			b=b+2
	print()


## 2 values jump
print('\nFirst Even then odd')
for i in range(n):
	cnt = 1+(2*i)
	a = 2  ## 2,4,6,8,.......
	b = 0  ## 1,2,3,4,............
	for j in range(cnt):
		if i%2==0:              # even rows 
			print(a+j,end=' ')
			a = a+1
		else:					## odd rows
			b = b+1
			print(b+j,end=' ')
	print()


print('\nFirst Odd then even')
for i in range(n):
	cnt = 1+(2*i)
	a = 0  ## 2,4,6,8,.......
	b = 2  ## 1,2,3,4,............
	for j in range(cnt):
		if i%2==0:         			## even rows
			a = a+1
			print(a+j,end=' ')
		else:		       			## odd rows
			print(b+j,end=' ')
			b = b+1		
	print()

		
