print('Module1 is successfully imported')  #This print statement is used for confirming the imported file

test_string = "Sample text"

def find_index(to_search,target):
    for i,j in enumerate(to_search):
        if j==target:
            return i
    return -1

to_search = ['Maths','Physics','Chemistry']
target    = 'Chemistry'

print(find_index(to_search,target))
