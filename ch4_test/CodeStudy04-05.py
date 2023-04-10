value = input("값을 입력해주세요: ")

if value.isalpha() :
    print("글자입니다")
elif value.isdigit() :
    print("숫자입니다")
elif value.isalnum() :
    print("글자+숫자입니다")
else :
    print ("모르겠습니다")            