# Using nested dictionaries
students={"Prashanth":{"roll_no":20,"group":"Data Science"},
         "Sairam":{"roll_no":64,"group":"Software engineering"} }

for i in students:
    print(i)
    for j in students[i]:
        print(j ," : ",students[i][j])
