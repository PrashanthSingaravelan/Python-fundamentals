str1 = input().lower()
str2 = input().lower()
temp_str = str1

for i in str2:
    for j in str1:
        if i==j:
            temp_str = temp_str.replace(j,'')    
print("The string after : ",temp_str)