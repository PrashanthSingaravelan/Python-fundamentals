########################## Method-1 ##########################
list1 = [-25,-10,-7,-3,2,4,8,10]
for i in range(len(list1)-2):
    for j in range(i+1,len(list1)-1):
        for k in range(j+1,len(list1)):
            sum1 = list1[i] + list1[j] + list1[k]
            if sum1==0:
                print("The sum is 0 and the elements are {} {} {}".format(list1[i],list1[j],list1[k]))

########################## Method-2 ##########################
list1 = [-25,-10,-7,-3,2,4,8,10]
n = len(list1)
for i in range(n-1):
    left = i+1
    element = list1[i]
    right = n-1
    
    while(left<right):
        sum1 = list1[left] + element + list1[right]
        if sum1==0:
            print("The sum is 0 and the elements are {} {} {}".format(element,list1[left],list1[right]))
            left = left + 1
            right = right - 1
        elif sum1<0:
            left = left + 1
        elif sum1>0:
            right = right - 1