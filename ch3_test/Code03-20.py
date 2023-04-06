i=0
num=0

for i in range(3333, 10000) : 
    if i % 1234 == 0 :
        continue
    num += i   
    if num > 100000 :
        num -= i
        break
print("num의 값 %d"%(num))