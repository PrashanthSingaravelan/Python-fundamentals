for row in range(6):
    for column in range(7):
        if(row==0 and column%3!=0) or (row==1 and column%3==0) or (row-column==2) or (row+column==8):
           print("*",end="")
        else: 
           print(" ",end="")
    print()