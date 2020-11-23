dict1={1:10,2:40}
dict2={3:21,8:45}
dict3={6:54,8:12}

dict4={}
for i in (dict1,dict2,dict3):
  dict4.update(i)
  
 
print(dict4)

# Note : Dict has no attirbute append
# Only list has append attribute