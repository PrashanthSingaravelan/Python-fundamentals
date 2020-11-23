# 1) read mode => Always opens an existing file
fptr=open("List methods.txt","r")

#print(fptr.read())       # Reads the entire file

# readline() => Return type => string
#print(fptr.readline())   # Reads the first line and has a self incrementation by itself
#print(fptr.readline())   # Reads the second line

# readlines() => Return type => list
print(fptr.readlines())   # Reads the entire document and returns as a list

# In write mode if the file is not there, it will create a new file and writes on it
f1=open("Prashanth.txt","w")
f1.write("Awesome")
f1.write(" Good")

# Append mode => Appends the contents 
f2=open("Prashanth.txt","a")
f2.write(" Morning")