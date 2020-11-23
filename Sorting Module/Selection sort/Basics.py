def selectionsort(list1):
    for i in range(len(list1)):
        min=i
        for j in range(i+1,len(list1)): # For comparing the min value with the entire list
            if list1[j] < list1[min] :
                min=j
        # Swap that min value to the first
        list1[min],list1[i]=list1[i],list1[min]
    print("The sorted list : ",*list1)

n=input("Enter the elements : ")
list1=n.split()
selectionsort(list1)
