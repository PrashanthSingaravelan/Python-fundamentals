def insertion_sort(list1):
    for i in range(1,len(list1)): # For passes. Assume 0th element is already inserted
        j=i-1
        x=list1[i]                  # If greater number then swap
        while(j>-1 and list1[j]>x): # Go on shifting till it becomes false
            list1[j+1]=list1[j]     # Wherever j points move the element to the next position 
            j=j-1
        list1[j+1]=x
    return list1

list1=[89,28,39,199,9]
a=insertion_sort(list1)
print("The list after insertion sort : ",a)
