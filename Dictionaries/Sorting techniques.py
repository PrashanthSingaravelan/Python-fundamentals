from operator import itemgetter
# To get values from specific keys

dict1={"Id":"19MID0020" , "Subject":"Maths" , "Theory":99 , "Lab":98}  # 1st dictionary

# Single dictionary sorting
print(sorted(dict1.items())) # [('Id', '19MID0020'), ('Lab', 98), ('Subject', 'Maths'), ('Theory', 99)]

p=itemgetter("Id") # Doesn't return anything
print(p)           #operator.itemgetter('Id')
print(p(dict1))    #19MID0020

dict2= [  {"Id":"19MID0017" , "Subject":"Maths" , "Theory":90} , # 2nd dictionary
          {"Id":"19MID0067" , "Subject":"Maths" , "Theory":76}  ]

# List of dictionary sorting
# 1) Main dictionary=Change
dict2.sort(key=itemgetter("Theory"))
print(dict2)

# 2) Main dictionary=Unchange
sorted_users=sorted(dict2,key=itemgetter("Id"))
print(sorted_users)