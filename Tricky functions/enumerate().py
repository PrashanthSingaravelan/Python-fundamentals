# enumerate(iterable, start=0)
# Return type => Tuple
# Iterable : any object that supports iteration
# Start    : the index value from which the counter is to be started, by default it is 0

list1=["Good","Better","Best"]
for i in enumerate(list1): # By default Starting count=0
    print(i) # (0, 'Good')
             # (1, 'Better')
             # (2, 'Best')

for x in enumerate(list1,100):
    print(x)  #(100, 'Good')
              #(101, 'Better')
              #(102, 'Best')