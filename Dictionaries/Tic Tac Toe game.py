theBoard={"top-L":" " , "top-M":" " , "top-R":" ",
          "mid-L":" " , "mid-M":" " , "mid-R":" ",
          "low-L":" " , "low-M":" " , "low-R":" ",}

def printboard(board):
    print("_____")
    print(board["top-L"] + "|" + board["top-M"] + "|" + board["top-R"])
    print("-+-+-")
    print(board["mid-L"] + "|" + board["mid-M"] + "|" + board["mid-R"])
    print("-+-+-")
    print(board["low-L"] + "|" + board["low-M"] + "|" + board["low-R"])
    print("_____")

n=input("Enter X or Y: ")
turn=n
for i in range(9):
    printboard(theBoard)
    print("Turn for " + turn + " .Move on which space?")
    move=input()
    theBoard[move]=turn
    if turn=="X":
        turn="Y"
    else:
        turn="X"
printboard(theBoard)

