
# Best method:Assignment
# A)Using dict()
# 1) Direct assignment
dict6=dict(Name="Prashanth",Age=18)  # And not for  dict6=dict(1="Prashanth",2="Age")
print(dict6)  # {'Name': 'Prashanth', 'Age': 18}     # keys as numbers

# 2) Using dictionary {}
dict2=dict( { "Iphone":"Xs max","Samsung":"Note 11" } )
print("Dictionary using dict method:",dict2)
# Dictionary using dict method: {'Iphone': 'Xs max', 'Samsung': 'Note 11'}

# 3) Using [],[]
dict3=dict( [ (99,"Good") , (100,"Best") ] )
print("Dictionary with each item as a pair: ",dict3)
# Dictionary with each item as a pair:  {99: 'Good', 100: 'Best'}


# B) With the use of integer keys
dict1={1:"Good",2:"Better",3:"Best"}
print("Dictionary using integer: ",dict1)
#  Dictionary using integer:  {1: 'Good', 2: 'Better', 3: 'Best'} 


# C) Insert a list into the dictionary
Dict = {'Name': 'Prashanth', 'Values': [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ",Dict)
# Dictionary with the use of Mixed Keys:  {'Name': 'Prashanth', 'Values': [1, 2, 3, 4]}


# D) Nested dictionary
dict5={1:"Eat", 2:"Sleep",
       3: {"3A":"Conquor","3B":"Repeat"} }
print("Nested Dictionary: ",dict5)
# Nested Dictionary:  {1: 'Eat', 2: 'Sleep', 3: {'3A': 'Conquor', '3B': 'Repeat'}}

# E) List of dictionary
student_details=[ # A complete list of 3 dictionaries separated by commas
       {"Id":"19MID0020" , "Subject":"Maths" , "Theory":99 , "Lab":98} , # 1st dictionary
       {"Id":"19MID0017" , "Subject":"Maths" , "Theory":90 , "Lab":88} , # 2nd dictionary
       {"Id":"19MID0067" , "Subject":"Maths" , "Theory":76 , "Lab":82} , # 3rd dictionary
 ]
print(*student_details)
