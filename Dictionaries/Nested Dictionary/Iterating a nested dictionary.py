dict1={ "Prashanth":{"DOB":"24th April 2001" , "Blood Group":"B +ve" , "Age":18},
        "Mothish": {"DOB":"19th June 2002" , "Blood Group":"A +ve" , "Age":19}  }
for i,j in dict1.items():   # i=> 1) Prashanth  2) Mothish
    print("Name : ",i)      # j=> 1) {"DOB":"24th April 2001" , "Blood Group":"B +ve" , "Age":18}
                            #     2) {"DOB":"19th June 2002" , "Blood Group":"A +ve" , "Age":19}

    for p in j: # Only keys here  p=> DOB,Blood group,Age
        print(p + ":" , j[p])
