list1 = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def leapornot(year):
    return (year%4==0 and (year%100!=0 or year%400==0))
def NumberofDays(year,month):
    if (month==2 and leapornot(year)):
        print(29)
    else:
        print(list1[month])

NumberofDays(2020,2)
