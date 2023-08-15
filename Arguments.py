# this function is using arguments to find volume

def findvolume(length=1, width=1, depth=1): #defining the variable here 
    print("Length = " + str(length))
    print("Width = " + str(width))
    print("Depth = " + str(depth))
    return length + width + depth #used to return variables

findvolume(1, 2, 3)
findvolume(length = 10, depth = 5, width = 6)
findvolume(2, depth = 3, width = 4)
