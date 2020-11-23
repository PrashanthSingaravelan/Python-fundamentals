allguests={  "Alice":{"Apples":7,"Cherry":5},
             "Monica":{"Hamburger":10,"Apples":5},
             "Chandler":{"Mulberry":5,"Cherry":13}  }

def totalitems(allguests,things): # totalitems(allguests,Apples)
    number=0
    for i,j in allguests.items():
        number=number + j.get(things,0)
    return number

print("Total number of apple     : ",str(totalitems(allguests,"Apples")))
print("Total number of cherry    : ",str(totalitems(allguests,"Cherry")))
print("Total number of Hamburger : ",str(totalitems(allguests,"Hamburger")))
print("Total number of Mulberry  : ",str(totalitems(allguests,"Mulberry")))

