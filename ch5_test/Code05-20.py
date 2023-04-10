inFp = None 
inList, inStr = [], ""
i = 1

# inFp = open("text/test.txt", "r", encoding="utf-8" )
# inFp = open("C:/Temp/data1.txt", "r", encoding="utf-8" )
#inFp = open("C:/Temp/data1.txt", "r")

# inList = inFp.readlines()
# for inStr in inList :
#     print(inStr, end="")

# inFp.close()

with open("text/test.txt", "r", encoding="utf-8" ) as inFp :
    inList = inFp.readlines()
    inStr = inFp.readline()
    print("%d: %s" % (i, inStr), end = "")
    i += 1