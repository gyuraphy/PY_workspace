inFp = None	# 입력 파일
inStr = ""		# 읽어온 문자열
i= 0
inFp = open("text/test.txt", "r", encoding="utf-8" )
# inFp = open("C:/Temp/data1.txt", "r", encoding="utf-8" )
#inFp = open("C:/Temp/data1.txt", "r")

while True :
    inStr = inFp.readline()
    i += 1
    if inStr == "" :
        break;
    print("%d: %s" % (i, inStr), end = "")
    
inFp.close()