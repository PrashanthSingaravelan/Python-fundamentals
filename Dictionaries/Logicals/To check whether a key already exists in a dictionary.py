dict1={1:34,2:45,3:46,4:90}

def IsKeyPresent(k):
    # 1) By using Loops
    print("Loop")
    for i in dict1.keys():
       if(k==i):print("Key is Present ")
       else : print("Key is not Present")
    
    # 2) By using simple if
    print("Simple if")
    if(k in dict1.keys()):print("Key is Present")
    else: print("Key is not present")
    
IsKeyPresent(2)

