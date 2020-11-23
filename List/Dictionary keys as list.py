# 1) dict.keys()
def getList(dict1):
    return dict1.keys()       # return list(dict1.keys()) => Returns the keys in list
    # But returns as a dictionary
dict1={1:"Prashanth",2:"Team Building"}
print("The keys of dict using dict.keys() is:",getList(dict1))

# 2) Naive approach
def getList2(dict2):
    list=[]
    for i in dict2.keys():
        list.append(i)
    return list # This list contains only keys
dict2={"R":"Ross","C":"Chandler","M":"Monica"}
print("The keys of dict using Naive approach is:",getList2(dict2)) 

# 3) itemgetter
from operator import itemgetter

def getList(dict):
    return list(map(itemgetter(0), dict.items()))

dict={'a': 'Geeks', 'b': 'For', 'c': 'geeks'}
print("The keys of dict using map() and itemgetter",*getList(dict))