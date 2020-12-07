str1 = input("Enter a string : ")
start_str = input("Enter the start letter of the string : ")
end_str   = input("Enter the end letter of the string : ")

start = lambda x:True if x.startswith(start_str) else False
end = lambda x:True if x.endswith(end_str) else False

print("Is starting letter is p : ",start(str1))
print("Is ending letter is h : ",end(str1))