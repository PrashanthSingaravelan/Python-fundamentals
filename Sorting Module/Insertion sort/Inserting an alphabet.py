def insertion_sort(list2):
    for i in range(1,len(list2)): # For passes. Assume 0th element is already inserted
        j=i-1
        x=list2[i]
        while(j>-1 and list2[j]>x): # Go on shifting till it becomes false
            list2[j+1]=list2[j]  # Wherever j points move the element to the next position 
            j=j-1
        list2[j+1]=x
    return list2

list1=["A","B","D","E","C"]
print("The list before sort : ",list1)

list2=[ord(i) for i in list1]  # Convert the list from ASCII to integer

insertion_sort(list2) # Function call

list3=[chr(i) for i in list2]  # Convert the list from integer to ASCII

print("The List after sort : ",list3)
