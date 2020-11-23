# 1) Using iteration
def index1(list3,list4):
    result=[]
    for i in list4:
        for j in list3:
            if i==j:
               result.append(list3.index(j))
    print("The result using iteration : ",result)

# 2) List Comprehension
def index2(list3,list4):
    temp={y:x for x,y in enumerate(list3)}   # {'Sleep': 1, 'Eat': 0, 'Conqueor': 2, 'Repeat': 3}
    Output=[]
                                          # for i in list4:
    Output=[temp.get(i) for i in list4]   #     Output.append(temp.get(i))
                                          # print(Output)
    print("The replacement using List Comprehension : ",Output)

# 3) map()
def index3(list3,list4):
    temp={y:x for x,y in enumerate(list3)}
    Output=list(map(temp.get,list4))
    print("The replacement using map() : ",Output)

list3=["Eat","Sleep","Conqueor","Repeat"]
list4=["Repeat","Sleep","Eat","Conqueor","Sleep","Repeat"]

index1(list3,list4)
index2(list3,list4)
index3(list3,list4)
