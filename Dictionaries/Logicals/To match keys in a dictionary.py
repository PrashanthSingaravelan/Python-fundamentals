dict1={"key1":"Good","key2":"Bad","key3":"Better"}
print(set(dict1.items())) # {('key2', 'Bad'), ('key1', 'Good'), ('key3', 'Better')}

dict2={"key2":"Bored","key4":"Worst"}
print(set(dict2.items()))  #{('key2', 'Bored'), ('key4', 'Worst')}

# for keys,values in set(dict1.items()) & set(dict2.items()):
   # print("%s : %s are present in both dict1 and dict2" %(keys,values))

for i in dict1:   # Comparing) for i in dict1: = for i in dict1.keys():
    for j in dict2:
        if i==j:
            print("{} is common".format(i))
            break
