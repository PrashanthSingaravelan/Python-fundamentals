## Bubble sort --> O(n^2) --> Always putting the largest element at the end
def Swap(list1,j):
	temp = list1[j]  
	list1[j]= list1[j + 1]  
	list1[j + 1]= temp  
	return list1

def Sort_2nd(list1):
    for i in range(len(list1)):
        for j in range(0,len(list1)-1):
            if list1[j][1]>list1[j+1][1]:   # If true swapping takes place 
            	list1 = Swap(list1,j)              
    return list1

list1 = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print("Sorting based on 2nd element using bubble sort : {}".format(Sort_2nd(list1)))

## Using inbuilt sort()
list2 = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
list2.sort(key=lambda x:x[1])
print('Sorting based on 2nd element using inbult sort() : {}'.format(list2))

list2.sort(key=lambda x:x[0])
print('Sorting based on 1st element using inbult sort() : {}'.format(list2))

