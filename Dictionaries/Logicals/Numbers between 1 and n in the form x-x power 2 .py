
def pattern(n):

    dict1={i:i**2 for i in range(1,n+1)}
    print("Your dictionary with range {}".format(n))
    print(dict1)

n=int(input("Enter a number: "))
pattern(n)