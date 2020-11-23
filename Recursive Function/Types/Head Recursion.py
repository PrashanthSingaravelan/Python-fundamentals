# Head Recursion
def fun(n): # In head recursion the operations of the function will be
    if n>0:  # performed only at the returning time.
        fun(n-1)
        print(n)

fun(5)

# Converting the same concept into loop
def fun1(m):
    i=1
    while i<=m:
        print("The value is:",i)
        i=i+1

fun1(5)