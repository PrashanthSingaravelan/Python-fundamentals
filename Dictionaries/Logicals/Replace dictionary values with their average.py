def average(student_details):
      for i in student_details:
            p=i.pop("Theory")
            q=i.pop("Lab")
            i["Theory + Lab"]=(p+q)/2
      return student_details

student_details=[ # A complete list of 3 dictionaries separated by commas
       {"Id":"19MID0020" , "Subject":"Maths" , "Theory":99 , "Lab":98} , # 1st dictionary
       {"Id":"19MID0017" , "Subject":"Maths" , "Theory":90 , "Lab":88} , # 2nd dictionary
       {"Id":"19MID0067" , "Subject":"Maths" , "Theory":76 , "Lab":82}   # 3rd dictionary
         ]

a=average(student_details)
print("The total marks are: ",a)
