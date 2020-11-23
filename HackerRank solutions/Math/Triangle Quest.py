# Triangle quest in two lines
for i in range(1,int(input())):
    print((pow(10,i)//9)*i)
    
# Triangle quest in n lines
for i in range(1,int(input())):
    for j in range(i):
        print(i,end="")
    print()