 
x1=int(input())
v1=int(input())
x2=int(input())
v2=int(input())

def sackRace(x1,v1,x2,v2):       
    return ( (v1 > v2 and (x2 - x1) % (v1 - v2) == 0)  
         or (v2 > v1 and (x1 - x2) % (v2 - v1) == 0) ) 

if(sackRace(x1,v1,x2,v2)): 
    print("YES") 
else: 
    print("NO") 
      