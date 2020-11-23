# File in which the contents has to be copied,so append mode
fptr=open("Prashanth.txt","a")

# File in which the contents has to be taken,so read mode
fptr2=open("Important function.txt","r")

for i in fptr2:
    fptr.write(i)