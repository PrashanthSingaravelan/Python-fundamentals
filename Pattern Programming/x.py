i=0
j=4
for row in range(5):
    for column in range(5):
        if row==i and column==j:
            print("*",end="")  # Dont leave gap after the star but the cursor remains in the same line
            i=i+1
            j=j-1
        elif(row==column):
            print("*",end="") # Dont leave gap after the star but the cursor remains in the same line
        else:
            #print(" ",end="")
            print(end=" ") # Leave gap when no star is printing and the curso remains in the same line
    print()