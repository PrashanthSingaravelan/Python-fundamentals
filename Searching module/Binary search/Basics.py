# 1) Sort the list
# 2) Then do binary search

position=1
def binary_search(list2,n):
    lower_bound=0
    upper_bound=len(list2)-1
    while lower_bound<=upper_bound:
        mid=(upper_bound + lower_bound)//2
        if list2[mid]==n:
            globals()["position"]=mid
            return True
        else:
            if list2[mid]<n:
                lower_bound=mid
            else:
                upper_bound=mid

list2=[12,45,89,100,432,890,1000]
list2.sort()
if binary_search(list2,890):
    print("Found at the position : ",position+1)
else:
    print("Not found")
