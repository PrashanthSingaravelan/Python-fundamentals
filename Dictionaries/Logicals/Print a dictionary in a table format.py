my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# Keys in [] and values in ()

# for row in zip(*( [key] + (value) for key,value in sorted(my_dict.items()))):
    #print(* row)
         #(OR)
a=zip(*( [key] + (value) for key,value in sorted(my_dict.items())))
for i in a:
    print(*i)