# 유니코드 표를 참고해서
# 한글의 유니코드 범위
# 영어의 대,소문자 유니코드 범위
# 특수문자의 유니코드 범위
# 숫자의 유니코드 범위
a = input()
if a >= 44032 and a <= 55203 :
    print("한글입니다")
elif a >= 65 and a <= 90 :
    print("영어 대문자입니다")
elif a >= 97 and a <= 122 :
    print("영어 소문자입니다")
elif a >= 48 and a <= 57 :
    print("영어 소문자입니다")