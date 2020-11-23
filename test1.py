def Separate(n):
    hrs=n[:2]
    hrs=int(hrs)
    mins=n[3:5]
    mins=int(mins)
    secs=n[6:8]
    period=n[8:10]
    return hrs,mins,secs,period

def Minute_Conversion(hrs,mins):
    x=mins-60
    hrs=hrs+1
    mins=x
    return hrs,mins


n=input()
hrs,mins,secs,period=Separate(n)

if mins>=60:
        hrs1,mins=Minute_Conversion(hrs,mins)

if period is "PM":
    hrs=hrs+12
    print("{}:{}:{}".format(hrs,mins,secs))


