def is_leap(year):
    if 1900<=year and year<10**5:
        if year%4==0:
            if year%100==0:
              if year%400==0:
                print("True")
              else:
               print("False")
            else:
               print("False")
        else:
           print("False")
    else:
        print("False")

year = int(input())