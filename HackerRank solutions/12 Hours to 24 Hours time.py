
list1=input()

hrs=int(list1[0:2])
min=int(list1[3:5])
sec=int(list1[6:8])
dur=str(list1[8:10])

#print("{}:{}:{}{}".format(hrs,min,sec,dur))
if dur is "PM":
    print(1)
    hrs=hrs+12
    print(hrs)
    print("{}:{}:{}{}".format(hrs,min,sec,dur))




