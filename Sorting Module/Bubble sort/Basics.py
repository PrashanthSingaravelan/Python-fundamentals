# Bubble sort will not sort the list which is already sorted .
# Here j loop is only swapping. So lets check with flags

def sort(list1): # len=>6
    for i in range(len(list1)-1,0,-1): # From 5 to 0 in steps of -1
        flags=0
        for j in range(i):
            if list1[j]>list1[j+1]:   # If greater number then swap
               list1[j+1], list1[j] = list1[j], list1[j+1]
               flags=1

    print("The sorted list is : ",*list1)
    if flags==1:
        print("It is sorted by myself")
    else:
        print("It is already a sorted list")

n=input("Enter the elements : ")
list1=n.split()
sort(list1)

