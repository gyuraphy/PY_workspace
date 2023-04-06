primes = []
for num in range(3, 101):
    # 모든 수는 1과 자기 자신으로 나누어 떨어지므로, 2부터 자기 자신-1까지 반복합니다.
    for i in range(2, num):
        # 만약 나누어 떨어지는 수가 있다면, 소수가 아니므로 반복을 중단합니다.
        if (num % i) == 0:
            break
    else:
        primes.append(num)
        # 소수인 경우 출력합니다.        
        print(num, end=" ")
print(primes)