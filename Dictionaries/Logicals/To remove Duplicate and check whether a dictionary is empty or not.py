# 1) Remove Duplicate elements from the dictionary
Student={
  'dict1' : {'Name':'Prashanth','Age':24,'Food':'Biriyani'},
  'dict2' : {'Name':'Balaji'   ,'Age':67,'Food':'Curd Rice'},
  'dict3' : {'Name':'Praveen'  ,'Age':80,'Food':'Lemon Rice'},
  'dict4' : {'Name':'Prashanth','Age':24,'Food':'Biriyani'}, 
  }

result={}

for i,j in Student.items():
 if j not in result.items():
  result[i]=j

# 2) Check whther a dictionary is empty/not
  
# bool returns either true/false
  
mydict={1:2}
if bool(mydict): # It checks whther any data is in my dict/not
  print("Dictionary is full")         # If True
else:
  print("Dictionary is not empty")    # If False

